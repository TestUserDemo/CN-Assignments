import socket
import math

server_ipaddr = '127.0.0.1'
server_port=5000
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((server_ipaddr,server_port))

print ('Server ready at 127.0.0.1')
server.listen(1)

client, address = server.accept()
print('\nGot connection from: {}'.format(address))
while True:
      choice=client.recv(1024).decode(encoding='UTF-8')
      if(choice=='0'):
            print ('Client wants to close Connection')
            print ('Bye')
            server.close()
            exit()
      elif(choice=='1'):
            angle=int(client.recv(1024).decode(encoding='UTF-8'))
            angle=math.radians(angle)
            result=math.sin(angle)
            client.send(bytes(str(result),encoding='UTF-8'))
      elif(choice=='2'):
            angle=int(client.recv(1024).decode(encoding='UTF-8'))
            angle=math.radians(angle)
            result=math.cos(angle)
            client.send(bytes(str(result),encoding='UTF-8'))
      elif(choice=='3'):
            angle=int(client.recv(1024).decode(encoding='UTF-8'))
            angle=math.radians(angle)
            result=math.tan(angle)
            client.send(bytes(str(result),encoding='UTF-8'))
            
            
             
      
