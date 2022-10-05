import os
from urllib import response
import requests
import json
from requests_toolbelt import MultipartEncoder


def set(jwt):
    k8s_env_url = f"{os.getenv('PORTAINER_HOST')}/api/endpoints"
    data = MultipartEncoder(
        fields={
            'Name': 'kind',
            'EndpointCreationType': "2",
            'URL': 'tcp://mock-mlops-cluster-control-plane:30080',
            'GroupID': "1",
            'TLS': "true",
            'TLSSkipVerify': "true",
            'TLSSkipClientVerify': "true"
        })
    request = requests.post(k8s_env_url,
                            headers={
                                'Authorization': f'Bearer {jwt}',
                                'Content-type': data.content_type
                            },
                            data=data)
    response = request.json()
    if request.status_code != 200 and request.status_code != 409:
        #200: created / 409: conflict, means portainer already connected to k8s
        raise Exception(json.dumps(response), request.status_code)
    if request.status_code == 409:
        request = requests.get(k8s_env_url,
                               params={'search': 'kind'},
                               headers={'Authorization': f'Bearer {jwt}'})
        response = request.json()
        if request.status_code != 200:
            raise Exception(json.dumps(response), request.status_code)
        response = response[0]
    os.environ["PORTAINER_ID"] = str(response["Id"])
    return
