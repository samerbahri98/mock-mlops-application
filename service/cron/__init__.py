from time import time
from urllib import request, response
# import schedule
import os
import requests
# import time
import logging
from db import loggerdb, logger_cursor
from decorators import with_portainer


@with_portainer
def job(jwt):
    logging.info(msg="job started")
    logger_cursor.execute(
        "select resourceVersion from logs order by resourceVersion limit 1")
    logger_cursor_results = logger_cursor.fetchall()
    resource_version = logger_cursor_results[0][0] if len(
        logger_cursor_results) == 1 else "0"
    k8s_env_url = f"{os.getenv('PORTAINER_HOST')}/api/endpoints/1/kubernetes/api/v1/namespaces/trainings/pods?resourceVersion={resource_version}"
    request = requests.get(k8s_env_url,
                           headers={'Authorization': f'Bearer {jwt}'})
    if request.status_code != 200:
        raise Exception("could not get pods")
    response = request.json()
    if response["metadata"]["resourceVersion"] == resource_version:
        return
    branch = os.getenv("BRANCH") if "BRANCH" in os.environ else "main"
    resource_version = response["metadata"]["resourceVersion"]
    for pod in response["items"]:
        name = pod["metadata"]["name"]
        state = pod["status"]["phase"]
        sql, val = "insert into logs (branch,name,resourceVersion,state) values (%s,%s,%s,%s)", (
            branch, name, resource_version, state)
        logger_cursor.execute(sql, val)
        loggerdb.commit()
    return


# def set():
#     interval = os.getenv(
#         "SCRAPE_INTERVAL") if "SCRAPE_INTERVAL" in os.environ else 10
#     schedule.every(interval).seconds.do(job)
#     while True:
#         schedule.run_pending()
#         time.sleep(1)