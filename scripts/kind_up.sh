export KUBECONFIG=_cache/admin.conf

# create registry container unless it already exists
./kind/kind create cluster --name=mock-mlops-cluster --config=./k8s/manifests/kind.cluster.yml

./kind/kind get kubeconfig --name mock-mlops-cluster > _cache/admin.conf

python ./scripts/load_registry.py

./kind/kubectl apply -f ./k8s/manifests/registry.configmap.yml

python ./scripts/generate_docker_kubeconfig.py

# ./kind/kubectl apply -f ./k8s/manifests/portainer-agent.yml