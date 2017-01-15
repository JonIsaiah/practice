'''
This is a TCP forwarding proxy.
Messages are expected to be of the format destIP:destPORT@forwardedMessage or
firstDestIP:firstDestPORT@nextDestIP:nextDestPORT@...forwardedMessage


TODO
make truly bidirectional with respect to multiple redirects

fix hardcoding of bind port somehow so sender only needs address
of first proxy and destination.

incoming messages should not give away addresses of more proxies than
nessessary 

add end to end encryption of message 
'''

import socket
import threading

bind_ip = "127.0.0.1"
bind_port = 9998

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print "[*] listening on %s:%d\n" %(bind_ip, bind_port)



def handle_client(client_socket):
	
	request = client_socket.recv(1024)
	client_socket.send("ACK!\n")
	
	print "[*] Received %s\n" %request
	
	request = request.split('@', 1)
	destination = request[0].split(':')
	destination_ip = destination[0]
	destination_port = int(destination[1])
	message = request[1]
	
	forwarding_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	forwarding_socket.connect((destination_ip, destination_port))
	forwarding_socket.send(message)
	
	response = forwarding_socket.recv(4096)
	client_socket.send(response)
	
	forwarding_socket.close
	client_socket.close
	

while True:

	client, addr = server.accept()
	
	print "[*] Accepted connection from: %s:%d\n" % (addr[0], addr[1])
	
	client_handler = threading.Thread(target= handle_client, args= (client,))
	client_handler.start()