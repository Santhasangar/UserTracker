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
 Create a model in the database


<input type = text>

    from django.db import models
    from django.db.models.deletion import CASCADE
    class user_activity(models.Models):
        test = models.ForeignKey(test, related_name='user_activity',on_delete=models.CASCADE)
        star_time = models.DateTimeField()
        end_time = models.DatetimeField()
        def __str__(self):
                return str(self.start_time)
                
 
<h3>Make migrations</h3>

<input type = text>

        python manage.py makemigrations
        python manage.py migrate

Register user_activity with admin site

<input type = text>

        from django.contrib import admin
        from . models import  user_activity
        admin.site.register(user_activity)
        
<h3>Run the django server</h3>

python manage.py runserver

<h3>Serialize the user_activity model</h3>
<input type = text>

        from rest_framework import serializers
        from .models import  user_activity, test
        class user_activitySerializers(serializers.ModelSerializer):

                class Meta:
                        model = user_activity
                        fields = ['start_time','end_time']
                        
<h3>Create views to display the data</h3>
<input type = text>

        from rest_framework import viewsets, permissions
        from . import models
        from . import serializers
        class testViewSet(viewsets.ModelViewSet):
                permission_classes = [permissions.IsAuthenticatedOrReadOnly]
                serializer_class = serializers.testSerializers
                queryset = models.test.objects.all()
  <h3>API URLs</h3>
  
  <input type = text>
   
        Include tracker.urls
        <input type = text>
        from django.urls import path, include
        from rest_framework import routers
        from . import views
        router = routers.DefaultRouter()
        router.register(r'api-test', views.testViewSet)
        urlpatterns = [
        path('', include(router.urls)),
        path('api-test/', include('rest_framework.urls', namespace='rest_framework'))
        ]
 <h3>Test it</h3 >
        <input type = text>
        
                python manage.py runserver
                http://127.0.0.1:8000/api-test/
                
 

       







