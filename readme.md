# Django Rest Framework API

## Running the project

### 1. Cloning the project
```
git clone https://github.com/jeelpatel231/django-rest-api-proto
```
> its implicit that you will cd into the dir


### 2. Installing pre-requisites
```
pip3 install -r requirements.txt
```

### 3. Making Migrations
```
python manage.py migrate
```

### 4. Running the server
```
python manage.py runserver
```
_______

### Creating new migrations
Make your preffered models in models/classmodels.py
with respected serializers in models/serializers.py
and viewsets in models/viewsets.py.

Run the following command to generate migrations
```
python manage.py makemigrations
python manage.py migrate
```