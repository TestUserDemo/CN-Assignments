import os
import socket
import threading

class Client:
	def create(self):
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.ip='127.0.0.1'
		self.port=25000
		print('Socket binded successfully')
		self.chatWindow()
		
	
	def sender(self):
		while True:
			msg=bytes(input(),'utf-8')
			self.sock.sendto(msg,(self.ip,self.port))
		
	def receiver(self):
		while True:
			msg,addr = self.sock.recvfrom(1024)
			print('Message from '+str(addr)+':'+str(msg.decode('utf-8')))
	
	def chatWindow(self):
		print('************ Chat Window *****************')
		threadS=threading.Thread(target=self.sender)
		threadR=threading.Thread(target=self.receiver)
		threadS.start()
		threadR.start()
		
if __name__ == '__main__':
	client = Client()
	client.create()
