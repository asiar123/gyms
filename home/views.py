from django.http import JsonResponse


# Create your views here.

def datosJson(request):
    dat={
        "usr":"",
    }
    
    if (request.method=='GET'):
        usernombre=request.GET.get('userN')
        print("Hola")
        print(usernombre)
        
        if((usernombre is not None)): #Consulta no vacia
            print(usernombre)

        else:
            dat={"msn":"Usuario o contraseña no encontrada"}

        #dat={"msn": usernombre}

    return JsonResponse(dat)