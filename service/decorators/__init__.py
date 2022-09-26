import requests
import os
from functools import wraps


def with_portainer(func):
    login_url=f"{os.getenv('PORTAINER_HOST')}/api/auth"
    request = requests.post(login_url,json={
        "username":os.getenv("PORTAINER_USER"),
        "password":os.getenv("PORTAINER_PASSWORD")
    })
    if request.status_code != 200:
        raise Exception("could not get jwt")
    jwt= request.json()["jwt"]
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(jwt,*args, **kwargs)
    return wrapper