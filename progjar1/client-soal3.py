import sys
import socket
import base64

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)

image_name = input("Input File name : ")
file = open(image_name, 'rb')

try:
    # Send data
    message = base64.b64encode(file.read())
    print(f"sending {image_name}, transmit size : {len(message)} bytes ...")
    sock.sendall(message)
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    output_file = open("output.jpg", 'wb')
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        output_file.write(base64.b64decode(data))
finally:
    print("closing")
    file.close()
    output_file.close()
    sock.close()