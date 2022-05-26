import socket as sck
import threading as thr

"""
temp = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
temp.connect(("8.8.8.8",9000))
myip = temp.getsockname()[0]"""
import tkinter as tk

myip = "0.0.0.1"


def convertih(ipv4=myip):
    return "".join([hex(int(i))[-2:] for i in ipv4.split(".")])


def converthi(ip4_e):
    ip = ""
    for i in range(4):
        if ip4_e[i * 2] == "x":
            ip += str(int("0" + ip4_e[i * 2 + 1], 16))[:-2]
        else:
            ip += str(int(ip4_e[i * 2 : i * 2 + 2], 16))
        ip += "."
    ip = ip[:-1]
    return ip


class Client:
    def __init__(self):
        self.socket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
        self.ip = None

    def read(self):
        while True:
            print(self.socket.recv(4096))

    def write(self, msg):
        print(msg.encode())
        self.socket.send(msg.encode())

    def setip(self, ip):
        self.ip = ip
        try:
            self.socket.connect((ip, 6789))
            t = thr.Thread(target=self.read)
            t.start()
            return True
        except:
            return False


x = Client()
x.setip("localhost")
x.write("init")
thr.Thread(target = x.read()).start()
