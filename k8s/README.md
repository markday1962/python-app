## Kubernetes README

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

### Deploy and expose python-app
* Deployment
https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
```
kubectl apply -f deployment.yaml
```
* Service
https://kubernetes.io/docs/concepts/services-networking/service/
```
kubectl apply -f service.yaml
```
* Ingress
https://kubernetes.io/docs/concepts/services-networking/ingress/
```
kubectl get ingressclass
kubectl apply -f ingress.yaml
kubectl get ingress
curl -s http://localhost/api/v1/details | jq
```
