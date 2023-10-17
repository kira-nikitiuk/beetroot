# Task 2
# Extend the echo server, which returns to client the data, encrypted using 
# the Caesar cipher algorithm by a specific key obtained from the client.

import socket

HOST = "localhost"
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# |||  UDP  |||
while True:
    data = input("Enter a message to send: ")
    data_bytes = data.encode()
    sock.sendto(data_bytes, (HOST, PORT)) 

    encrypted_data_bytes, server_address = sock.recvfrom(1024)  
    decrypted_data = encrypted_data_bytes.decode()
    print("Received:", decrypted_data)
