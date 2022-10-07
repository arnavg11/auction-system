import pickle

with open("team.dat","rb") as file:
        t = pickle.load(file)
        print(t)