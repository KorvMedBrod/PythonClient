# Echo server program
import socket
from sys import exit
import glob
import logging
import logging.handlers
import time
from datetime import datetime

def start():
    LOG_FILENAME = 'logs/access.out'

    # Set up a specific logger with our desired output level
    accessLog = logging.getLogger('MyLogger')
    accessLog.setLevel(logging.DEBUG)

    # Add the log message handler to the logger
    handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1048576, backupCount=5)
    accessLog.addHandler(handler)

    #handeling the socket
    HOST = ''                # Symbolic name meaning all available interfaces
    PORT = 8080              # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    c, addr = s.accept()

    c.sendall('connected to server')


    while True:
        c, addr = s.accept()     # Establish connection with client.
        #print 'Got connection from', addr
        inData =  c.recv(1024)

        accessLog.debug("Connected by %s", addr)
        accessLog.debug("inData is; %s",inData)

        if inData == "GetTestData":
            accessLog.debug("Returning GetTestData")
            twitterExample = open("Test/twitter.json", "r")
            returnValue  = str(twitterExample.read()) + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            c.sendall(returnValue) #returns the example file

        else:
            accessLog.debug("Found Error")
            returnValue ="Error " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            c.sendall(returnValue)


        c.close()
