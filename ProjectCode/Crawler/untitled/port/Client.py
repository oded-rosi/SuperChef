import os
import socket
import sys


#create an INET, STREAMing socket
s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
#now connect to the web server on port 80
# - the normal http port
s.connect((socket.gethostname(), 8000))

message = "test"

s.sendall(message)
oded = s.recv(2014)
print >>sys.stderr, oded
