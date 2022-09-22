export KUBECONFIG=_cache/admin.conf

# create registry container unless it already exists
pip3 install docker
python3 ./scripts/load_registry.py

./kind/kind create cluster --name=open-company --config=./k8s/manifests/kind.cluster.yml

./kind/kind get kubeconfig --name open-company > _cache/admin.conf

./kind/kubectl apply -f ./k8s/manifests/registry.configmap.yml
