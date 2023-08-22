from django.conf.urls import url
from home.views import datosJson

urlpatterns = [
    url(r'^new', datosJson , name='datosJson'),
]