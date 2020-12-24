from .Utils import screenshot, fileHandler
import discord
from .config import config


class Bot(discord.Client):
    def __init__(self, master_id, prefix)
    self.master_id = master_id
    self.prefix = prefix
    super().__init__()

    async def on_ready(self):
        print('bot started has', self.user)

    async def on_message(self, message):
        print(f'{message.author.id} : {message.content}')
        if message.author.id != master_id or not message.content.startswith(config['prefix']):
            return

        command = message.content[len(self.prefix):]

        if command == 'screenshot':
            workingMsg = await message.channel.send("Executing...")
            fileName = screenshot.takeScreenshot()
            with open(fileName, 'br') as f:
                await message.channel.send(file=discord.File(f, fileName))
            fileHandler.deleteFile(fileName)
            await workingMsg.delete()
