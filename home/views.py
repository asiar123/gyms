from django.http import JsonResponse
import socket
from ast import literal_eval
from django.contrib.auth import authenticate
import socket
from ast import literal_eval
import socket 

# Create your views here.

def datosJson(request):
    
    host , port = '192.168.1.6' , 56458

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
    serversocket.bind((host , port))
    serversocket.listen(1)
    print('servidor en el puerto',port)

    while True:
        connection , address = serversocket.accept()
        request = connection.recv(1024).decode('utf-8')
        string_list = request.split(' ')
        method = string_list[0]
        requesting_file = string_list[1]

        print('Client requestttttt',string_list)
    
