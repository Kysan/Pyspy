# pour tester un bot sans le compiler
from config import config
import sys

if __name__ == '__main__':

    # * pour importer en passant par le dossier parent

    sys.path[0] += ("\\..\\")
    from src.Bot import Bot

    # * print(sys.path[0])
    sys.path[0] = sys.path[0][:-4]

    # * lance le bot depuis le fichier de config
    bot = Bot(config['master_id'], config['prefix'])
    bot.run(config['bot_token'])
