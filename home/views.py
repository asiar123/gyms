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
        print(gps)

        if(gps): #Consulta no vacia
            print('usernombre')

    return HttpResponse(gps)
    
