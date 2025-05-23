## README

https://argo-cd.readthedocs.io/en/stable/operator-manual/installation/
https://github.com/argoproj/argo-helm/tree/main/charts/argo-cd

### Add argocd repo
```
helm repo add argo https://argoproj.github.io/argo-helm
helm repo ls
```

### Install argocd after updating values file
```
helm upgrade --install argocd argo/argo-cd -n argocd --create-namespace -f values.yaml
```
Response
```
In order to access the server UI you have the following options:

1. kubectl port-forward service/argocd-server -n argocd 8080:443

    and then open the browser on http://localhost:8080 and accept the certificate

2. enable ingress in the values file `server.ingress.enabled` and either
      - Add the annotation for ssl passthrough: https://argo-cd.readthedocs.io/en/stable/operator-manual/ingress/#option-1-ssl-passthrough
      - Set the `configs.params."server.insecure"` in the values file and terminate SSL at your ingress: https://argo-cd.readthedocs.io/en/stable/operator-manual/ingress/#option-2-multiple-ingress-objects-and-hosts

kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```
### Check Ingress
```
kubectl get ing -n argocd
```
