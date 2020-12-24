# pour tester un bot sans le compiler
from config import config

if __name__ == '__main__':
    import sys
    sys.path[0] += ("\\..\\")

    # je veux charger les 2 fichiers suivant
    from src.Bot import Bot

    # print(sys.path[0])
    sys.path[0] = sys.path[0][:-4]
    bot = Bot()

    bot.run(config['bot_token'])
