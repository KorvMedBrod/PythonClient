# Echo server program
import socket
from sys import exit
#global variables
delayTime = 1 #the delay between the packages for making the car move
#handeling the socket
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8080              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
c, addr = s.accept()
c.sendall('connected to server')
print "Connected by", addr

while True:
   c, addr = s.accept()     # Establish connection with client.
   #print 'Got connection from', addr
   inData =  c.recv(1024)
   print("inData is; ",inData)

   c.close()                # Close the connection
