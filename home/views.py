from django.http import JsonResponse
import socket
from ast import literal_eval
from django.contrib.auth import authenticate

# Create your views here.

def datosJson(request):
    dat={
        "usr":"",
        "pass":"",
    }
    
    if (request.method=='GET'):
        usernombre=request.GET.get('userN')
        user=authenticate(request, username=usernombre)
        print(user)
        
        if((user is not None)): #Consulta no vacia
            dat={    #Arreglo que contiene los datos de la bd
                "usr":user.username,
                "nombre":user.first_name,
                "email":user.email,
                "Msn":"Bienvenido"
            }

        else:
            dat={"msn":"Usuario o contraseña no encontrada"}

        #dat={"msn": usernombre}

    return JsonResponse(dat)