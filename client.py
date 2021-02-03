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
        
        class Design(MainForms, ContinueNext):

    def Form1design(self):

        self.__logo = PhotoImage(file='ubt-logo1.png')
        self.labellogo = Label(self.login, image=self._Design__logo, bg='#359fd2')

        self.labellogo.place(relx=0.415, rely=0.089, height=130, width=128)

        self.label1 = Label(self.login,  
                       text = "University of Business and Technology", 
                       justify = CENTER,  
                       font = "Cambria 18 bold", fg = '#ffffff', bg='#359fd2') 

        self.label1.place(relx=-0.015, rely=0.0, height=51, width=665)

        
        self.label2 = Label(self.login,  
                       text = "Students Application", 
                       justify = CENTER,  
                       font = "Cambria 14 bold", fg = '#ffffff', bg='#359fd2') 

        self.label2.place(relx=0.154, rely=0.282, height=71, width=454)


        self.lineDesign1 = Label(self.login, bg='#D3D3D3', relief='groove')
        self.lineDesign1.place(relx=0.046, rely=0.371, height=7, width=594)

        self.label3 = Label(self.login,  
                       text = "Login", 
                       justify = CENTER,  
                       font = "Cambria 14 bold", fg = '#ffffff', bg='#359fd2')

        self.label3.place(relx=0.277, rely=0.386, height=31, width=294)

        self.lineDesign2 = Label(self.login, bg='#D3D3D3', relief='groove')
        self.lineDesign2.place(relx=0.180, rely=0.445, height=7, width=400)

