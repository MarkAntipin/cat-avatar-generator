# cat-avatar-generator

## Introdution

This Rest API allows you to automatically generate an identification icon by user name.
CatAvatarGenerator can generate 10 million unique cats such as these

![Alt text](https://raw.githubusercontent.com/MarkAntipin/CatAvatarGenerator/master/cat_examples/cat1.jpg)| ![Alt text](https://raw.githubusercontent.com/MarkAntipin/CatAvatarGenerator/master/cat_examples/cat2.jpg)| ![Alt text](https://raw.githubusercontent.com/MarkAntipin/CatAvatarGenerator/master/cat_examples/cat3.jpg)
:-------------------------:|:-------------------------:|:-------------------------|

For one <user_id> you will always get the same identification icon.
Every icon caches in redis

## Run Application

```shell script
docker-compose build
docker-compose up
```

or without docker
```shell script
pip install -r requirements.txt
python3 CatAvatarGenerator/server.py
```

and make request on
```
http://0.0.0.0:5000/<user_id>
```
For one <user_id> you will always get the same identification icon.
Every icon caches in redis
