########################################################################
#   Author: Nolan Y.                                                   #
#   Description: File that contains server functions (aka, the host)   #
########################################################################

import socket                                         

def run_server():
   # create a socket object
   serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 

   # get local machine name
   host = socket.gethostname()                           

   port = 9998                                           

   # bind to the port
   serversocket.bind((host, port))                                  

   # queue up to 5 requests
   serversocket.listen(5)                                           

   setup = True

   while setup:
      # establish a connection
      clientsocket,addr = serversocket.accept()      

      print("Got a connection from %s" % str(addr))

      player = 1
      
      msg = "You have connected as Player" + str(player) + "\r\n"
      clientsocket.send(msg.encode('ascii'))

      player += 1

      #clientsocket.close()

   game = True
   while game:
      msg = 'We are in the game!'+ "\r\n"
      clientsocket.send(msg.encode('ascii'))


run_server()