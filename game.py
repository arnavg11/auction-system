from tkinter import *
import pickle
from PIL import Image,ImageTk
import time


class game_working:
    def __init__(self,root,comp):
        self.comp = comp
        self.comp.eventhand = self.event_handler

        #screen
        self.root = root
        self.root.geometry("1050x750")
        self.root.title("FIFAPROLALU")

        self.root.resizable(False,False)

        self.urteam()

        self.player = None
        self.playing = []
        self.score = 0
        self.selfscore = 0
        self.count_turn = 0
        self.remaining = []


        self.turn = 0
        self.opp_player = None
        self.opp_player_test = None

        self.canvas = Canvas(self.root, width = 1050, height = 650, bg = 'black',relief = 'sunken')
        self.canvas.pack()

        self.canvas.create_rectangle(771,180,1018,310,fill ='black', outline = 'white')

        self.canvas.create_text(1000, 200, anchor='e',text='OPPONENT SCORE', fill="white", font=('Arial 10 '))
        self.canvas.create_text(781, 200, anchor='w',text='YOUR SCORE', fill="white", font=('Arial 10 '))

        self.canvas.create_text(826, 250, anchor='w',text=self.selfscore, fill="white", font=('Arial 15 '))
        self.canvas.create_text(900, 250,text=':', fill="white", font=('Arial 15 '))
        self.canvas.create_text(960, 250, anchor='e',text='0', fill="white", font=('Arial 15 '))

        self.canvas.create_rectangle(471,180,741,310,fill ='black', outline = 'white')

       

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
       
        self.canvas.create_rectangle(29,451,250,470,fill ='black',outline = 'black')
        self.canvas.create_rectangle(29,42,380,65,fill ='black',outline = 'black')
        self.canvas.create_text(30, 460, anchor='w',text='PLAYER HEALTH BAR', fill="white", font=('Arial 12 '))
        player_bar = self.canvas.create_rectangle(30,480,416,505,fill ='green',outline = 'white')
        self.canvas.create_text(30, 50, anchor='w',text='OPPONENT HEALTH BAR AND PLAYER', fill="white", font=('Arial 12 '))
        opponent_bar = self.canvas.create_rectangle(30,10,416,35,fill ='red',outline = 'white')

        #stamina_bar = self.canvas.create_rectangle(30,465,416,475,fill ='purple',outline = 'white')

        with open("team.dat","rb") as file:
                l =[]
           
                t = pickle.load(file)
                for i in range(len(t)):
                    if t[i][0] == self.comp.user:
                        for j in range(1,len(t[i])):
                            l.append(t[i][j][0].upper())

           
                self.f_players = Listbox(self.canvas,width = 27, height = 13,bg = 'black',fg = 'white',font = 'Arial',activestyle = 'none',bd = 2,relief = 'sunken')

                for item in l:
                    self.f_players.insert('end',item)

                def select():
                    selected_name = self.f_players.get(ANCHOR)
                    if selected_name != '':
                        self.card(selected_name)


                   
                select_option1 = Button(self.root, text= 'select' ,bg = 'black',fg = 'white',padx = 76,pady = 15,command = lambda: select(),borderwidth = 0,width = 4)
                select_option1.place(x =803,y =590)
               

               
                self.f_players.place(x = 771, y = 330)

    def urteam(self):
        self.pop = Toplevel(self.root)
        self.pop.geometry("910x670")
        self.pop.config(bg = "black")
        self.pop.resizable(False,False)
        self.pop.title("YOUR TEAM")

        self.canva = Canvas(self.pop, width = 910, height = 670, bg = 'black',relief = 'sunken')
        self.canva.pack()

        length = 30
        width = 30
        count = 0

        with open("team.dat","rb") as file:
           
                t = pickle.load(file)
                for i in range(len(t)):
                    if t[i][0] == self.comp.user:
                        for j in range(1,len(t[i])):
                            count +=1

                            n = t[i][j][0].upper()
                            st = str(t[i][j][5])
                       
                            m1 = t[i][j][2][0].upper()
                            m2 = t[i][j][3][0].upper()
                            m3 = t[i][j][4][0].upper()

                            d1 = str(t[i][j][2][1])
                            d2 = str(t[i][j][3][1])
                            d3 = str(t[i][j][4][1])

                            if count <= 3:

                                self.canva.create_rectangle(length-10,20,length+260,325,fill ='black', outline = 'white')

                       
                                name = self.canva.create_text(length, 30, anchor='w',text=n, fill="white", font=('Arial 12 '))
                                stamina = self.canva.create_text(length+240, 30, anchor='e', text=st, fill="white", font=('Arial 13 '))

                                move1 = self.canva.create_text(length, 130, anchor='w', text=m1, fill="white", font=('Arial 12 '))
                                damage1 = self.canva.create_text(length+240, 130, anchor='e', text=d1, fill="white", font=('Arial 13 '))

                                move2 = self.canva.create_text(length, 160, anchor='w', text=m2, fill="white", font=('Arial 12 '))
                                damage2 = self.canva.create_text(length+240, 160, anchor='e',text=d2, fill="white", font=('Arial 13 '))

                                move3 = self.canva.create_text(length, 190, anchor='w', text=m3, fill="white", font=('Arial 12 '))
                                damage3 = self.canva.create_text(length+240, 190, anchor='e', text=d3, fill="white", font=('Arial 13 '))

                                if count == 3:
                                    length = 30

                            elif count > 3:
                                self.canva.create_rectangle(length-10,345,length+260,650,fill ='black', outline = 'white')

                       
                                name = self.canva.create_text(length, 30+345, anchor='w',text=n, fill="white", font=('Arial 12 '))
                                stamina = self.canva.create_text(length+240, 30+345, anchor='e', text=st, fill="white", font=('Arial 13 '))

                                move1 = self.canva.create_text(length, 130+345, anchor='w', text=m1, fill="white", font=('Arial 12 '))
                                damage1 = self.canva.create_text(length+240, 130+345, anchor='e', text=d1, fill="white", font=('Arial 13 '))

                                move2 = self.canva.create_text(length, 160+345, anchor='w', text=m2, fill="white", font=('Arial 12 '))
                                damage2 = self.canva.create_text(length+240, 160+345, anchor='e',text=d2, fill="white", font=('Arial 13 '))

                                move3 = self.canva.create_text(length, 190+345, anchor='w', text=m3, fill="white", font=('Arial 12 '))
                                damage3 = self.canva.create_text(length+240, 190+345, anchor='e', text=d3, fill="white", font=('Arial 13 '))


                            length += 300
   

        time.sleep(5)
        self.pop.destroy()
       

    def move_buttons(self,player):
        with open("team.dat","rb") as file:
           
                t = pickle.load(file)
                for i in range(len(t)):
                    if t[i][0] == self.comp.user:
                        for j in range(1,len(t[i])):
                            print("players buttons",player.lower(),t[i][j][0])
                            if player.lower() ==  t[i][j][0].lower():
                           
                                self.opp_player = t[i][j][0].upper()

                                self.card(t[i][j][0])
                                self.playing.append(t[i][j][0].upper())
                                damage1 = t[i][j][2][1]
                                damage2 = t[i][j][3][1]
                                damage3 = t[i][j][4][1]

                   
                                self.b1 = Button(self.root, text=t[i][j][2][0],padx = 70,pady = 15,borderwidth = 0,command = lambda: self.health_bar(damage1),width = 6)
                                self.b2 = Button(self.root, text=t[i][j][3][0],padx = 70,pady = 15,borderwidth = 0,command = lambda: self.health_bar(damage2),width = 6)
                                self.b3 = Button(self.root, text=t[i][j][4][0],padx = 70,pady = 15,borderwidth = 0,command = lambda: self.health_bar(damage3),width =6)

                                self.b1.place(x = 30, y = 510)
                                self.b2.place(x = 230, y = 510)
                                self.b3.place(x = 30, y = 575)

                                """self.b1['state'] = DISABLED
                                self.b2['state'] = DISABLED
                                self.b3['state'] = DISABLED"""

                                self.send(f'starting_player:{self.opp_player}')

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

                       
                                name = self.canvas.create_text(486, 350, anchor='w',text=n, fill="white", font=('Arial 12 '))
                                stamina = self.canvas.create_text(726, 350, anchor='e', text=st, fill="white", font=('Arial 13 '))

                                move1 = self.canvas.create_text(486, 450, anchor='w', text=m1, fill="white", font=('Arial 12 '))
                                damage1 = self.canvas.create_text(726, 450, anchor='e', text=d1, fill="white", font=('Arial 13 '))

                                move2 = self.canvas.create_text(486, 480, anchor='w', text=m2, fill="white", font=('Arial 12 '))
                                damage2 = self.canvas.create_text(726, 480, anchor='e',text=d2, fill="white", font=('Arial 13 '))

                                move3 = self.canvas.create_text(486, 510, anchor='w', text=m3, fill="white", font=('Arial 12 '))
                                damage3 = self.canvas.create_text(726, 510, anchor='e', text=d3, fill="white", font=('Arial 13 '))

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
                    self.canvas.create_rectangle(940,240,1000,270,fill = 'black',outline = 'black')
                    self.canvas.create_text(960, 250, anchor='e',text=f'{self.score}', fill="white", font=('Arial 15 '))

                    self.lost()



                else:
                    self.change_player()

            else:  
                self.canvas.create_rectangle(x1,480.5,415,504,fill = 'black',outline = 'black')
       
        elif keyword == 'opp_name_change':

            self.opp_player = value
            self.opp_player_test = self.opp_player
            self.canvas.create_rectangle(30,10,416,35,fill ='red',outline = 'white')
            self.canvas.create_rectangle(420,5,1000,90,fill ='black',outline = 'black')
            self.canvas.create_text(436, 20, anchor='w',text=self.opp_player, fill="white", font=('Arial 15 '))

        elif keyword == 'starting_player':
            self.opp_player = value
            self.opp_player_test = self.opp_player
           
            """self.b1['state'] = NORMAL
            self.b2['state'] = NORMAL
            self.b3['state'] = NORMAL"""

            self.canvas.create_rectangle(30,10,416,35,fill ='red',outline = 'white')
            self.canvas.create_rectangle(420,5,1000,90,fill ='black',outline = 'black')
            opp = self.canvas.create_text(436,20, anchor='w',text=self.opp_player, fill="white", font=('Arial 15 '))

        elif keyword == 'won':
            self.won()

        elif keyword == 'wonround':
            self.playing = []
            self.choose_player()
           
        elif keyword == 'your_score':
            self.selfscore = value
            self.canvas.create_rectangle(820,240,870,270,fill = 'black',outline = 'black')
            self.canvas.create_text(826, 250, anchor='w',text=f'{self.selfscore}', fill="white", font=('Arial 15 '))

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
                            print
