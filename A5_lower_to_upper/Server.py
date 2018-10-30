import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 5000)
sock.bind(server_address)
print('Waiting for client...')

message,address=sock.recvfrom(65535)
message = message.decode(encoding='UTF-8').upper()
sock.sendto(bytes(message ,encoding='UTF-8'),address)

fileName , clientAddress = sock.recvfrom(256)
with open(fileName.decode(encoding = 'UTF-8') , 'rb') as file:
    sock.sendto(file.read(65535), clientAddress)

sock.close()
