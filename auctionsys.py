import mysql.connector as sql
import random as rand
passw = "4rn4vGU!"
auctioned = []
def pickAuctionPlayer(filename = "players_fifa22", primary_key = "fullname",ovr = "overall",size = 50,influence = 2):
    do = sql.connect(host = "localhost", user = "root", password = passw, database = "fifadata")
    ci = do.cursor()
    ci.execute(f"desc {filename}")
    datatypes = []
    for i in ci:
        datatypes.append(i[0].lower())

    if len(auctioned)==0:
        execstr = f"select*from {filename} order by overall desc limit {size}"
    else:
        execstr = f"select * from {filename} where "
        for i in auctioned:
            execstr+=f"not fullname = '{i}' and"
        execstr = execstr[:-3]+ f"order by overall desc limit {size}"
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
