# Task 1

# During the lesson, we have created a server and client, 
# which use TCP/IP protocol for communication via sockets. 
# In this task, you have to create a server and client, which will use 
# user datagram protocol (UDP) for communication.

import socket

HOST = "localhost"
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# |||  UDP  |||
while True:
    data = input("message tosend: ")
    data_bytes = data.encode() # str to bytes
    sock.sendto(data_bytes, (HOST, PORT)) # send
    data_bytes, server_address = sock.recvfrom(1024)# receive
    data = data_bytes.decode()
    print("received: ", data)


# |||  TCP  |||
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#     sock.connect((HOST, PORT))
#     while True:
#         data = input("Type the message to send:")
#         data_bytes = data.encode()  # str to bytes
#         sock.sendall(data_bytes)
#         data_bytes = sock.recv(1024)
#         data = data_bytes.decode()  # bytes to str
#         print("Received:", data)
