#Import the user_activity and testUser models.
#Import the rest_framework serializer

from rest_framework import serializers
from .models import  user_activity, test

#Create a Serializer class which enables  queryset and model instances to be converted into datatypes and rendered into JSON

#Serializers define the API representation
class user_activitySerializers(serializers.ModelSerializer):

    class Meta:
        model = user_activity
        fields = ['start_time','end_time']

class testSerializers(serializers.ModelSerializer):
    user_activity = user_activitySerializers(many=True)

    class Meta:
        model = test
        fields = ['id','name','place_name','user_activity']

#With the help of overriding create method we are populating the data in tables.
    def create(self, valid_data):
        user_activity_data = valid_data.pop('user_activity')
        name = test.objects.create(**valid_data)
        for user_activity_data in user_activity_data:
            user_activity.objects.create(testUser=name, **user_activity_data)
        return name

