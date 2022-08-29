import mysql.connector as sql
import random as rand
def pickAuctionPlayer(passw,filename = "players_fifa22", primary_key = "name",ovr = "potential",size = 50,influence = 2):
    do = sql.connect(host = "localhost", user = "root", password = passw, database = "fifadata")
    ci = do.cursor()
    ci.execute(f"desc {filename}")
    datatypes = []
    for i in ci:
        datatypes.append(i[0].lower())
    ci.execute(f"select*from {filename} order by potential desc limit {size}")
    p = list(ci)
    ovrList= []
    for i in p:
        ovrList.append(i[datatypes.index(ovr)]**2)
    pick = rand.random()*sum(ovrList)
    for i in range(len(ovrList)):
        if pick-ovrList[i]>=0:
            pick-=ovrList[i]
        else:
            print(i)
            return p[i]
    print(-1)
    return p[-1]
def team_init(luck,passw,filename = "players_fifa22"):
    pl = []
    op = []
    do = sql.connect(host = "localhost", user = "root", password = passw, database = "fifadata")
    ci = do.cursor()
    formn = [3,3]
    pos = [["LB","RB","CB","CDM","CM","GK"],["LM","RM","CAM","RW","ST","LW","CF"]]
    for k in range(len(formn)):
        s = "select * from players_fifa22 where"
        for p in pos[k]:
            s+=f" bestposition = '{p}' or"
        s = s[:-2]+f"order by rand() limit 50"
        ci.execute(s)
        temp=[]
        line = []
        for j in range(formn[k]):
            pool = 0
            for p in ci:
                temp.append( p)
                pool+=int(p[1])**luck
            num = rand.random()*pool
            for i in range(len(temp)):
                if num-temp[i][1]**luck>=0:
                    num-=temp[i][1]**luck
                else:
                    print(i)
                    t=temp.pop(i)
                    break
            else:
                t = temp.pop(len(temp)-1)
            line.append(t)
        pl.append(line)
    for j in pl:
        for i in j:
            print(i[0],i[1],end = "\t")
        print()
    return pl
