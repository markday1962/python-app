# python-app
Simple python app

### Generate PAT
```
login to github
Settings -> Developer Settings -> Personal access tokens (classic) -> Generate new token
```
* New PAT details
```
Expiration: Custom # enter date 1 year away
Select Scopes: repo
Generate Token
```
* Add pat token to .git/config
```
[remote "origin"]
	url = https://markday1962:<add-pat-token-here>markday1962/python-app.git
	fetch = +refs/heads/*:refs/remotes/origin/*
```


### Github Actions
https://github.com/docker/build-push-action

* Create a Docker hub access token
https://docs.docker.com/security/for-developers/access-tokens/
Account settings -> Personnel Access Tokens -> Generate new token

* Add Actions secrets and variables
Repo -> Settings -> Secrets and Variables -> Repository secrets -> New repository secret
