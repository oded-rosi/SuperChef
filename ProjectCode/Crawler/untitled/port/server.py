import os
import socket
import sys
import subprocess


def client_thread(clientsocket):
    oded = clientsocket.recv(1024)
    print >>sys.stderr, oded
    clientsocket.sendall("SOMETHING")


#create an INET, STREAMing socket
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
serversocket.bind((socket.gethostname(), 8000))
#become a server socket
serversocket.listen(5)
while 1:
    #accept connections from outside
    (clientsocket, address) = serversocket.accept()
    #now do something with the clientsocket
    #in this case, we'll pretend this is a threaded server
    client_thread(clientsocket)






