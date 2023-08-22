from django.conf.urls import url
from django.urls import path
from home.views import datosJson

urlpatterns = [
    path('/datosJson/', datosJson, name="index")
]