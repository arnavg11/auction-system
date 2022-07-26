from tkinter import *
import time
#import mysql.connector as mysql
from networking import *
import threading as thr
bg= "black"
fg = "white"
def destruct(ele):
    for i in ele:
        print(i)
        i.destroy()

otherPlayer = None
root = Tk()

class serverOrClient:
    def __init__(self,master = root):
         self.ele = []
         self.master=master
         self.master.geometry("700x400")
         self.master.title("FIFA")
         self.master.resizable(False,False)

         self.clientor = Label(self.master,text = "DO YOU WANT TO SET UP THE DEVICE AS A CLIENT OR SERVER")
         self.clientor.place(x = 150,y = 70)
         self.ele.append(self.clientor)

         self.client = Button(self.master,text="CLIENT",padx=80,pady=30,borderwidth=0,command =lambda:\
                              self.setAsClient())

         self.server = Button(self.master,text="SERVER",padx=78,pady=30,borderwidth=0,command =lambda:\
                              self.setAsServer())

         self.ele.append(self.client)
         self.ele.append(self.server)
         self.client.place(x = 100,y = 200)
         self.server.place(x = 358,y=200)

         
         root.mainloop()
    def setAsServer(self):
        global comp
        comp = Server()
        self.next_window(False)
    def setAsClient(self):
        global comp
        comp = Client()
        self.next_window(True)
    
    def next_window(self,isClient):
        destruct(self.ele)
        if isClient:enterUser()
        else:server_screen(root)

#comp = None
class enterUser:
    def __init__(self,root=root):
        self.ele = []
        self.entryfg = "red"
        
        self.root = root
        self.root.resizable(False,False)
        self.root.geometry(f"600x150+5+5")
        self.root.configure(bg= bg)
        self.root.title("a")
        
        
        self.ele.append(Label(self.root,text = "Enter your username(8+character, dashes and colon are not allowed):",font = "Helvetica",padx = 10,pady = 10,foreground = fg,background = bg))
        self.ele[-1].place(x = 0, y=  0)
        
        self.enterbox = Entry(self.root,width = 60,background = "white", foreground = self.entryfg)
        self.enterbox.place(height = 30,x = 10,y = 50)
        self.enterbox.bind("<Key>",self.checkName)
        self.ele.append(self.enterbox)

        
        self.l =  Label(self.root,text = "",font = "Helvetica",padx = 10,pady = 10,foreground = fg,background = bg)
        self.l.place(x = 10, y=  100)
        self.ele.append(self.l)
        
        self.root.mainloop()
    def subm(self):
        c = self.enterbox.get()
        if '-' in c or ":" in c or len(c)<8:
            self.l.config(text = "Please enter a 8+ character username without dashes or colon")
        else:
            comp.user = c
            self.enterbox.delete(0,END)
            destruct(self.ele)
            connectServer(root)
            
    def checkName(self,key):
            if ord(key.char) == 13:
                self.subm()
                return
            c = self.enterbox.get()
            if "-" not in c and ":" not in c and len(c)>=8:
                    self.entryfg = "green"
            else:
                    self.entryfg = "red"
            self.enterbox.config(foreground = self.entryfg)
            
class mysql_password:
    def __init__(self,master):
     global b
     self.master=master
     self.master.geometry("700x400")
     self.master.title("FIFA")
     b = StringVar()
     self.master.configure(bg = "black")

     self.password = Label(self.master,bg = "black",fg = "white",text = "Please enter your system's mysql password and press enter",font = ("Calibri",17))
     self.password.pack()

     self.entry = Entry(self.master,text=b,show = "*",font = ("Calibri",17))
     self.entry.pack()
     self.entry.bind("<Return>",self.checkpss)
     self.ele = [self.password,self.entry]
    def checkpss(self,k):
     if ord(k.char)!=13:
         return
     pss = str(b.get())
     
     try:
         test = mysql.connect(host = "localhost",user = "root", passwd = pss)
         destruct(self.ele)
         with open("server_details.txt","w") as user:
             mysql_pss = pss
             user.write(pss)
         server_screen()
     except mysql.errors.ProgrammingError:
         pass

class server_screen:
    def __init__(self,root=root):
        self.r = root
        self.r.geometry("400x300")
        self.r.configure(bg = "black")
        self.ele = []
        self.label = Label(self.r,text = f"Your ip address is : {convertih(myip)}",font = ("Calibri",20),bg = "black",fg ="white")
        self.label.pack()
        self.ele.append(self.label)
        self.b =Button(self.r,text="close this server",command = self.close,bg = "black",fg =
                       "white")
        self.b.pack()
        self.ele.append(self.b)
    def close(self):
        global comp
        del comp
        self.r.destroy()
        del self
class connectServer:
    def __init__(self,root = root):
        self.root = root
        self.root.configure(bg = "black")
        self.root.geometry("700x400")
        self.l = Label(self.root,text = "Enter the server ip you want to join and press enter",font = ("Helvetica",13),padx = 10,pady = 10,fg = "white",bg ="black" )
        self.ele = [self.l]
        self.l.pack()
        self.enterbox = Entry(self.root,width = 60,background = "white")
        self.enterbox.pack()
        self.enterbox.bind("<Return>",self.connServer)
        self.ele.append(self.enterbox)
    def connServer(self,key):
        print(self.enterbox.get())
        x = comp.setip(self.enterbox.get())
        if x:
            destruct(self.ele)
            join(root)
        else:
            self.l1 = Label(self.root,text = "The server you entered may not be running",font = ("Helvetica",13),padx = 10,pady = 10,fg = "white",bg ="black" )
class join():
    def __init__(self,root):
        self.root = root
        self.root.configure(bg = "black")
        self.root.geometry("700x400")
        self.ele = []
        self.l = None
        self.cont = True
        t = thr.Thread(target=self.updateList)
        t.start()
        t2 = thr.Thread(target=self.transition)
        t2.start()
        self.lab = Label(self.root,text = "Pick who you want to play with:",font = ("Helvetica",13),padx = 10,pady = 10,fg = "white",bg ="black" )
        self.lab.pack()
        
    def updateList(self):
        while True:
            if not self.cont:
                break
            if self.l !=comp.servconn:
                destruct(self.ele)
                print(2)
                self.l = comp.servconn
                n = 0
                for i in range(len(self.l)):
                    if self.l[i]!= comp.user:
                        n+=1
                        self.ele.append(Button(self.root,padx = 200,pady = 3,text=self.l[i],borderwidth=0,command =
                                               lambda a=i: self.joinconn(self.l[a])))
                        self.ele[-1].place(relx=0.5,rely=i*0.1+0.05,anchor='center')
    def joinconn(self,user2):
        print("J")
        comp.write(f"::cnct-{comp.user}:{user2}")
    def transition(self):
        while True:
            if comp.paired:
                self.cont = False
                print(self.ele)
                destruct(self.ele+[self.lab])
                message()
                break

class message:
    def __init__(self,root=root):
        self.root = root
        self.root.configure(bg = "black")
        self.root.geometry("700x400")
        self.enterbox = Entry(self.root,width = 60,background = "white")
        self.enterbox.pack()
        self.enterbox.bind("<Return>",self.onEnter)
    def onEnter(self,k):
        comp.write(f"{comp.opp}-{self.enterbox.get()}")
class distributeMoney:
    def __init__(self,root):
        self.root=root
        self.root.configure(bg = "black")
        self.root.geometry("700x400")
        self.ele = []
        self.ele.append(Label(self.root,text = "how much of your money do you want to invest in your base team?(out of 1000)",font = ("Helvetica",13),padx = 10,pady = 10,fg = "white",bg ="black" ))
        self.ele[-1].pack()
        self.ele.append(Entry(self.root,width = 60,background = "white"))
        self.ele[-1].pack()
        self.enterb = self.ele[-1]
        self.enterb.bind("<Key>",self.sub)
        self.l = Label(self.root,font = ("Helvetica",13),padx = 10,pady = 10,fg = "white",bg ="black" )
        self.l.pack()
        self.ele.append(self.l)
    def sub(self,key):
        if ord(key.char)!=13:
            return
        c = self.enterb.get()
        if c.isdigit() and 0<=int(c)<=1000:
            destruct(self.ele)
            game(root)
        else:
            self.l.config(text = "Please enter a valid integer between 0 and 1000")
        
    
class game:
    def __init__(self,master):
     self.master=master
     self.master.geometry("700x400")
     self.root.configure(bg = "black")
     self.button1 = Button(self.master,text="GAME",padx=130,pady=50,borderwidth=0)
     self.button2 = Button(self.master,text="AUCTION",padx=110,pady=50,borderwidth=0)
     self.button3 = Button(self.master,text="CARDS",padx=127,pady=50,borderwidth=0)
     self.button4 = Button(self.master,text="TEAM MANAGEMENT",padx=74,pady=50,borderwidth=0)
     self.button4.place(x=370,y=255)

     self.button1.place(x = 15,y = 100)
     self.button2.place(x = 370,y=100)
     self.button3.place(x = 15,y = 255)
     
     

     self.quit=Button(self.master,text="<--",command=self.close_window,borderwidth=0)

     self.quit.place(x=15,y=10)

    def close_window(self):
     self.master.destroy()
    
serverOrClient(root)
