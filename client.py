import socket 
import threading 
from tkinter import *
from tkinter import font 
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import db


class ChatGeneral:
    ### Informacionet kryesore 
    PORT = 5080
    SERVER = "127.0.0.1"
    ADDRESS = (SERVER, PORT) 
    FORMAT = "utf-8"
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client.connect(ADDRESS) 

class MainForms(ChatGeneral): 

    def __init__(self): 
       
        self.Window = Tk()
        self.Window.wm_iconbitmap('ubt-icon.ico')
        self.Window.withdraw() 
          

        self.login = Toplevel() 
        self.login.title("UBT Students - Login Form") 
        self.login.resizable(width = False,  
                             height = False) 
        self.login.configure(width = 650, 
                             height = 674, bg='#359fd2')
        self.login.wm_iconbitmap('ubt-icon.ico') 
        #shfaqja e dritares ne qender te ekranit
        width = self.login.winfo_screenwidth()
        height = self.login.winfo_screenheight()
        x = int(width / 2 - 650 / 2)
        y = int(height / 2 - 674 / 2)
        str1 = "650x674+"+ str(x) + "+" + str(y)
        self.login.geometry(str1)

class ContinueNext:

    def goAhead(self):

        messagebox.showwarning("Information!","Sorry you can't continue next!!!")
