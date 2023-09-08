from django.http import JsonResponse
import socket
from ast import literal_eval
from django.contrib.auth import authenticate
import socket
import time

# Create your views here.

def datosJson(request):
    
    HOST = ''
    PORT = 2102
    BUFSIZ = 1024
    ADDR = (HOST,PORT)

    sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind( ADDR)

    print('waiting for data on', ADDR)
    while True:
        data,addr = sock.recvfrom(BUFSIZ)
        print('Recv from %s at %s' % (str(addr),time.ctime(time.time())))
        print(data)

        sock.close()