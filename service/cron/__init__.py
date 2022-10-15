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
    if "PORTAINER_ID" not in os.environ:
        logging.debug(msg="PORTAINER NOT SET")
        return
    logging.debug(msg="job started")
    portainer_id = os.getenv("PORTAINER_ID")

    logger_cursor.execute(
        "select resourceVersion from logs order by resourceVersion limit 1")
    logger_cursor_results = logger_cursor.fetchall()
    resource_version = logger_cursor_results[0][0] if len(
        logger_cursor_results) == 1 else "0"
    k8s_env_url = f"{os.getenv('PORTAINER_HOST')}/api/endpoints/{portainer_id}/kubernetes/api/v1/namespaces/trainings/pods?resourceVersion={resource_version}"
    request = requests.get(k8s_env_url,
                           headers={'Authorization': f'Bearer {jwt}'})
    if request.status_code != 200:
        raise Exception("could not get pods")
    response = request.json()
    if response["metadata"]["resourceVersion"] == resource_version:
        return
    resource_version = response["metadata"]["resourceVersion"]
    for pod in response["items"]:
        name = pod["metadata"]["name"]
        state = pod["status"]["phase"]
        sql, val = "insert into logs (name,resourceVersion,state) values (%s,%s,%s,%s)", (
            name, resource_version, state)
        logger_cursor.execute(sql, val)
        loggerdb.commit()
    return
