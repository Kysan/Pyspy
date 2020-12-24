import discord


async def sendFile(channel, fileName):
    with open(fileName, 'br') as f:
        await channel.send(file=discord.File(f, fileName))
    return
