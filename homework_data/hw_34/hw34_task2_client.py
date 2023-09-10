# Task 2 client
# Echo server with threading
# Create a socket echo server which handles each connection in a separate Thread

import socket

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    message = "Hello, server!"
    client_socket.send(message.encode())

    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode()}")

    client_socket.close()

if __name__ == "__main__":
    main()
