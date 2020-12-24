import discord
from .config import config
from .utils import takeScreenshot


class Bot(discord.Client):
    async def on_ready(self):
        print('bot started has', self.user)

    async def on_message(self, message):
        print(f'{message.author.id} : {message.content}')
        if message.author.id != config['master_id'] or not message.content.startswith(config['prefix']):
            return

        command = message.content[1:]
        await message.channel.send(command)
        if command == 'screenshot':
            file_path = takeScreenshot()
            with open(file_path, 'br') as file:
                await message.channel.send(file=file_path)
