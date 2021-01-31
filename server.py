
import socket  
import threading
  

class Communicate:

    def __init__(self):

        self.PORT = 5080
        self.SERVER = '127.0.0.1'   
        #self.SERVER = socket.gethostbyname(socket.gethostname())	  
        self.ADDRESS = (self.SERVER, self.PORT)  
        self.FORMAT = "utf-8"
        self.clients, self.names = [], [] 
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.server.bind(self.ADDRESS)

    def startChat(self):   ### Polimorfizem
        print(self.SERVER + " has not started!!") 
