
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_ipaddr = '127.0.0.1'
server_port=5000
client.connect((server_ipaddr,server_port))
print ('Connected to server')
while True:
      choice=input('\nMENU:\nPress 1.for Sine\nPress 2.for Cosine\n Press 3.for Tangent\nPress 0 to Exit\n')
      choice1=bytes(choice, encoding='UTF-8')
      client.send(choice1)
      if(choice=='0'):
            print ('Exiting ....')
            client.close()
            exit()
      angle=bytes(input('Enter the angle in Degrees\n'),encoding='UTF-8')
      client.send(angle)
      res=client.recv(1024).decode(encoding='UTF-8')
      print('\n>Result: {}'.format(res))
      
      
