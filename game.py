from tkinter import *
import pickle
from PIL import Image,ImageTk


class game_working:
    def __init__(self,root,comp):
        self.comp = comp
        self.comp.eventhand = self.event_handler

        #screen
        self.root = root
        self.root.geometry("1050x750")
        self.root.title("FIFAPROLALU")

        self.root.resizable(False,False)

        self.player = None
        self.playing = []
        self.score = 0
        self.selfscore = 0


        self.turn = 0
        self.opp_player = None
        self.opp_player_test = None

        self.canvas = Canvas(self.root, width = 1050, height = 650, bg = 'black',relief = 'sunken')
        self.canvas.pack()
       
        self.canvas.create_text(600, 200, anchor='w',text=self.selfscore, fill="white", font=('Arial 15 '))
        self.canvas.create_text(640, 200,text=':', fill="white", font=('Arial 15 '))
        self.canvas.create_text(680, 200, anchor='e',text='0', fill="white", font=('Arial 15 '))
       

        self.choose_player()


        #football ground
        img = Image.open("football_field.png")
        resize = img.resize((480,385), Image.ANTIALIAS)
        rotated = resize.rotate(90,expand = True)
        self.new_image= ImageTk.PhotoImage(rotated)
        self.canvas.create_image(224,250,image=self.new_image)


        self.canvas.create_rectangle(20,500,426,635,fill ='blue',outline = 'blue')          

        self.canvas.create_rectangle(471,330,741,635,fill ='black', outline = 'white')

        #health bar

        self.x1 = 416
        self.x_ = 416
        player_bar = self.canvas.create_rectangle(30,480,416,505,fill ='green',outline = 'white')
        opponent_bar = self.canvas.create_rectangle(30,10,416,35,fill ='red',outline = 'white')

        stamina_bar = self.canvas.create_rectangle(30,465,416,475,fill ='purple',outline = 'white')

        with open("team.dat","rb") as file:
                l =[]
           
                t = pickle.load(file)
                for i in range(len(t)):
                    if t[i][0] == self.comp.user:
                        for j in range(1,len(t[i])):
                            l.append(t[i][j][0].upper())

           
                self.f_players = Listbox(self.canvas,width = 27, height = 13,bg = 'black',fg = 'white',font = 'Arial',activestyle = 'none',bd = 2,relief = 'sunken')

                for item in l:
                    self.f_players.insert(item,item)

                def select():
                    selected_name = self.f_players.get(ANCHOR)
                    if selected_name != '':
                        self.card(selected_name)


                   
                select_option1 = Button(self.root, text= 'select' ,bg = 'black',fg = 'white',padx = 76,pady = 15,command = lambda: select(),borderwidth = 0,width = 4)
                select_option1.place(x =803,y =613)
               

               
                self.f_players.place(x = 771, y = 330)

    def move_buttons(self,player):
        with open("team.dat","rb") as file:
           
                t = pickle.load(file)
                for i in range(len(t)):
                    if t[i][0] == self.comp.user:
                        for j in range(1,len(t[i])):
                            print("players buttons",player.lower(),t[i][j][0])
                            if player.lower() ==  t[i][j][0].lower():
                           
                                self.opp_player = t[i][j][0].upper()
                                self.send(f'starting_player:{self.opp_player}')
                                self.card(t[i][j][0])
                                self.playing.append(t[i][j][0].upper())
                                damage1 = t[i][j][2][1]
                                damage2 = t[i][j][3][1]
                                damage3 = t[i][j][4][1]

                   
                                self.b1 = Button(self.root, text=t[i][j][2][0],padx = 70,pady = 15,borderwidth = 0,command = lambda: self.health_bar(damage1),width = 6)
                                self.b2 = Button(self.root, text=t[i][j][3][0],padx = 70,pady = 15,borderwidth = 0,command = lambda: self.health_bar(damage2),width = 6)
                                self.b3 = Button(self.root, text=t[i][j][4][0],padx = 70,pady = 15,borderwidth = 0,command = lambda: self.health_bar(damage3),width =6)

                                self.b1.place(x = 30, y = 520)
                                self.b2.place(x = 230, y = 520)
                                self.b3.place(x = 30, y = 585)

                                self.canvas.create_rectangle(30,480,416,505,fill ='green',outline = 'white')

        self.pop.destroy()

    def card(self,x):
        self.canvas.create_rectangle(481,340,731,625,fill ='black',outline = 'black')
   
        with open("team.dat","rb") as file:
                t = pickle.load(file)
                for i in range(len(t)):
                    if t[i][0] == self.comp.user:
                        for j in range(1,len(t[i])):
                            print("players card",x.lower(),t[i][j][0])
                            if t[i][j][0].lower() == x.lower():
                                n = t[i][j][0].upper()
                                st = str(t[i][j][5])
                           
                                m1 = t[i][j][2][0].upper()
                                m2 = t[i][j][3][0].upper()
                                m3 = t[i][j][4][0].upper()

                                d1 = str(t[i][j][2][1])
                                d2 = str(t[i][j][3][1])
                                d3 = str(t[i][j][4][1])

                       
                                name = self.canvas.create_text(486, 350, anchor='w',text=n, fill="white", font=('Arial 15 '))
                                stamina = self.canvas.create_text(726, 350, anchor='e', text=st, fill="white", font=('Arial 15 '))

                                move1 = self.canvas.create_text(486, 450, anchor='w', text=m1, fill="white", font=('Arial 15 '))
                                damage1 = self.canvas.create_text(726, 450, anchor='e', text=d1, fill="white", font=('Arial 15 '))

                                move2 = self.canvas.create_text(486, 480, anchor='w', text=m2, fill="white", font=('Arial 15 '))
                                damage2 = self.canvas.create_text(726, 480, anchor='e',text=d2, fill="white", font=('Arial 15 '))

                                move3 = self.canvas.create_text(486, 510, anchor='w', text=m3, fill="white", font=('Arial 15 '))
                                damage3 = self.canvas.create_text(726, 510, anchor='e', text=d3, fill="white", font=('Arial 15 '))

    def event_handler(self, event):

        keyword,value = event[0].split(":")

        if keyword == 'damage':
           
            x1 = value
            x1 = float(x1)
            print()
            print("value of x1:",x1)
            print()
            self.turn=0
            self.endturn()

            if x1 <= 30:
                self.canvas.create_rectangle(30,480,416,505,fill ='black',outline = 'white')
                with open("team.dat","rb") as file:
                    l =[]
       
                    t = pickle.load(file)
                    for i in range(len(t)):
                        if t[i][0] == self.comp.user:
                            for j in range(1,len(t[i])):
                                l.append(t[i][j][0].upper())

                len_l = len(l)
                len_playing = len(self.playing)

                if len_l == len_playing:
                    self.score += 1
                    self.send(f'your_score:{self.score}')
                    self.canvas.create_rectangle(650,190,690,210,fill = 'black',outline = 'black')
                    self.canvas.create_text(680, 200, anchor='e',text=f'{self.score}', fill="white", font=('Arial 15 '))

                    if self.score == 3:
                        self.lost()

                    else:
                        self.choose_player()


                else:
                    self.change_player()

            else:  
                self.canvas.create_rectangle(x1,480.5,415,504,fill = 'black',outline = 'black')
       
        elif keyword == 'opp_name_change':

            self.opp_player = value
            self.opp_player_test = self.opp_player
            self.canvas.create_rectangle(30,10,416,35,fill ='red',outline = 'white')
            self.canvas.create_rectangle(420,10,600,60,fill ='black',outline = 'black')
            self.canvas.create_text(436, 20, anchor='w',text=self.opp_player, fill="white", font=('Arial 15 '))

        elif keyword == 'starting_player':
            self.opp_player = value
            self.opp_player_test = self.opp_player
            self.canvas.create_rectangle(30,10,416,35,fill ='red',outline = 'white')
            self.canvas.create_rectangle(420,10,600,60,fill ='black',outline = 'black')
            opp = self.canvas.create_text(436,20, anchor='w',text=self.opp_player, fill="white", font=('Arial 15 '))

        elif keyword == 'won':
            self.won()

        elif keyword == 'wonround':
            self.playing = []
            self.choose_player()
           
        elif keyword == 'your_score':
            self.selfscore = value
            self.canvas.create_rectangle(560,190,630,210,fill = 'black',outline = 'black')
            self.canvas.create_text(600, 200, anchor='w',text=f'{self.selfscore}', fill="white", font=('Arial 15 '))


    def health_bar(self,damage):
        self.turn = 1
        self.endturn()
       
        print()
        print("done:",damage)
        print()

        """damage_per = (damage/total_health)*100
        damage_amo = (damage_per/100) * 386"""
       
        with open("team.dat","rb") as file:
            t = pickle.load(file)
            for i in range(len(t)):
                if t[i][0] != self.comp.user:
                    for j in range(1,len(t[i])):
                        if t[i][j][0].lower() ==self.opp_player_test.lower():
                            opp_total_health = t[i][j][5]
                            print()
                            print("opp player",self.opp_player_test)
                            print("opp damage:",opp_total_health)
                            print("damage sent",damage)
                            damage_amo = (damage/opp_total_health)*386
                            print("damage amount:",damage_amo)
           
            self.x1 -= 30      
            self.x1 -= damage_amo
            print("check",self.x1)
            print()
            self.x1 += 30

            if self.x1 < 0:
                self.x1 = 0

            if self.x1 <= 30:
                self.send(f'damage:{self.x1}')
                print("sending")
                #canvas.create_rectangle(30,480,416,505,fill ='black',outline = 'white')
                self.canvas.create_rectangle(30,10,416,35,fill ='black',outline = 'white')
                self.x1 = 416

            else:  
                self.send(f'damage:{self.x1}')
                print("sending")
                #canvas.create_rectangle(x1,480.5,x2-1,504,fill = 'black',outline = 'black')
                self.canvas.create_rectangle(self.x1,11,415,34,fill ='black',outline = 'black')

        if damage >= 100:
            x__ = self.x_
            self.x_ -= (70/100) * 386

            if self.x_ <= 30:
                self.canvas.create_rectangle(30,465,416,475,fill ='black',outline = 'white')

            else:
                self.canvas.create_rectangle(self.x_,466,x__ - 1,474,fill ='black',outline = 'black')

        elif damage >= 65:
            x__ = self.x_
            self.x_ -= (40/100) * 386

            if self.x_ <= 30:
                self.canvas.create_rectangle(30,465,416,475,fill ='black',outline = 'white')

            else:
                self.canvas.create_rectangle(self.x_,466,x__ - 1,474,fill ='black',outline = 'black')

        elif damage >= 40:
            x__ = self.x_
            self.x_ -= (20/100) * 386

            if self.x_ <= 30:
                self.canvas.create_rectangle(30,465,416,475,fill ='black',outline = 'white')

            else:
                self.canvas.create_rectangle(self.x_,466,x__ - 1,474,fill ='black',outline = 'black')
   
    def send(self,msg):
        print("send",msg)
        self.comp.write(f"{self.comp.opp}-{msg}")

    def change_info(self,selected_name):

        with open("team.dat","rb") as file:
            l =[]
       
            t = pickle.load(file)
            for i in range(len(t)):
                if t[i][0] == self.comp.user:
                    for j in range(1,len(t[i])):
                        if t[i][j][0].lower() == selected_name.lower():
                            self.playing.append(selected_name)

                            self.b1.config(text = t[i][j][2][0])
                            self.b2.config(text = t[i][j][3][0])
                            self.b3.config(text = t[i][j][4][0])

                            new_damage1 = t[i][j][2][1]
                            new_damage2 = t[i][j][3][1]
                            new_damage3 = t[i][j][4][1]

                            self.b1.config(command = lambda: self.health_bar(new_damage1))
                            self.b2.config(command = lambda: self.health_bar(new_damage2))
                            self.b3.config(command = lambda: self.health_bar(new_damage3))
                       
                            self.send(f'opp_name_change:{selected_name}')
                            self.canvas.create_rectangle(30,480,416,505,fill ='green',outline = 'white')
                            self.card(selected_name)

        self.b1['state'] = NORMAL
        self.b2['state'] = NORMAL
        self.b3['state'] = NORMAL
        self.pop.destroy()

    def change_player(self):
        #global pop
        self.pop = Toplevel(self.root)
        self.pop.geometry("450x400")
        self.pop.config(bg = "grey")
        self.pop.resizable(False,False)
        self.b1['state'] = DISABLED
        self.b2['state'] = DISABLED
        self.b3['state'] = DISABLED

        with open("team.dat","rb") as file:
            l =[]
       
            t = pickle.load(file)
            for i in range(len(t)):
                if t[i][0] == self.comp.user:
                    for j in range(1,len(t[i])):
                        l.append(t[i][j][0].upper())

            label1 = Label(self.pop,text = "YOUR PLAYER HAS BEEN DEFEATED CHOOSE ANOTHER",bg = 'grey',fg = 'black',font=("Arial", 15))
            label1.place(x = 10,y = 20)

            f = Frame(self.pop,height = 700,width = 700,bg = 'grey')
            f.place(x = 10,y = 50)

            def select_choice():
                selected_name = player_choice.get(ANCHOR)
                if selected_name != '':
                    self.change_info(selected_name)
                    self.f_players.delete(selected_name)
               
           
       
            player_choice = Listbox(f,width = 27, height = 13,fg = 'black',font = 'Arial',activestyle = 'none',bd = 2,relief = 'sunken')
            player_choice.place(x = 110, y = 50)

            print(self.playing)
            print(l)

            for i in self.playing:
                if i in l:
                    l.remove(i)

            for item in l:
                player_choice.insert(END,item)

            select_option1 = Button(f, text= 'select' ,bg = 'black',fg = 'white',padx = 76,pady = 15,command = lambda: select_choice(),borderwidth = 0,width = 4,relief = 'sunken')
            select_option1.place(x =110,y =280)

    def endturn(self):
        if self.turn == 1:
            self.b1['state'] = DISABLED
            self.b2['state'] = DISABLED
            self.b3['state'] = DISABLED
        else:
            self.b1['state'] = NORMAL
            self.b2['state'] = NORMAL
            self.b3['state'] = NORMAL
       
    def choose_player(self):
        self.pop = Toplevel(self.root)
        self.pop.geometry("450x400")
        self.pop.config(bg = "grey")
        self.pop.resizable(False,False)

        with open("team.dat","rb") as file:
            l =[]
       
            t = pickle.load(file)
            for i in range(len(t)):
                if t[i][0] == self.comp.user:
                    for j in range(1,len(t[i])):
                        l.append(t[i][j][0].upper())

            if len(l) == len(self.playing):
                self.playing = []
                round_lost = Label(self.pop,text = 'YOU HAVE LOST THE ROUND',bg = 'grey',fg = 'black',pady = 30,font=("Arial", 15))
                round_lost2 =  Label(self.pop,text = 'SELECT NEW PLAYER',bg = 'grey',fg = 'black',pady = 50,font=("Arial", 15))
                round_lost.pack()
                round_lost2.pack()
                self.send("wonround:0")

            else:
                label1 = Label(self.pop,text = "CHOOSE PLAYER",bg = 'grey',fg = 'black',font=("Arial", 15))
                label1.place(x = 10,y = 20)

            f = Frame(self.pop,height = 700,width = 700,bg = 'grey')
            f.place(x = 10,y = 50)

            def PLAYER():
                self.player = player_choice.get(ANCHOR)
                if self.player != '':
                    self.move_buttons(self.player)
           
       
            player_choice = Listbox(f,width = 27, height = 13,fg = 'black',font = 'Arial',activestyle = 'none',bd = 2,relief = 'sunken')
            player_choice.place(x = 110, y = 50)

            for item in l:
                player_choice.insert(END,item)

            select_option1 = Button(f, text= 'select' ,bg = 'black',fg = 'white',padx = 76,pady = 15,command = lambda: PLAYER(),borderwidth = 0,width = 4,relief = 'sunken')
            select_option1.place(x =110,y =280)

       
    def lost(self):
        self.pop = Toplevel(self.root)
        self.pop.geometry("450x400")
        self.pop.config(bg = "grey")
        self.pop.resizable(False,False)

        lab = Label(self.pop,text = "YOU LOST",bg = 'grey',fg = 'black',pady = 200,font=("Arial", 15))
        lab.pack()

        self.send('won:0')

    def won(self):
        self.pop = Toplevel(self.root)
        self.pop.geometry("450x400")
        self.pop.config(bg = "grey")
        self.pop.resizable(False,False)

        lab = Label(self.pop,text = "YOU  WON",bg = 'grey',fg = 'black',pady = 200,font=("Arial", 15))
        lab.pack()





if __name__ == '__main__':

    root = Tk()
    game = game_working(root)
    root.mainloop()
