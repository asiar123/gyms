from django.http import JsonResponse
import socket
from ast import literal_eval
from django.contrib.auth import authenticate
import socket
from ast import literal_eval

# Create your views here.

def datosJson(request):
    
    localIP     = "192.168.1.8"

    localPort   = 10000

    bufferSize  = 1024

 

    msgFromServer       = "1"

    bytesToSend         = str.encode(msgFromServer)

 

    # Create a datagram socket

    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

    # Bind to address and ip

    UDPServerSocket.bind((localIP, localPort))

 

    print("UDP server up and listening")

 

    # Listen for incoming datagrams

    while(True):

        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        message = bytesAddressPair[0]

        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)
    
    #messajes= Encoding.ASCII.GetString(message)
    
        print(message)
        print(clientMsg)
        print(clientIP)
        print(address)
   

    # Sending a reply to client

        UDPServerSocket.sendto(bytesToSend, address)
    