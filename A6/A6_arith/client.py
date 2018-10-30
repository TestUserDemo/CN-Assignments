
import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_ipaddr = '127.0.0.1'
server_port=5000
client.connect((server_ipaddr,server_port))
print ('Connected to server')
while True:
      choice=input('\nMENU:\nPress 1.for Add\nPress 2.for Subtract\n Press 3.for multiply\nPress 4.for divide \nPress 0 to Exit\n')
      choice1=bytes(choice, encoding='UTF-8')
      client.send(choice1)
      
      if(choice=='0'):
            print ('Exiting ....')
            client.close()
            exit()
      
      client.send(bytes(input('Enter 1st Number : ') , encoding = 'UTF-8'))
      client.send(bytes(input('Enter 2nd Number : ') , encoding = 'UTF-8'))
      print('Answer : ' , client.recv(8).decode(encoding = 'UTF-8'))
      
   
