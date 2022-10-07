import pickle
import random as r

class team_creation:
    def __init__(self,root,comp,team):
        #moves-

        print("my team is: ",team)

        print("tema creating")

        final_teams = []

        destruction = [30,50,70,100,130,160]

        #defending
        d =[['block'],['block','sidepush'],['tackle','sidepush'],['tackle','sidetackle','powerblock'],['supersidetackle','ultimatetackle','powershoulderpush'],['destructivetackover']]


        #attack

        a = [['dribble'],['stepover','bodyfeint'],['bodyfeint','rabona'],['rabona','rainbow','elastico'],['rabona','elastico','nutmeg'],['ghost body fake','chip','nutmeg','superelastico']]


        #shooting

        s = [['powershot','curve'],['placement','curve','head'],['paneka','powershot','topbin'],['powerhead','paneka','supershot','swerve']]

        #distribution of moves


        for i in range(len(team)):
            player_moves=[]
            for x in range(1,len(team[i])):
                if team[i][x][2] == 'LM' or team[i][x][2] == 'RM' or team[i][x][2] == 'CAM' or team[i][x][2] == 'RW' or team[i][x][2] == 'ST' or team[i][x][2] == 'LW' or team[i][x][2] == 'CF':
                    if team[i][x][1] <= 100 and team[i][x][1] >=80:
                        l1 = r.randint(0,3)
                        l2 = r.randint(0,2)
                        l3 = r.randint(0,3)
                        
                        m1=a[5][l1]
                        m2=a[4][l2]
                        s1 = s[3][l3]
                        
                        l = [team[i][x][0],team[i][x][2],[m1,160],[m2,130],[s1,160],200]
                        player_moves.append(l)
                        

                    elif team[i][x][1] < 80 and team[i][x][1] >=70:
                        l1 = r.randint(0,2)
                        l2 = r.randint(0,2)
                        l3 = r.randint(0,2)
                        
                        m1=a[4][l1]
                        m2=a[3][l2]
                        s1 = s[2][l3]

                        l = [team[i][x][0],team[i][x][2],[m1,130],[m2,100],[s1,130],160]
                        player_moves.append(l)


                    elif team[i][x][1] < 70 and team[i][x][1] >= 50:
                        l1 = r.randint(0,2)
                        l2 = r.randint(0,1)
                        l3 = r.randint(0,2)
                        
                        m1=a[3][l1]
                        m2=a[2][l2]
                        s1 = s[1][l3]

                        l = [team[i][x][0],team[i][x][2],[m1,100],[m2,70],[s1,100],100]
                        player_moves.append(l)

                        
                    elif team[i][x][1] < 50:
                        l1 = r.randint(0,1)
                        l3 = r.randint(0,1)
                        
                        m1=a[1][l1]
                        m2=a[0]
                        s1 = s[0][l3]

                        l = [team[i][x][0],team[i][x][2],[m1,50],[m2,30],[s1,70],70]
                        player_moves.append(l)
                

                elif team[i][x][2] == 'LB' or team[i][x][2] == 'RB' or team[i][x][2] == 'CDM' or team[i][x][2] == 'CM' or team[i][x][2] == 'GK' or team[i][x][2] == 'CB' :
                    if team[i][x][1] <= 100 and team[i][x][1] >=80:
                        l2 = r.randint(0,2)
                        l3 = r.randint(0,3)
                        
                        m1=d[5][0]
                        m2=d[4][l2]
                        s1 = s[3][l3]

                        l = [team[i][x][0],team[i][x][2],[m1,160],[m2,130],[s1,160],200]
                        player_moves.append(l)
                        

                    elif team[i][x][1] < 80 and team[i][x][1] >=70:
                        l1 = r.randint(0,2)
                        l2 = r.randint(0,2)
                        l3 = r.randint(0,2)
                        
                        m1=d[4][l1]
                        m2=d[3][l2]
                        s1 = s[2][l3]

                        l = [team[i][x][0],team[i][x][2],[m1,130],[m2,100],[s1,130],160]
                        player_moves.append(l)


                    elif team[i][x][1] < 70 and team[i][x][1] >=50:
                        l1 = r.randint(0,2)
                        l2 = r.randint(0,1)
                        l3 = r.randint(0,2)
                        
                        m1=d[3][l1]
                        m2=d[2][l2]
                        s1 = s[1][l3]

                        l = [team[i][x][0],team[i][x][2],[m1,100],[m2,70],[s1,100],100]
                        player_moves.append(l)


                    elif team[i][x][1] < 50:
                        l1 = r.randint(0,1)
                        l3 = r.randint(0,1)
                        
                        m1=d[1][l1]
                        m2=d[0]
                        s1 = s[0][l3]

                        l = [team[i][x][0],team[i][x][2],[m1,50],[m2,30],[s1,70],70]
                        player_moves.append(l)

            player_moves.insert(0,team[i][0])
            final_teams.append(player_moves)


            with open("team.dat","wb") as file:
                pickle.dump(final_teams,file)
                

