import socket;


def clientthread(clientsocket):
    try:
        s = clientsocket
        #//s.connect((host, port))
        return s
    except:
        s.close()
        return None

__author__ = 'oded'
#create an INET, STREAMing socket
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
serversocket.bind((socket.gethostname(), 82))
#become a server socket
serversocket.listen(500000)


while 1:
    #accept connections from outside
    (clientsocket, address) = serversocket.accept()
    #now do something with the clientsocket
    #in this case, we'll pretend this is a threaded server
    ct = client_thread(clientsocket)
    ct.run()
