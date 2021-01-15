# WEATHER APP

Weather app is a project library for taking a 3 and 5 days weather forecast for Turkey from www.worldweatheronline.com api and represent them.

Combination of PostgreSQL and Django including Django Templates.
## Installation

Please make sure that you have installed packages in requirements.txt, [PostgreSQL](https://www.postgresqltutorial.com/install-postgresql/). You can check how to install them by clicking on them.

1- Configure DB as follows or do not forget to change settings.py in weather/ as requested:

For use:
```json
HOST: "localhost",
USER: "sinantalhakosar",
PASSWORD: "kosar",
DB: "weather",
```

### DB Setup for Docker
1- Create docker-compose.yml[(see configure docker-compose section)](https://medium.com/analytics-vidhya/getting-started-with-postgresql-using-docker-compose-34d6b808c47c) having credentials above and run followings:
```bash
$ docker run -d -p 5432:5432 --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword postgres
$ docker exec -it my-postgres bash
$ psql -U postgres
$ CREATE USER sinantalhakosar SUPERUSER;
$ ALTER USER user_name WITH PASSWORD 'kosar';
$ CREATE DATABASE weather;
```
after that PostgreSQL container is ready to connect with localhost and port 5432

## Additonal Notes

In weatherapp/views.py file there is a key value which is provided by 
```
www.worldweatheronline.com
```
 api, for use in production
``` 
please put key in .env file
make necessary changes in settings.py(commented section at the end of the file)
remove key='your_key' in weatherapp/views.py and uncomment the other key variable.
```

## Owner
[Sinan Talha Kosar](https://sinantalhakosar.github.io)

## License
[MIT](https://choosealicense.com/licenses/mit/)