import csv
import mysql.connector as sql
import threading as thr
from time import time as t
def maketable(filename,primary_key = "Name",additional = ")"):
    passw = "deens"
    do = sql.connect(host = "localhost", user = "root",password = passw)
    ci = do.cursor()
    ci.execute("create database if not exists fifadata")
    ci.execute("use fifadata")
    csvr = csv.reader(open(filename+".csv",encoding='utf8'))
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
    print(s)
    ci.execute(s)
    print(f"table {filename} successfully created")
    do.commit()
def loadData(filename):
    passw = "deens"
    do = sql.connect(host = "localhost", user = "root",password = passw)
    ci = do.cursor()
    ci.execute("use fifadata")
    ci.execute(f"delete from {filename}")
    ci.execute(f"desc {filename}")
    datatypes = []
    for i in ci:
        datatypes.append(i[1])
    print(datatypes)
    csvr = csv.reader(open(filename+".csv",encoding = "utf8"))
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
print(t()-p)
