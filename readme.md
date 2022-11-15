# TEST DJANGO REST FRAMEWORK & CELERY
* JoinUp Technical Test

---------------

## Installation guide 🔧
* Activar entorno virtual

```
pip3 install --upgrade pip
```
```
pip3 install --no-cache-dir -r requirements.txt
```
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```
```
python3 manage.py runserver
```

* Activar paralelamente en otra terminal el servicio Celery
```
celery -A test_app worker -l info
```
---------------

## Endpoints
* Signup (POST)
```
http://localhost:8000/api/v1/signup
```
* Profiles (GET)
```
http://localhost:8000/api/v1/profile/<id>
```
---------------


## Application built with 🛠️

* [Python 3.7](https://www.python.org/)
* [Django 3.2](https://www.djangoproject.com/)
* [Django RESTFramework 3.14](https://www.django-rest-framework.org/)
* [Celery 4.3.0](https://docs.celeryq.dev/en/stable/)
* [RabbitMQ](https://www.rabbitmq.com/)
* [Docker 20.10](https://www.docker.com/)
* [Bulma](https://bulma.io/)

---------------
## Developer ⌨️

* **Jesús Villegas** | [e-mail](jvncode@gmail.com)  |  [LinkedIn](https://www.linkedin.com/in/jes%C3%BAs-villegas-609b71198)


