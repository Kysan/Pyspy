# pour tester un bot sans le compiler


if __name__ == '__main__':
    import sys
    sys.path[0] += ("\\..\\")

    # je veux charger les 2 fichiers suivant
    from src.Bot import Bot
    from test.config import config

    print(sys.path[0])
    sys.path[0] = sys.path[0][:-4]
    bot = Bot()

    # TODO: token qui devras être généré à la volé durant la création d'un nouveau client
    bot.run(config['bot_token'])
