# Task 3 server
# Echo server with threading
# Create a socket echo server that handles each connection using the multiprocessing library.

import socket
import multiprocessing

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            client_socket.send(data)
    finally:
        client_socket.close()

def main():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    print(f"Listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from: {addr[0]}:{addr[1]}")
        
        client_process = multiprocessing.Process(target=handle_client, args=(client_socket,))
        client_process.start()

if __name__ == "__main__":
    main()

