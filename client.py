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
        
        self.User  = Label(self.login, 
                           text = "Username: ", 
                           font = "Cambria 14 bold", fg = '#ffffff', bg='#359fd2') 
          
        self.User.place(relx=0.138, rely=0.480, height=50, width=200)
          
        self.space1 = Entry(self.login,
                             font = "Cambria 13 bold", fg='#808080', borderwidth=2, bg='white', relief='ridge') 
          
        self.space1.place(relx=0.4, rely=0.490, height=40, relwidth=0.375)
          
        self.space1.focus() 


        self.Password  = Label(self.login, 
                               text = "Password: ",
                               font = "Cambria 14 bold", fg = '#ffffff', bg='#359fd2') 
          
        self.Password.place(relx=0.138, rely=0.593, height=40, width=200)


        self.space2 = Entry(self.login,
                             font = "Cambria 13 bold", show = '*', fg='#808080', borderwidth=2, bg='white', relief='ridge') 
          
        self.space2.place(relx=0.4, rely=0.593, height=40, relwidth=0.375)
          
        self.space2.focus() 

        self.var1 = IntVar()
        self.acceptRules = Checkbutton(self.login, 
                                       text="I accept the rules and conditions to enter this chat",
                                       font = "Cambria 10 bold",
                                       activebackground = '#359fd2',
                                       highlightcolor = '#359fd2',
                                       selectcolor = '#359fd2',
                                       variable = self.var1,
                                       fg = 'white',
                                       bg = '#359fd2',
                                       justify ='left',
                                       command=self.allowLogin)
        
        self.acceptRules.place(relx=0.185, rely=0.697, relheight=0.037, relwidth=0.648)
        
        self.copyRights = Label (self.login,
                                text = "COPYRIGHT  © 2021   UNIVERSITY OF BUSINESS AND TECHNOLOGY",
                                font = "Cambria 9 bold",
                                fg = '#ffffff',
                                bg = '#359fd2',
                                justify = CENTER )

        self.copyRights.place(relx=0.169, rely=0.935, height=41, width=444)
        
        #Krijimi i login butonit dhe vendosja ne dritare
        self.Login = Button(self.login, 
                         text = "LOGIN",  
                         font = "Cambria 14 bold", fg='#808080', bg='white', relief='ridge', 
                         command = lambda: self.goAhead(self.space1.get()))
        
        self.Login.place(relx=0.431, rely=0.772, height=44, width=107)
        self.Login.configure(state=DISABLED)

        self.Window.mainloop()
        
    def goAhead(self, name): 
        ### Pjesa e inkorporimit te databazes.
        
        informations = (self.space1.get(), self.space2.get())
        if self.space1.get() == "":
            messagebox.showinfo("Alert!!!","Please enter username first")
        elif self.space2.get() == "":
            messagebox.showinfo("Alert!!!","Please enter password first")
        else:
            checklist = db.DatabaseLink().dbcreate(informations)
            if checklist:
                messagebox.showinfo("Message","Login Successfully")
                self.login.destroy()
                self.chatlayout(name)
                
                # pranimi i informcaioneve nga serveri 
                rcv = threading.Thread(target=self.receive) 
                rcv.start()
            else:
                messagebox.showinfo("Message","Your username/password is wrong")

    def allowLogin(self):
        if self.var1.get()==0:
            self.Login.configure(state=DISABLED)
            #self.acceptRules.configure(state=NORMAL)
        else:
            self.Login.configure(state=ACTIVE)
            #self.acceptRules.configure(state=NORMAL)

    def chatlayout(self,name): 
        
        self.name = name 
        self.Window.deiconify() 
        self.Window.title("UBT Student - CHATROOM")
        #çaktivizimi i ndryshimit te madhesise se dritares
        self.Window.resizable(width = False, 
                              height = False) 
        self.Window.configure(width = 470, 
                              height = 550, 
                              bg = "#01A9E8") 
        #shfaqja e dritares ne qender te ekranit
        width = self.Window.winfo_screenwidth()
        height = self.Window.winfo_screenheight()
        x = int(width / 2 - 470 / 2)
        y = int(height / 2 - 550 / 2)
        str2 = "470x550+"+ str(x) + "+" + str(y)
        self.Window.geometry(str2)

        self.Welcome = Label(self.Window, 
                             bg = "#01A9E8",  
                              fg = "white", 
                              text = "Welcome" , 
                               font = "Cambria 14 bold") 
          
        self.Welcome.place(relx=0.298, rely=0.018, height=31, width=184)
        #paraqitja e emrit te userit ne dritare
        self.showName = Label(self.Window, 
                             bg = "#01A9E8",  
                              fg = "white", 
                              text = self.name , 
                               font = "Cambria 12 bold") 
        
        self.showName.place(relx=0.298, rely=0.091, height=31, width=184) 

        self.logoF2foto = PhotoImage(file='form2.png')
        self.logoF2 = Label(self.Window, image=self.logoF2foto, bg='#01A9E8')  
        self.logoF2.place(relx=0.095, rely=0.011, height=85, width=104)
        
        #Krijimi i butonit logout
        self.logout = Button(self.Window, 
                                text = "Log Out", 
                                font = "Cambria 12 bold",  
                                width = 10,
                                bg = "#36ABE0", fg="white", command = self.closeApp) 
          
        self.logout.place(relwidth=0.2,relheight=0.06,relx = 0.70, 
                      rely = 0.05)

        self.line = Label(self.Window, 
                          bg = "#D9E7EB")  
        self.line.place(relx=-0.021, rely=0.182, width=480, height=11)
          
        self.text = Text(self.Window, 
                             width = 20,  
                             height = 2, 
                             bg = "#ffffff", 
                             fg = "#000000", 
                             font = "Cambria 12",  
                             padx = 5, 
                             pady = 5) 
          
        self.text.place(relx=0.0, rely=0.2, height=345, width=470) 
          
        self.bottomPart = Label(self.Window, 
                                 bg = "#D7E5EA", 
                                 height = 80) 
          
        self.bottomPart.place(relwidth = 1, 
                               rely = 0.825) 
          
        self.message = Entry(self.bottomPart, 
                              bg = "#ffffff", 
                              fg = "#000000", 
                              font = "Cambria 12") 
          
        self.message.place(relwidth = 0.74, 
                            relheight = 0.06, 
                            rely = 0.008, 
                            relx = 0.011) 
          
        self.message.focus() 
          
        self.send = Button(self.bottomPart, 
                                text = "Send", 
                                font = "Rubik 12 bold",  
                                width = 20, 
                                bg = "#01A9E8", fg="white",
                                command = lambda : self.sendButton(self.message.get())) 
          
        self.send.place(relx = 0.77, 
                             rely = 0.008, 
                             relheight = 0.06,  
                             relwidth = 0.22)
        
        self.text.config(cursor = "arrow") 
          
        scrollBar = Scrollbar(self.text) 

        scrollBar.place(relheight = 1, 
                        relx = 0.974) 
          
        scrollBar.config(command = self.text.yview) 
          
        self.text.config(state = DISABLED)
        
    def sendButton(self, msg): 
        self.text.config(state = DISABLED) 
        self.msg=msg
        if msg == "":
            messagebox.showinfo("Alert","Please type something!!!")
        else:
            self.message.delete(0, END) 
            snd= threading.Thread(target = self.sendMessage) 
            snd.start() 

    def closeApp(self):
        self.answer = messagebox.askquestion("Logout","Are you sure you want to logout!!")
        if self.answer == 'yes':
            self.Window.destroy()

    def receive(self): 
    
        while True: 
            try: 
                message = self.client.recv(1024).decode(self.FORMAT) 
                  
                if message == 'NAME': 
                    self.client.send(self.name.encode(self.FORMAT)) 
                else:
                    self.text.config(state = NORMAL) 
                    self.text.insert(END, 
                                         message+"\n\n") 
                      
                    self.text.config(state = DISABLED) 
                    self.text.see(END) 
            except: 
                print("An error occured!") 
                self.client.close() 
                break 
           
    def sendMessage(self): 
        self.text.config(state=DISABLED) 
        while True: 
            message = (f"{self.name}: {self.msg}") 
            self.client.send(message.encode(self.FORMAT))     
            break    
