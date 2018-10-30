import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 5000)

sock.sendto(bytes(input('Enter a message : '),encoding='UTF-8'),server_address)
print('Received message',sock.recv(65535).decode(encoding='UTF-8'))

fileName = input('Enter Name of File to Receive : ')
sock.sendto(bytes(fileName, encoding = 'UTF-8'), server_address)
with open(fileName , 'wb') as file:
	data , serveraddr = sock.recvfrom(65535)
	file.write(data)
	
sock.close()
