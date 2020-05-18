#Display the data

from django.shortcuts import render
from rest_framework import viewsets, permissions
from . import models
from . import serializers

#Create your views here.



#Query the database for all test
#Pass the database queryset into the serializer  so that it gets converted into JSON and rendered


class testViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.testSerializers
    queryset = models.test.objects.all()
