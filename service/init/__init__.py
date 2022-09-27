from init import k8s_env, k8s_trainings_namespace


def init(jwt):
    k8s_env.set(jwt)
    k8s_trainings_namespace.set(jwt)
    return
