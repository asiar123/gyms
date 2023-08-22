from django.conf.urls import url
from django.urls import path
from home.views import datosJson

urlpatterns = [
    url(r'^new', datosJson , name='datosJson'),
    path('datosJson/', datosJson, name="index")
]