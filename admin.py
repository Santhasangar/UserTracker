from django.contrib import admin
from . models import test, user_activity

# Register your models here.

#add our models to the admin

admin.site.register(test)

admin.site.register(user_activity)
