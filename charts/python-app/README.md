## README

### Install Chart
```
helm upgrade python-app -n apps --create-namespace .
helm upgrade python-app -n apps .
```
### Test Ingress
```
curl -s http://python-app.test.com/api/v1/details | jq
```

### Delete Chart
```
helm uninstall python-app -n apps
```
