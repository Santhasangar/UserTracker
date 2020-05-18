from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

# Create a database  that will store the data about the testUser that will be returned in the response.
class test(models.Model):
    name = models.CharField(max_length=90,null=False,blank=False)
    place_name = models.CharField(max_length=100)

#name and place_name are character strings where we can store strings The __str__ method just tells Django what to print when it needs to print out an instance of the test model.
    def __str__(self):
      return self.name

class user_activity(models.Model):
    test = models.ForeignKey(test, related_name='user_activity', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

#start_time and end_time are character fields where we can store strings. The __str__ method just tells Django what to print when it needs to print out an instance of the user_activity model._
    def __str__(self):
       return str(self.start_time)
