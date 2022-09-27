import docker

client = docker.from_env()

print("====PULL REGISTRY====")
client.images.pull("registry:2")

filters = {"name": "kind-registry", "status": "running"}
running_containers = client.containers.list(filters=filters)
print("====START REGISTRY====")

if len(running_containers) == 0:
    client.containers.run(image="registry:2",
                          name="kind-registry",
                          ports={5000: 5001},
                          restart_policy={"Name": "always"},
                          detach=True,
                          network="kind")

local_images = {
    "ghcr.io/samerbahri98/mock-mlops-application-training:main":
    "localhost:5001/mock-mlops-application-training:main",
    "portainer/agent:linux-amd64":
    "localhost:5001/portainer-agent:linux-amd64",
}
print("====LOAD CONTAINERS====")
for key in local_images:
    print(f"====PULL {key}====")
    client.images.pull(key).tag(local_images[key])
    print(f"====PUSH {key}====")
    client.images.push(local_images[key])
