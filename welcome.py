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
        self.win.wm_iconbitmap('ubt-icon.ico')
                
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
        
        def add_frame(self):
        #krijimi i kornizes se brendshme
        self.frame = Frame(self.win, height=300, width=450)
        self.frame.place(x=80, y=50)

        x, y = 70, 20

        # vendosja e fotografise ne kornize
        self.img = PhotoImage(file='ubt-logo1.png')
        self.label = Label(self.frame, image=self.img)
        self.label.place(x=x+80, y=y+0)

        self.labeltitle = Label(self.frame, text="Welcome to UBT Students Point ")
        self.labeltitle.config(font=("Rubik", 20),fg='#808080')
        self.labeltitle.place(x=25, y=y+150)

        self.button = Button(self.frame, text="Continue", font=('Cambria', 20,)
                             , bg='#359fd2', fg='white', command=self.login)
        self.button.place(x=x+80, y=y+200)

        self.win.mainloop()
        
         def login(self):
        #mbyllja e dritares aktuale
        self.win.destroy()

        #hapja e dritares se re
        log = client.Design()
        log.Form1design()

        if __name__ == "__main__":

    x = CreateFrame()
    x.add_frame()
