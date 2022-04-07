import csv
import mysql.connector as sql
from time import time as t
do_temp = sql.connect(host = "localhost", user = "root",password = "4rn4vGU!")
ci_temp = do_temp.cursor()
ci_temp.execute("create database if not exists fifadata")
do = sql.connect(host = "localhost", user = "root",password = "4rn4vGU!",database = "fifadata")
ci = do_temp.cursor()
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
    csvr = csv.reader(open(filename+".csv"))
    next(csvr)
    for i in csvr:
        s = f"insert into {filename} values("
        prev = t()
        for j in i:
            if j.isdigit():
                if j == "":
                    s+="0"
                else:
                    s+=f"{int(j)}"
            elif j.lower() in ["true","false"]:
                s+=f"{bool(j)}"
            else:
                s+=f'"{j}"'
            s+=","
        s = s[:-1]
        s+=")"
        if t()-prev>=1:
            print("end")
            break
        print(s)
        print()
        ci.execute(s)
maketable("players_fifa22")
loadData("players_fifa22")
