import re

admin_conf_file = open('_cache/admin.conf', 'rt')
admin_conf = admin_conf_file.read()
admin_conf_file.close()
docker_admin_conf = re.sub("127\.0\.0\.1:[0-9]*\n",
                           "mock-mlops-cluster-control-plane:6443\n",
                           admin_conf)
docker_admin_conf_file = open("_cache/docker.admin.conf", "w")
docker_admin_conf_file.write(docker_admin_conf)
docker_admin_conf_file.close()
