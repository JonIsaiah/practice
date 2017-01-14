import socket
import urllib


#raw sockets

target_host = "127.0.0.1"
target_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	target_ip = socket.gethostbyname(target_host)
	print("\n" + target_ip + "\n")
except:
	print("could not resolve ip")
	


client.connect((target_ip, target_port))
client.send("it works!")
response = client.recv(4069)
print response


#    using library for web requests 
'''   

response = urllib.urlopen("http://google.com")
print 'RESPONSE:', response
print 'URL     :', response.geturl()


headers = response.info()
print 'DATE    :', headers['date']

print "\n\n"
print 'HEADERS :'
print '---------'
print headers
print "\n\n"

data = response.read()
print 'LENGTH  :', len(data)
print 'DATA    :'
print '---------'
print data

'''