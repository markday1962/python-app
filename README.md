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
