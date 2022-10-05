import os
from urllib import request
import requests
import json


def set(jwt):
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    REDIRECT_URI = os.getenv('REDIRECT_URI')
    with open('keycloak/well_known.json') as f:
        well_known_content = f.read()
        WELL_KNOWN = json.loads(well_known_content)
        k8s_env_url = f"{os.getenv('PORTAINER_HOST')}/api/settings"
        data = {
            "authenticationMethod": 3,
            "enableTelemetry": False,
            "oauthSettings": {
                "AccessTokenURI": WELL_KNOWN["token_endpoint"],
                "AuthorizationURI": WELL_KNOWN["authorization_endpoint"],
                "ClientID": CLIENT_ID,
                "ClientSecret": CLIENT_SECRET,
                "DefaultTeamID": 0,
                "LogoutURI":
                f'{WELL_KNOWN["end_session_endpoint"]}?redirect_uri={REDIRECT_URI}',
                "OAuthAutoCreateUsers": True,
                "RedirectURI": REDIRECT_URI,
                "ResourceURI": WELL_KNOWN["userinfo_endpoint"],
                "SSO": True,
                "Scopes": "email",
                "UserIdentifier": "email"
            }
        }
        request = requests.put(k8s_env_url,
                               headers={
                                   'Authorization': f'Bearer {jwt}',
                                   'Content-type': 'application/json'
                               },
                               json=data)
        if request.status_code != 200:
            raise Exception(json.dumps(request.json()), request.status_code)
        return
