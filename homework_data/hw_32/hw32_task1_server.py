# Task 1

# During the lesson, we have created a server and client, 
# which use TCP/IP protocol for communication via sockets. 
# In this task, you have to create a server and client, which will use 
# user datagram protocol (UDP) for communication.

import socket

HOST = '127.0.0.1'
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Щоб використовувати сокети у програмі, потрібно, по-перше, створити об'єкт сокету. Для клієнта та сервера він створюється однаково
sock.bind((HOST, PORT)) #Серверний сокет прив'язується до адреси (bind)

while True:
    data_bytes, client_addrress = sock.recvfrom(1024) # receive
    data = data_bytes.decode()
    data = data.upper() # Process bytes
    sock.sendto(data.encode(), client_addrress)
