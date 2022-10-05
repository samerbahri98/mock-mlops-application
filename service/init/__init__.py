from init import k8s_env, k8s_trainings_namespace, keycloak, mysql_migrations


def init(jwt):
    mysql_migrations.set()
    k8s_env.set(jwt)
    k8s_trainings_namespace.set(jwt)
    keycloak.set(jwt)
    return
