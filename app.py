import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='/', intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print('message received from', message)
    if message.content.startswith('hello'):
        if message.author.nick == None:
            await message.channel.send('Hello! {0}'.format(message.author))
        else:
            await message.channel.send('Hello! {0}'.format(message.author.nick))

    await client.process_commands(message)
@client.event
async def on_member_join(member):
    await member.send('Listen here you little bitch...{0}'.format(member.name))
    return


@client.command(help = 'Get yourself sucked off', breif= 'suck')
async def suck(ctx):
    await ctx.channel.send('Sucking...')
    return


client.run(TOKEN);
