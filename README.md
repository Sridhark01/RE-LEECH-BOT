# RE-LEECH-BOT


---
-  Clone this repo:
```
git clone https://github.com/Sridhark01/RE-LEECH-BOT RE-LEECH-BOT/ && cd RE-LEECH-BOT
```
 
- Switch to deploy branch:
```
git checkout main
```

- Login to heroku:
```
heroku login
```

- Create heroku app:
```
heroku create --region us YOUR-APP-NAME
```

- Add remote: ```heroku git:remote -a YOUR-APP-NAME```

- Create container: ```heroku stack:set container```

- Push to heroku: ```git push heroku main:master -f```
