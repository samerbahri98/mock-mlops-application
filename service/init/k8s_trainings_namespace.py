import os
import requests
import json


def set(jwt):
    k8s_env_url = f"{os.getenv('PORTAINER_HOST')}/api/endpoints/1/kubernetes/api/v1/namespaces"
    request = requests.post(k8s_env_url,
                            headers={'Authorization': f'Bearer {jwt}'},
                            json={
                                "apiVersion": "v1",
                                "kind": "Namespace",
                                "metadata": {
                                    "name": "trainings"
                                }
                            })
    if request.status_code != 201 and request.status_code != 409:
        #201: created / 409: conflict, means namespace already exists
        raise Exception(json.dumps(request.json()))
    return
