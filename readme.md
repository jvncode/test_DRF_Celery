## Test Django Rest Framework & Celery

---------------

## Installation guide 🔧

- Activar de entorno virtual
```
source <entorno_virtual>/bin/activate
```
- Instalar dependencias

```
pip3 install --upgrade pip
```
```
pip3 install --no-cache-dir -r requirements.txt
```
- Configuración de migraciones
```
python3 manage.py migrate
```
- Crear usuario administrador
```
python3 manage.py createsuperuser
```
- Iniciar aplicación
```
python3 manage.py runserver
```
- Paralelamente en otra terminal, activar servicio Celery
```
celery -A test_app worker -l info
```
---------------
## Admin
- Acceso al administrador para autenticación y gestión de usuarios
```
http://localhost:8000/admin
```

## Endpoints
* Signup (POST) - Creación de nuevos usuarios
```
http://localhost:8000/api/v1/signup
```
* Profile (GET) - Verificación de usuario autenticado
```
http://localhost:8000/api/v1/profile
```
---------------

## cURL
* Signup (POST)
```
curl -H "Content-Type: application/json" -X POST -d '{"name":"Helena","surnames":"Queiros","email":"helen_q@gmail.com","phone":"682902308","hobbies":"viajar"}' http://localhost:8000/api/v1/signup
```
* Profile (GET)
```
curl --location --request GET 'http://127.0.0.1:8000/api/v1/profile'
```
---------------

## Application built with 🛠️

* [Python 3.7](https://www.python.org/)
* [Django 3.2](https://www.djangoproject.com/)
* [Django RESTFramework 3.14](https://www.django-rest-framework.org/)
* [Celery 4.3.0](https://docs.celeryq.dev/en/stable/)
* [RabbitMQ](https://www.rabbitmq.com/)
* [Docker 20.10](https://www.docker.com/)
* [Bulma CSS](https://bulma.io/)

---------------
## Developer ⌨️

* **Jesús Villegas** | [email](jvncode@gmail.com)  |  [LinkedIn](https://www.linkedin.com/in/jes%C3%BAs-villegas-609b71198)


