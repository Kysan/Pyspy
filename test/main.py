# pour tester un bot sans le compiler

if __name__ == '__main__':
    import sys
    sys.path[0] += ("/..")
    # print(sys.path)
    from src.Bot import Bot
    sys.path[0] = sys.path[0][:-3]
    bot = Bot()
    # token qui devras être généré à la volé durant la création d'un nouveau client
    bot.run('NzkxNDA4MDQ2MTM1NDQzNTI4.X-OuLQ.q16bcOZ7iHJStTJOd8h_30FCKC8')
