import sys
import socket
import string
import random

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)

def megabyte_to_byte(arg):
    return arg * 1024 * 1024

try:
    # Send data
    message_length = megabyte_to_byte(2)
    message = ""
    for i in range(0, message_length):
        message += random.choice(string.ascii_letters)
    
    encoded_message = message.encode()

    print(f"sending {len(encoded_message)} bytes with last 16 character {message[-16:]}")
    sock.sendall(encoded_message)
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
    print(f"message received. Last 16 byte is {data.decode()}")
finally:
    print("closing")
    sock.close()