import mysql.connector as sql
passw = "4rn4vGU!"
auctioned = ["Lionel Messi"]
def pickAuctionPlayer(filename = "players_fifa22", primary_key = "fullname"):
    do = sql.connect(host = "localhost", user = "root", password = passw, database = "fifadata")
    ci = do.cursor()
    if len(auctioned)==0:
        exec = f"select*from {filename} order by overall desc limit 50"
    else:
        exec = f"select * from {filename} where "
        for i in auctioned:
            exec+=f"not fullname = '{i}' and"
        exec = exec[:-3]+ "order by overall desc limit 50"
    ci.execute(exec)

    p = list(ci)
    
pickAuctionPlayer()
