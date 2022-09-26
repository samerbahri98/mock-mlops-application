from init import k8s_env,keycloak

def init(jwt):
    k8s_env.set(jwt)
    # keycloak.set(jwt)
    return