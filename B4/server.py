import os
import socket
import threading

class Server:
	def create(self):
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.ip='127.0.0.1'
		self.port=25000
		self.sock.bind((self.ip,self.port))
		print('Starting up on {'+str(self.ip)+'} port: {'+str(self.port)+'}')
		self.chatWindow()
		return
	
	def sender(self):
		while True:
			msg=bytes(input(),'utf-8')
			self.sock.sendto(msg,self.addr)
		
	def receiver(self):
		while True:
			msg,self.addr = self.sock.recvfrom(1024)
			print('Message from '+str(self.addr)+':'+str(msg.decode('utf-8')))
	
	def chatWindow(self):
		print('************ Chat Window *****************')
		threadS=threading.Thread(target=self.sender)
		threadR=threading.Thread(target=self.receiver)
		threadS.start()
		threadR.start()
		
if __name__ == '__main__':
	server = Server()
	server.create()
