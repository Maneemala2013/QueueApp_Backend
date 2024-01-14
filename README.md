# QueueApp_Backend

This is the backend of a QueueApp.

### Installation

pip3 install Django
pip3 install djangorestframework
pip3 install django-cors-headers

### Run a server

Go to the root directory
python3 manage.py runserver

### migrate, which is responsible for applying and unapplying migrations.

python3 manage.py migrate

### makemigrations, which is responsible for creating new migrations based on the changes you have made to your models.

python3 manage.py makemigrations

### create a superuser

python3 manage.py createsuperuser

Then, you can run a server with the following command via Terminal
python manage.py runserver

### Authentication // To be implemented later

#### Source

**Getting started with React Native & Django authentication - Part 1**
https://afdezl.github.io/post/authentication-react-native-django-1/

**Getting started with React Native & Django authentication - Part 2**
https://afdezl.github.io/post/authentication-react-native-django-2/

#### First, create a python virtual environment

pip install virtualenv virtualenvwrapper
mkvirtualenv django-rn-auth

#### Create username and password

python3 manage.py createsuperuser

#### How to test a system and get the token?

curl -X POST -d "username=<USERNAME>&password=<PASSWORD>" http://<IP_ADDRESS>:80/auth/login/  
Note that your username and password can be created from python mangae.py createsuperuser.
Example: curl -X POST -d "username=kaimook3&password=Blue1234" http://<IP_ADDRESS>:80/auth/login/
