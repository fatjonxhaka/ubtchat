
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
       
class StartCommunication(Communicate):

    def startChat(self): 
        
        print("Server is working on " + self.SERVER) 
        
        self.server.listen() 
        
        while True: 
            
            self.conn, self.addr =  self.server.accept() 
            self.conn.send("NAME".encode(self.FORMAT)) 
            
            self.name = self.conn.recv(1024).decode(self.FORMAT) 
            
            self.names.append(self.name) 
            self.clients.append(self.conn) 
            
            print(f"Name is :{self.name}") 
            
            self.broadcastMessage(f"{self.name} has joined the chat!".encode(self.FORMAT)) 
            
            self.conn.send('Connection successful!'.encode(self.FORMAT)) 
            
            thread = threading.Thread(target = self.handle, 
                                    args = (self.conn, self.addr)) 
            thread.start() 
            
            print(f"active connections {threading.activeCount()-1}") 
    

    def handle(self, conn, addr): 
        
        print(f"new connection {self.addr}") 
        connected = True
        
        while connected: 
            self.message = conn.recv(1024) 
            
            self.broadcastMessage(self.message) 
        
        conn.close()
 
