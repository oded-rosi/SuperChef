import socket
import sys



def HandleNewCon( connection ,s):
   #"This prints a passed string into this function"
    # starts with sendind
    s.send("Hello Back")
    return;



#for tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind(("localhost", 50000))
s.listen(1)

while True:

    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = s.accept()
    #someData = s.recv(1024)
    #data=connection.recv(100000)  # Read from newly accepted socket
    HandleNewCon(connection,s)
    connection.close()

    #print >>sys.stderr, data

s.close()

