mkdir _cache

reset_cache(){
    rm -rf _cache/kind-linux-amd64.sha256sum _cache/kind-linux-amd64 _cache/kubectl _cache/kubectl.sha256 _cache/kubectl.sha256sum;

    rm -rf _cache/checksums.txt _cache/k9s.sha256sum _cache/k9s _cache/LICENSE _cache/README.md;
    
    # rm -rf _cache/helm-$HELM_VERSION-linux-amd64.tar.gz.sha256sum _cache/linux-amd64
}

reset_cache;
cp kind/kind _cache/kind-linux-amd64
cp kind/kubectl _cache/kubectl
cd _cache

# KIND

wget https://github.com/kubernetes-sigs/kind/releases/download/$KIND_VERSION/kind-linux-amd64.sha256sum

if ! sha256sum -c kind-linux-amd64.sha256sum ; then
    wget https://github.com/kubernetes-sigs/kind/releases/download/$KIND_VERSION/kind-linux-amd64;
    if ! sha256sum -c kind-linux-amd64.sha256sum ; then
        echo "####ERROR####";
        exit 1;
    fi
    mv kind-linux-amd64 ../kind/kind
fi

# KUBECTL

wget https://dl.k8s.io/$KUBECTL_VERSION/bin/linux/amd64/kubectl.sha256;

echo "$(cat ./kubectl.sha256) kubectl" > ./kubectl.sha256sum


if ! sha256sum -c kubectl.sha256sum; then
    wget https://dl.k8s.io/release/$KUBECTL_VERSION/bin/linux/amd64/kubectl;
    if ! sha256sum -c kubectl.sha256sum ; then
        echo "####ERROR####";
        exit 1;
    fi
    mv kubectl ../kind/kubectl
fi

# K9S

rm -rf ../kind/k9s

wget https://github.com/derailed/k9s/releases/download/$K9S_VERSION/checksums.txt;

cat checksums.txt | grep k9s_Linux_x86_64.tar.gz > ./k9s.sha256sum


if ! sha256sum -c k9s.sha256sum; then
    wget https://github.com/derailed/k9s/releases/download/$K9S_VERSION/k9s_Linux_x86_64.tar.gz;
    if ! sha256sum -c k9s.sha256sum ; then
        echo "####ERROR####";
        exit 1;
    fi
fi
tar -xvf ./k9s_Linux_x86_64.tar.gz
mv k9s ../kind/k9s

# # HELM3

# wget https://get.helm.sh/$HELM_VERSION-linux-amd64.tar.gz.sha256sum

# if ! sha256sum -c k9s.sha256sum; then
#     wget https://get.helm.sh/helm-$HELM_VERSION-linux-amd64.tar.gz;
#     if ! sha256sum -c k9s.sha256sum ; then
#         echo "####ERROR####";
#         exit 1;
#     fi
# fi
# tar -xvf ./helm-$HELM_VERSION-linux-amd64.tar.gz
# mv ./linux-amd64/helm ../kind/helm

cd ../kind

chmod +x ./kind ./kubectl ./k9s
#  ./helm

cd ../


reset_cache;
