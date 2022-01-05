# a simple script to connect to google using socket
# programming in python
import socket # for socket 
import sys


# try:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     print('Socket successfully connected')
# except socket.error as err:
#     print(f'socket creation failed with error {err}')


# # default port for socket
# port = 80

# try:
#     host_ip = socket.gethostbyname('www.skycrew.tech')
# except socket.gaierror:

#     # this means could not resolve the host 
#     print('there was an error resolving the host')
#     sys.exit()

# # connecting to the Server
# s.connect((host_ip, port))

# print('the socket has successfully connected to skycrew technologies')


# A simple server-client program
# create a socket object 
s = socket.socket()
print('Socket successfully created')

# reserve a port on your computer in our
# case it is 12345 baut it can be anything
port = 12345

# next bind to the port
# we have not typed any ip in the field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print(f'socket binded to {port}')

# put the socket into listening mode
s.listen(5)
print('socket is listening')

# a forever loop until we interrupt it or
# an error occurs
while True:
    # established connection with client.
    c, addr = s.accept()
    print(f'got connection from {addr}')

    # send a thank you message to the client. encoding to send byte type.
    c.send('Thank you for connecting'.encode())

    # clode the connection with the client
    c.close()

    # breaking once connection closed
    break

