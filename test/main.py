# pour tester un bot sans le compiler
from .config import config

if __name__ == '__main__':
    import sys
    sys.path[0] += ("/..")
    # print(sys.path[0])
    from src.Bot import Bot
    sys.path[0] = sys.path[0][:-3]
    bot = Bot()
    # token qui devras être généré à la volé durant la création d'un nouveau client
    bot.run(config['bot_token'])
