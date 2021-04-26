import discord

class MyClient(discord.Client):
  async def on_ready(self):
    print(discord.__version__)
    print('Logged on as', self.user)
    varStatus = "Text Status"
    varEmoji = "🐻"

    #varActivity = discord.Activity(type=discord.ActivityType.custom, name=varEmoji+" "+varStatus, state=varEmoji+" "+varStatus)
    varActivity = discord.CustomActivity(name=varStatus, state=varStatus, emoji=discord.PartialEmoji(name=varEmoji))
    await client.change_presence(status=discord.Status.online, activity=varActivity)

  async def on_message(self, message):
    # don't respond to ourselves
    if message.author == self.user:
      return

    if message.content == 'ping':
      await message.channel.send('pong')

client = MyClient()
client.run("TOKEN-HERE", bot=False)
