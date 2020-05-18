


from django.urls import path, include
from rest_framework import routers
from . import views

#Routers provide a way of determining the URL configuring
router = routers.DefaultRouter()
router.register(r'api-test', views.testViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-test/', include('rest_framework.urls', namespace='rest_framework'))
]
