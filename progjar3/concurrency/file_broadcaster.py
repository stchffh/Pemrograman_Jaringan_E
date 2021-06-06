import socket

CHUNK_SIZE = 1024

def broadcast_config():
    return [{'ip_address':'192.168.122.91'},
    {'ip_address':'192.168.122.66'},
    {'ip_address':'192.168.122.103'}]

def broadcast_file(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    filename = "data.txt"
    file = open(filename, "r")
    while True:
        chunk = file.read(CHUNK_SIZE)
        if not chunk:
            break
        sock.sendto(chunk.encode(), (ip, port))
    
if __name__ == '__main__' :
    configs = broadcast_config()
    for config in configs:
        print(f"broadcasting file data.txt to {config['ip_address']}")
