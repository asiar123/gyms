from django.urls.conf import path
from home.views import datosJson

urlpatterns = [
    path('datosJson/', datosJson, name="datosJson")
]