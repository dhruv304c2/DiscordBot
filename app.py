import string

import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents= intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print('message received from {0.author}', message)
    if message.content.startswith('hello'):
        await message.channel.send('Hello! {0}'.format(message.author))
        return

client.run(TOKEN);