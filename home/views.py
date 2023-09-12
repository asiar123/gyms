from django.http import HttpResponse

# Create your views here.

def datosJson(request):
    dat={
        "usr":"",
    }

    if (request.method):
        gps=request.GET.get('userN')
        print(gps)

        if(gps): #Consulta no vacia
            print('usernombre')

    return HttpResponse(gps)
    
