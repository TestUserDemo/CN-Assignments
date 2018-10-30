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
      choice=client.recv(8).decode(encoding='UTF-8')
      
      if(choice=='0'):
            print ('Client wants to close Connection')
            print ('Bye')
            client.close()
            exit()
      
      num1 = float(client.recv(8).decode(encoding = 'UTF-8'))
      num2 = float(client.recv(8).decode(encoding = 'UTF-8'))
      
      if(choice=='1'):
            client.send(bytes(str(num1 + num2), encoding = 'UTF-8'))
      elif(choice=='2'):
            client.send(bytes(str(num1 - num2), encoding = 'UTF-8'))
      elif(choice=='3'):
            client.send(bytes(str(num1 * num2), encoding = 'UTF-8'))
      elif(choice=='4'):
            client.send(bytes(str(num1 / num2), encoding = 'UTF-8'))
            
            
             
      
