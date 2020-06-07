########################################################################
#   Author: Nolan Y.                                                   #
#   Description: File that contains server functions (aka, the host)   #
########################################################################

import socket                                         

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
   # establish a connection
   clientsocket,addr = serversocket.accept()      

   print("Got a connection from %s" % str(addr))
    
   msg = 'Thank you for connecting'+ "\r\n"
   clientsocket.send(msg.encode('ascii'))
   clientsocket.close()