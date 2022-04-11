import csv
import mysql.connector as sql
import threading as thr
from time import time as t
passw = "4rn4vGU!"
do = sql.connect(host = "localhost", user = "root",password = passw)
ci = do.cursor()
ci.execute("create database if not exists fifadata")
ci.execute("use fifadata")
def maketable(filename,primary_key = "FullName",additional = ")"):
    csvr = csv.reader(open(filename+".csv"))
    indexes = next(csvr)
    sample = next(csvr)
    s = f"create table if not exists {filename}("
    for i in range(len(indexes)):
        if sample[i].isdigit():
            s+=f"{indexes[i]} int"
        elif sample[i].lower() in ["true","false"]:
            s+=f"{indexes[i]} boolean"
        else:
            s+=f"{indexes[i]} varchar(100)"
        if indexes[i]==primary_key:
            s+="primary key"
        s+=","
    s = s[:-1]
    s+=additional
    ci.execute(s)
    print(f"table {filename} successfully created")
def loadData(filename):
    ci.execute(f"delete from {filename}")
    ci.execute(f"desc {filename}")
    datatypes = []
    for i in ci:
        datatypes.append(i[1])
    csvr = csv.reader(open(filename+".csv"))
    next(csvr)
    for i in csvr:
        s = f"insert into {filename} values("
        for j in range(len(datatypes)):
            if datatypes[j] == b'int':
                if i[j] == "":
                    s+="0"
                else:
                    s+=f"{eval(i[j])}"
            elif datatypes[j] ==b'tinyint(1)':
                s+=f"{bool(i[j])}"
            else:
                s+=f'"{i[j]}"'
            s+=","
        s = s[:-1]
        s+=")"
        try:
            ci.execute(s)
        except sql.Error as e:
            pass
        do.commit()
    print(f"data loaded into {filename}")
p = t()
maketable("players_fifa22")
loadData("players_fifa22")
maketable("players_22")
loadData("players_22")
maketable("teams_fifa22")
loadData("teams_fifa22")
print(t()-p)
