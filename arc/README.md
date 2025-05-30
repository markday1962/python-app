### Github Actions
https://github.com/docker/build-push-action

* Create a Docker hub access token
https://docs.docker.com/security/for-developers/access-tokens/
Account settings -> Personnel Access Tokens -> Generate new token

* Add Actions secrets and variables
Repo -> Settings -> Secrets and Variables -> Repository secrets -> New repository secret

### Github runners
https://github.com/actions/actions-runner-controller
* Install cert manager prerequisite
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.8.2/cert-manager.yaml


#### Install Github Actions Runner Controller (ARC)

* Helm
Add repo
```
helm repo add actions-runner-controller https://actions-runner-controller.github.io/actions-runner-controller
```
Apply Chart
```
helm upgrade --install --namespace actions-runner-system --create-namespace\
  --set=authSecret.create=true\
  --set=authSecret.github_token="<ADD-PAT-TOKEN>"\
  --wait actions-runner-controller actions-runner-controller/actions-runner-controller
```

* Configure PAT
kubectl create secret generic controller-manager \
    -n actions-runner-system \
    --from-literal=github_token=<ADD-PAT-TOKEN>

* Install runnerdeployment

```
kubectl -n actions-runner-system apply -f runnerdeployment.yaml
kubectl get runnerdeployment --all-namespaces
```
