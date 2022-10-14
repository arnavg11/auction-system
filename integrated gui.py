from tkinter import *
import mysql.connector as mysql
import dataloading as dtl
import auctionsys as actsys
from networking import *
import tkinter.messagebox
import threading as thr
import time
from players import team_creation
from game import game_working

passw = None
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
            try:
                f= open("server_details.txt","r")
                global passw
                passw = f.read()
                connectServer()
            except:
                mysql_password(root)
            
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
    def popup(self):
        tkinter.messagebox.showinfo('info','''Refer to your system's card for the mysql password''')
    def __init__(self,master):
     global b
     self.master=master
     self.b = Button(root,command = self.popup, text= 'i',padx = 5,pady = 5,borderwidth = 0,width = 2)
     self.b.place(x = 650,y = 10)
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
         global passw
         passw = pss
         connectServer()
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
        self.t = thr.Thread(target = self.load)
        self.t.start()
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
    def load(self):
        dtl.maketable("players_fifa22",passw)
        dtl.loadData("players_fifa22",passw)
    def connServer(self,key):
        c = self.enterbox.get()
        print(c)
        if len(c)!=8:
            self.l1 = Label(self.root,text = "The server you entered may not be running",font = ("Helvetica",13),padx = 10,pady = 10,fg = "white",bg ="black" )
        x = comp.setip(self.enterbox.get())
        if x:
            self.t.join()
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
        time.sleep(.1)
        self.lab1 = Label(root,text = f"your username is: {comp.user}",bg = 'black',font=("Arial", 13),fg = "white")
        self.lab1.pack()
        
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
                        self.ele.append(Button(self.root,padx = 200,pady = 3,text=self.l[i],borderwidth=0))
                        x= self.ele[-1]
                        self.ele[-1].configure(command =lambda a=i,b=x: self.joinconn(self.l[a],b))
                        self.ele[-1].place(relx=0.5,rely=n*0.1+0.17,anchor='center')
    def joinconn(self,user2,b):
        print("J")
        b.configure(bg= "blue")
        comp.write(f"::cnct-{comp.user}:{user2}")
    def transition(self):
        while True:
            if comp.paired:
                self.cont = False
                print(self.ele)
                destruct(self.ele+[self.lab,self.lab1])
                distributeMoney(root)
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
moneyToTeam = None
money = 1000
class distributeMoney:
    def popup(self):
        tkinter.messagebox.showinfo('info','''Team investment:
    Out of 50 randomly selected players, the base team of the user is made by prioritizing higher value players and the strength of this priority is determined by how much money the user decides to put into forminghis baseteam.
    
Auction players:
    These are high ranked players chosen so that users can battle for them witth the remainder of their money.
Auction system:
    Click on raise bid by 100 if you want to increase the bid for a player.
    The player's name should turn green if you have the highest bid for that player and red if your opponent has the highest bid.
    If you want to back out of the bid for a player, you can only do so if your opponent has the highest bid.
    You cannot set a bid for a player if the total bid amount crosses the money you have left.
    
    ''')
    def __init__(self,root):
        global comp
        comp.eventhand = self.evnt
        self.bid = [0,0]
        self.bidDone = [False,False]
        self.root=root
        self.b = Button(root,command = self.popup, text= 'i',padx = 5,pady = 5,borderwidth = 0,width = 2)
        self.b.place(x=650,y=30)
        self.root.configure(bg = "black")
        self.root.geometry("700x400")
        self.ele = []
        if comp.user>comp.opp:
            self.p2 = actsys.pickAuctionPlayer(passw)   #name,ovr,pos
            self.p1 = actsys.pickAuctionPlayer(passw)
            
            comp.write(f"{comp.opp}-auctplrs:{self.p1},{self.p2}")
        time.sleep(.2)
        self.label1 = Label(root,text = f"bid:{self.bid[0]}",bg = 'black',font=("Arial", 20),fg = "white")
        self.label1_ = Label(root,text = f"bid:{self.bid[1]}",bg = 'black',font=("Arial", 20),fg = "white")
        self.ele.append(Label(self.root,text = "how much of your money do you want to invest in auction?(out of 1000)",font = ("Helvetica",13),padx = 10,pady = 10,fg = "white",bg ="black" ))
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
            global moneyToTeam,money
            moneyToTeam = 1000-int(c)
            money= int(c)
            destruct(self.ele)
            self._init__(root)
        else:
            self.l.config(text = "Please enter a valid integer between 0 and 1000")
    def _init__(self,root):
        global comp
        canvas = Canvas(root, width = 660, height = 400, bg = 'black',relief = 'sunken')
        canvas.place
        self.root = root
        self.canvas = canvas
        self.moneyLabel = Label(root,text = f"initial money:{money}",bg = 'black',font=("Arial", 20),fg = "white")
        root.geometry("700x400")
        root.title("FIFA")
        root.resizable(False,False)
        root.config(bg = 'black')
        self.label2 = Label(root,text = "name:"+self.p1[0],bg = 'black',font=("Arial", 20),fg="white")
        self.label3 = Label(root,text = "rating:"+str(self.p1[1]),bg = 'black',font=("Arial", 20),fg = "white")

        self.label1.place(x = 30,y = 90)
        self.label2.place(x = 30,y = 150)
        self.label3.place(x = 30,y = 210)

        self.label2_ = Label(root,text = "name:"+self.p2[0],bg = 'black',font=("Arial", 20),fg = "white")
        self.label3_ = Label(root,text = "rating:"+str(self.p2[1]),bg = 'black',font=("Arial", 20),fg = "white")

        self.label1_.place(x = 390,y = 90)
        self.label2_.place(x = 390,y = 150)
        self.label3_.place(x = 390,y = 210)

        b1 = Button(root,command = lambda:self.raisebid(1), text= 'RAISE BID BY 100',padx = 50,pady = 12,borderwidth = 0,width = 2)
        b2 = Button(root,command = lambda:self.back(1), text= 'BACKOUT',padx = 50,pady = 12,borderwidth = 0,width = 2)
        b3 = Button(root,command = lambda:self.raisebid(2), text= 'RAISE BID BY 100',padx = 50,pady = 12,borderwidth = 0,width = 2)
        b4 = Button(root,command = lambda:self.back(2), text= 'BACKKOUT',padx = 50,pady = 12,borderwidth = 0,width = 2)
        self.moneyLabel.place(x=250,y=5)
        b1.place(x = 20, y = 320)
        b2.place(x = 175, y = 320)
        b3.place(x = 377, y = 320)
        b4.place(x = 533, y = 320)
        self.ele = [self.canvas,self.label1,self.moneyLabel,self.label2,self.label3,self.label1_,self.label2_,self.label3_,b1,b2,b3,b4]
    def raisebid(self, auctplr):
        if money<100+self.bid[0]*(auctplr==1 or self.label1.cget("fg")=="green")+self.bid[1]*(auctplr==2 or self.label1_.cget("fg")=="green"):
            return
        comp.write(f"{comp.opp}-raisebid:{auctplr}")
        print(f"{comp.opp}-raisebid:{auctplr}")
        self.evnt([f"raisebid:{auctplr}"],True)
    def back(self,plr):
        if (self.label1.cget("fg")!="red" and plr == 1) or (self.label1_.cget("fg")!="red" and plr == 2):
            return
        print(self.label1.cget("fg"))
        comp.write(comp.opp+"-back:"+str(plr))
        self.evnt(("back:"+str(plr)).split("-"),True)
    def evnt(self,msg,msgsentbyself = False):
        print(msg)
        msg = msg[0].split(":")
        if msg[0] == "raisebid":
            
            print((self.bid,msg[1]))
            if (not self.bidDone[0]) and msg[1]=="1":
                self.bid[0]+=100
                self.label1.configure(text = "bid:"+str(self.bid[0]))
                if msgsentbyself:
                    self.label1.configure(fg = "green")
                else:
                    self.label1.configure(fg = "red")
            elif (not self.bidDone[1]) and msg[1]=="2":
                self.bid[1]+=100
                self.label1_.configure(text = "bid:"+str(self.bid[1]))
                if msgsentbyself:
                    self.label1_.configure(fg = "green")
                else:
                    self.label1_.configure(fg = "red")
            
        elif msg[0]=="back":
            print(5)
            if msg[1]=="1":
                self.label1.configure(text = "bid:"+str(self.bid[0])+"(confirmed)")
                self.bidDone[0] = True
            elif msg[1]=="2":
                self.label1_.configure(text = "bid:"+str(self.bid[1])+"(confirmed)")
                self.bidDone[1] = True
            if self.bidDone[0] and self.bidDone[1]:
                print(moneyToTeam/2000+1)
                team = actsys.team_init(moneyToTeam/500+1,passw)
                if self.label1.cget("fg")=="green":
                    if self.p1[2] in ["LB","RB","CB","CDM","CM","GK"]:
                        mode = 0
                    else:
                        mode = 1
                    lowest = [None,0]
                    for i in range(3):
                        if lowest[1]<team[mode][i][1]:
                            lowest = [i,team[mode][i][1]]
                    team[mode][lowest[0]] = self.p1
                if self.label1_.cget("fg")=="green":
                    if self.p2[2] in ["LB","RB","CB","CDM","CM","GK"]:
                        mode = 0
                    else:
                        mode = 1
                    lowest = [None,0]
                    for i in range(3):
                        if lowest[1]<team[mode][i][1]:
                            lowest = [i,team[mode][i][1]]
                    team[mode][lowest[0]] = self.p2
                print(team)
                destruct(self.ele)
                gamework(root,team)
        elif msg[0]=="auctplrs":
            self.p1,self.p2 = eval(msg[1])

class gamework:

    def __init__(self,master,team):
        self.team_final = []
        comp.eventhand = self.event_handler

        team[0].extend(team[1])
        team_new = team[0]
        
        print()
        print("see:",team_new)
        print()

        print(comp.user)
        team_new.insert(0,comp.user)
        self.team_final.append(team_new)
        self.send(f"{team_new}")

    def event_handler(self, event):
        value = eval(event[0])
        opp_team = value
        self.team_final.append(opp_team)
        print("final team:",self.team_final)
        self.player_moves()
        game_start(root)

    def player_moves(self):
        f = team_creation(root,comp,self.team_final)

    def send(self,msg):
        print("send",msg)
        comp.write(f"{comp.opp}-{msg}")

class game_start:
    def __init__(self,root):
        g = game_working(root,comp)
   
serverOrClient(root)

           
