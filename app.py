import discord
import os
# .env
DISORD_TOKEN = 'MTAyMTc3NDA4ODk1NzYxMjA5Mw.GAPrij.WFBhEUY5KPR0gy7VnOHm7vcwE8EmjVvArqj87M'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv(DISORD_TOKEN));