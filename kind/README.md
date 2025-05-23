## Kind README

### Install kind for running local kubernetes clusters
https://kind.sigs.k8s.io/docs/user/quick-start/#installation
```
# For Intel Macs
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.29.0/kind-darwin-amd64
# For M1 / ARM Macs
[ $(uname -m) = arm64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.29.0/kind-darwin-arm64
chmod +x /tmp/kind
mv /tmp/kind /usr/local/bin/kind
kind --version
```

### Create Cluster
https://kind.sigs.k8s.io/docs/user/quick-start/#creating-a-cluster
```
kind create cluster
kubectl cluster-info --context kind-kind
docker ps
kubectl config use-context kind-kind
```

### Create Ingress
https://kind.sigs.k8s.io/docs/user/ingress/


https://kind.sigs.k8s.io/docs/user/quick-start/#deleting-a-cluster
Delete existing kind cluster
```
kind delete cluster
```
* extraPortMapping
Create a single node kind cluster with extraPortMappings to allow the local host
to make requests to the Ingress controller over ports 80/443.
```
cat <<EOF | kind create cluster --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP
EOF
```
* Ingress NGINX
```
kubectl apply -f https://kind.sigs.k8s.io/examples/ingress/deploy-ingress-nginx.yaml
```
Now the Ingress is all setup. Wait until is ready to process requests running:
```
kubectl wait --namespace ingress-nginx \
  --for=condition=ready pod \
  --selector=app.kubernetes.io/component=controller \
  --timeout=90s
```
