#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM) #Prepare a sever socket
#Fill in start
serverPort = 5817
bufferSize = 2048
server_address_and_port = (gethostname(), serverPort) #tuple or pair
serverSocket.bind(server_address_and_port)
serverSocket.listen(1) # TCP has listen()
print 'the web server is on port:', serverPort
#Fill in end
while True:
	#Establish the connection
	print 'Ready to serve...'
	connectionSocket, addr = serverSocket.accept() #accept and initialize another socket - 'connection_socket'
	try:
		#Fill in start
		message = connectionSocket.recv(bufferSize)
		print message, '::',message.split()[0],':',message.split()[1]
		filename = message.split[1]
		print filename, '||',filename[1:]
		#Fill in end
		f = open(filename[1:])
		#Fill in start 
		outputdata = f.read()
		#Fill in end 
		#Send one HTTP header line into socket
		#Fill in start
		connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
		connectionSocket.send(outputdata)
		#Fill in end
		#Send the content of the requested file to the client
     	for i in range(0, len(outputdata)):
        	connectionSocket.send(outputdata[i])
     	connectionSocket.close()
	except IOError:
	#Send response message for file not found
	#Fill in start 
	connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
	connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
	#Fill in end
	#Close client socket #Fill in start #Fill in end
serverSocket.close()