<h1>Django and React Project</h1>
<h2>Installation</h2>

```bash
install python3 and pip
install nodejs and npm
install django and django rest framework with pip
```
<h3>start a django project</h3>

```bash
django-admin startproject <project_name>
```

<h3>start a django app</h3>
For this project we will need two apps, one for the frontend and one for the backend

CD into the django project folder, run the following command:

```bash
django-admin startapp <app_name>
```
The above command is the equivalent of the following:

```bash
python manage.py startapp <app_name>
```

<h2>Inside the django parent project folder</h2>

Our initial app will be an api app, so we will name it api
```bash
django-admin startapp api
```

Don't forget to add it to the installed apps in the settings.py file together with the rest framework

```python
INSTALLED_APPS = [
    'api.apps.ApiConfig',
    'rest_framework',
]
```

<h1>api app</h1>
<h2>DJANGO REST FRAMEWORK</h2>
<h2>Creating REST API Endpoints and Models</h2>

<p>When it comes to django models, the rule is:</p>
<u>Write Fat Models and Thin Views</u>
This means that you should have most of logic within the models not the views.

<h1>REST API ENDPOINT</h1>
With our app, we want the frontend to query our backend and not receive a html like response but instead a json response.With this kind of response, we can easily manipulate the data and display it on the frontend as well as allow the frontend to make decisions based on the data received. This is where the django rest framework comes in.

<h3>STEP 1</h3>
Create a serializers.py file inside the api app folder

A serializer is a way of converting complex data such as querysets and model instances to native python datatypes that can then be easily rendered into json, xml or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

Another explanation is:
Serializers takes our models that has all the python code and translate it to json response.

```python
from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')
```

model: the model that we want to serialize
fields: the fields in that model that we want to serialize, in our case we want all of them incuding the automated id field.

<h3>STEP 2</h3>
Head over to the views.py file and create a api view that will let us view a list of all different rooms in our database.

```python
from rest_framework import generics

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all() #what we want to return
    serializer_class = RoomSerializer #converting them to a format that can be displayed on the frontend
```
This is a view that is already set up to return to us all teh different rooms in our database.

This will not only allow us to view the rooms but create them as well.
Then link it to our urls.py file

```python
from django.urls import path
from .views import RoomView

urlpatterns = [
    path('api', RoomView.as_view()),
]
```
To test it, we run the url to get a get a display of our api output and also a form to create a new room below.

With the <u>CreateAPIView</u> we are getting a "method error with GET" because we are not allowed to use the GET method with this view. We can only use the POST method to create a new room.

To allow the GET method, we use the <u>ListAPIView</u> instead of the <u>CreateAPIView</u>

```python
from rest_framework import generics

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all() #what we want to return
    serializer_class = RoomSerializer #converting them to a format that can be displayed on the frontend
```


<h1>REACT</h1>
We will be adding a React app as our frontend to the django backend.

<h2>STEP 1</h2>
Create a frontend app inside the django project folder

```bash
django-admin startapp frontend
```

This app will store every aspect of our frontend code, that means it will store everything to do with react.

<h2>STEP 2</h2>
cd to the frontend app
create the necessary folders and then run the following commands:

```bash
npm init -y
npm i webpack webpack-cli --save-dev
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
npm i react react-dom --save-dev
npm install @mui/material
npm install @babel/plugin-proposal-class-properties
npm install react-router-dom
npm install @mui/icons-material
```
NB - while installing the above dependancies, ensure react version installed is compatible with the material ui since material ui is dependent on react. When installing i had to force material ui.
dependancies i forced include te react router-dom and material ui.

<u>proposed solution to the above problem</u>
```bash
replace material-ui/core with @mui/material
replace material-ui/icons with @mui/icons-material
```

<h2>STEP 3</h2>
Integrating React with Django

When django renders a template, react should be able to render the template as well.
Django will render the template but react will manage it.
