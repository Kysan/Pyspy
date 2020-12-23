import random


def randomString(charNb=6):
    stringbuilder = ""
    for x in range(charNb):
        stringbuilder += random.choice("1234567890abcdef")
    return stringbuilder
