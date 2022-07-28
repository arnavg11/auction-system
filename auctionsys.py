import mysql.connector as sql
import random as rand
passw = "deens"
auctioned = []
def pickAuctionPlayer(filename = "players_fifa22", primary_key = "name",ovr = "potential",size = 50,influence = 2):
    do = sql.connect(host = "localhost", user = "root", password = passw, database = "fifadata")
    ci = do.cursor()
    ci.execute(f"desc {filename}")
    datatypes = []
    for i in ci:
        datatypes.append(i[0].lower())

    if len(auctioned)==0:
        execstr = f"select*from {filename} order by potential desc limit {size}"
    else:
        execstr = f"select * from {filename} where "
        for i in auctioned:
            execstr+=f"not fullname = '{i}' and"
        execstr = execstr[:-3]+ f"order by potential desc limit {size}"
    ci.execute(execstr)
    p = list(ci)
    ovrList= []
    for i in p:
        ovrList.append(i[datatypes.index(ovr)]**2)
    pick = rand.random()*sum(ovrList)
    for i in range(len(ovrList)):
        if pick-ovrList[i]>=0:
            pick-=ovrList[i]
        else:
            auctioned.append(p[i])
            return dict(zip(datatypes, p[i]))
    auctioned.append(p[-1])
    return dict(zip(datatypes, p[-1]))
def team_init(filename = "players_fifa22"):
    pl = []
    op = []
    do = sql.connect(host = "localhost", user = "root", password = passw, database = "fifadata")
    ci = do.cursor()
    ci.execute(f"desc {filename}")
    datatypes = []
    for i in ci:
        datatypes.append(i[0].lower())
    formn = [3,3]
    pos = [["LB","RB","CB","CDM","CM","GK"],["LM","RM","CAM","RW","ST","LW","CF"]]
    for i in range(2):
        s = "select * from players_fifa22 where"
        for p in pos[i]:
            s+=f" bestposition = '{p}' or"
        s = s[:-2]+f"order by rand() limit {formn[i]}"
        ci.execute(s)
        t=[]
        for p in ci:
            t.append(dict(zip(datatypes, p)))
        pl.append(t)
    for j in pl:
        for i in j:
            print(i["name"],i["potential"],end = "\t")
        print()
    

    return pl
print(pickAuctionPlayer())
