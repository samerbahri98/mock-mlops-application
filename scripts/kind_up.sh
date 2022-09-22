export KUBECONFIG=_cache/admin.conf

# create registry container unless it already exists
reg_name='kind-registry'
reg_port='5001'
if [ "$(docker inspect -f '{{.State.Running}}' "${reg_name}" 2>/dev/null || true)" != 'true' ]; then
  docker run \
    -d --restart=always -p "127.0.0.1:${reg_port}:5000" --name "${reg_name}" \
    registry:2
fi


./kind/kind create cluster --name=open-company --config=./k8s/manifests/kind.cluster.yml

./kind/kind get kubeconfig --name open-company > _cache/admin.conf

./kind/kubectl apply -f ./k8s/manifests/registry.configmap.yml
