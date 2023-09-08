from django.http import JsonResponse
import socket
from ast import literal_eval

# Create your views here.

def datosJson(request):
    dat={
        "usr":"",
    }
    
    if (request.method):
        usernombre=request.GET

        print("Parametro enviado: ", usernombre)