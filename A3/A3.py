import ipaddress
import math

default_mask={'A':'255.0.0.0','B':'255.255.0.0','C':'255.255.255.0'}

	
def find_class(ip, n):
	octet=ip.split('.')
	new_octet=octet
	default=""
	new=""
	net_id=""
	
	if(int(octet[0]) in range(0,128) and n<=24):
		temp=0;
		for i in range(0,n):
			temp+=2**(7-i)
		default=default_mask['A']
		net_id=octet[0]+'.0.0.0'
		new='255.'+str(temp)+'.0.0'
		print(temp)
		
	elif(int(octet[0]) in range (128,192) and n<=16):
		temp=0;
		for i in range (0,n):
			temp+=2**(7-i)
		default=default_mask['B']
		net_id=octet[0]+'.'+octet[1]+'.0.0'
		new='255.255.'+str(temp)+'.0'
		print(temp)
		
	elif(int(octet[0]) in range (192,224) and n<=8):
		temp=0
		for i in range (0,n):
			temp+=2**(7-i)
		default=default_mask['C']
		net_id=octet[0]+'.'+octet[1]+'.'+octet[2]+'.0'
		new='255.255.255.'+str(temp)
		print(temp)
		
	return default,new,net_id		

def print_subnets(subnets,ip):
	ip=ip.split('.')
	for i,subnets_gr in enumerate(subnets):
		print('Subnet no. = {}'.format(i+1))
		print('First address = {}  Last address = {}'.format(subnets_gr[0],subnets_gr[-1]))
		


def classful():
	ip=input('Enter ip address : ')
	no_of_subnets=int(input('Enter number of subnets : '))
	n=int(math.ceil(math.log(no_of_subnets,2)))
	
	default,new,net_id = find_class(ip,n)
	
	print('Network details')
	print('Default : '+default)
	print('Net id : '+net_id)
	print('New subnet mask : '+new)
	
	network=ipaddress.IPv4Network(net_id+'/'+default)
	subnets=network.subnets(n)
	
	print_subnets(subnets,ip)

if __name__ == '__main__':
	classful()


