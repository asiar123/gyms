from django.http import JsonResponse
import socket
from ast import literal_eval
from django.contrib.auth import authenticate
import socket
from ast import literal_eval
import socket 

# Create your views here.

def datosJson(request):
    dat={
        "usr":"",
    }

    if (request.method=='GET'):
        gps=request.GET.get('userN')
        print('usernombre')

        if((usernombre is not None)): #Consulta no vacia
            dat={    #Arreglo que contiene los datos de la bd

            }

    return HttpResponse(user)
    
