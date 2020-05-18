# UserTracker
UserTracker is a django app  which has to be created in rest_framework api and allows to tracks the userinformation.

<h1>Steps to Create a Django App in Window</h1>

<h3>Setup virtual environment</h3>

pip install virtualenvwrapper-win

<h3>create virtual environment</h3>

pip install mkvirtualenv

<h3>install Django</h3>

pip install django

<h3>Create Project<h3>
        
django-admin startproject 

<h3>Install django restframework</h3>
pip install djangorestframework

<h3>Run Server</h3>

Python manage.py runserver

Add django rest_framework and application name in settings.py under INSTALLED_APPS

 <input type = text>
       
       INSTALLED_APPS = [
        .......
        'rest_framework',
        'app_name'
        .....
        
        ]
 Create a model

<input type = text>

from django.db import models
from django.db.models.deletion import CASCADE

class test(models.Model):
    name = models.CharField(max_length=90,null=False,blank=False)
    place_name = models.CharField(max_length=100)
    
 def __str__(self):
      return self.name




