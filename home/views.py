from django.http import HttpResponse

# Create your views here.

def datosJson(request):
    
    if (request.method):
        gps=request.method
        print(gps)

        if(gps): #Consulta no vacia
            print(gps)

    return HttpResponse(gps)
    
