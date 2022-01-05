# import socket module
import socket


# create a socket object 
s = socket.socket()

# define the port on whick to connect 
port = 12345

# connect to the server on local computer 
s.connect(('127.0.0.1', port))

# receieve data from the server and decoding to get the string 
print(s.recv(1024).decode())

# close the connection
s.close() 
