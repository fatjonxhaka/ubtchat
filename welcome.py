from tkinter import *
import client


class WelcomeWindow:
    
    def __init__(self):
        # Krijimi i faqes se pare
        self.win = Tk()

        #vendosja e dritares dhe ngjyres se prapavise
        self.canvas = Canvas(self.win, width=600, height=400, bg='black')
        self.canvas.pack(expand=YES, fill=BOTH)
    
    def __str__(self):
  
        #shfaqja e dritares ne qender te ekranit
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "500x500+"+ (x) + "+" + (y)
        self.win.geometry(str1)

        
class CreateFrame(WelcomeWindow):

    def __init__(self):
        
        self.win = Tk()

        
        self.canvas = Canvas(self.win, width=600, height=400, bg='#359fd2')
        self.canvas.pack(expand=YES, fill=BOTH)
   
         
        
        width = self.win.winfo_screenwidth()
        height = self.win.winfo_screenheight()
        x = int(width / 2 - 600 / 2)
        y = int(height / 2 - 400 / 2)
        str1 = "600x400+"+ str(x) + "+" + str(y)
        self.win.geometry(str1)

        #çaktivizimi i ndryshimit te madhesise se dritares
        self.win.resizable(width=False, height=False)

        #ndryshimi i titullit te dritares
        self.win.title("UBT Students Point")
