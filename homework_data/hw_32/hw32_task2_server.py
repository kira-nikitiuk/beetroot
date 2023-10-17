#Task 2
# Extend the echo server, which returns to client the data, encrypted using 
# the Caesar cipher algorithm by a specific key obtained from the client.

import socket

def caesar_cipher(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('a') + 3) % 26) + ord('a'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

HOST = '127.0.0.1'
PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

while True:
    data_bytes, client_address = sock.recvfrom(1024) 
    data = data_bytes.decode()
    encrypted_data = caesar_cipher(data)  # Encrypt "cat" to "fdw"
    sock.sendto(encrypted_data.encode(), client_address)
