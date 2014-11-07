# Echo server program
import socket
from sys import exit
import glob
import logging
import logging.handlers
import time
from datetime import datetime

def start():
    LOG_FILENAME = "logs/access.out"

    # Set up a specific logger with our desired output level
    accessLog = logging.getLogger("MyLogger")
    accessLog.setLevel(logging.DEBUG)

    # Add the log message handler to the logger
    handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1048576, backupCount=5)
    accessLog.addHandler(handler)

    #handeling the socket
    HOST = ""                # Symbolic name meaning all available interfaces
    PORT = 8080              # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    c, addr = s.accept()

    #not senting any response if connected
    #c.sendall("connected to server")


    while True:
        c, addr = s.accept()     # Establish connection with client.
        #print 'Got connection from', addr
        inData =  c.recv(1024)

        accessLog.debug("%s Connected by %s",str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) , addr)
        accessLog.debug("%s inData is; %s",str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) , inData)

        if inData == "GetTestData":
            accessLog.debug(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " Returning GetTestData")
            twitterExample = open("Test/twitter.json", "r")
            c.sendall(twitterExample.read()) #returns the example file

        elif inData =="GetRandomTweet":
            with Client.GetRandomTweet() as returnVal:
                c.sendall(returnVal)


        #else:
            #If the message is not recognized noting is returned
            #accessLog.debug(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " Found Error")
            #c.sendall(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " Error")


        c.close()
