#Features to implement:
#Rule embed on join?
######Import modules######
import os
import discord #Import discord module
from dotenv import load_dotenv #??
import random
from requests import get
import time
##########################
load_dotenv() #Load variables to set up the bot
TOKEN = os.getenv('DISCORD_TOKEN')#Get token
GUILD = os.getenv('DISCORD_GUILD')#Get guild id
from discord.ext import commands, tasks #Import commands
client = commands.Bot(command_prefix="2!")#Set up prefix
#client.remove_command('help')#Overwrite the default help command, not yet in effect
server_id = 192537434280427520 #Server ID for identifying our main server
autheduser = 192537330509152257 #Proves 2t is the one sending the command in servers with other admins

@client.event #Show wake messages
async def on_ready():
    await client.change_presence(activity=discord.Game("a breakdown | 2!help"))
    print(f'{client.user} has connected to Discord!')
    print(f'{client.user} is connected to the following guild:\n')
    for guild in client.guilds:#Repeat for each guild the client is connected to
        print(f'{guild.name}(id: {guild.id})')#Print the guild and id
        if guild.name == GUILD:
            break
    print('\n\n\n')

@client.command(pass_context=True)#Admin help command
@commands.has_permissions(administrator=True)
async def adminhelp(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour=discord.Colour.red()
    )

    embed.set_author(name='Admin Commands')
    embed.add_field(name='Status Update', value='Update the status of the bot\nUsage: 2!status [Status]')
    embed.add_field(name='Stream Status', value="Update the streaming status of the bot\nUsage: 2!streamstatus [Game]\nPlease note this command only links to 2tbc1887's channel")
    embed.add_field(name='Broadcast', value="Send a broadcast to any channel the bot can access with the channel ID\nUsage: 2!broadcast [Channel ID] [Message]")
    embed.add_field(name='Servers', value='Returns a list of the servers the bot is connected to at the current time. Mostly for debug purposes\nUsage: 2!servers')
    embed.add_field(name='IP Address', value='Sends the current IP of 2tbc1887 hosted services\nUsage: 2!ip')

    await ctx.send(author, embed=embed)

@client.command(name="embedsend")
async def fuckit(ctx):
    embed = discord.Embed(
        title='Code', 
        description='KYJTYQ', 
        colour=discord.Colour.red()
    )
    await ctx.send(embed=embed)
#######################################################################################################################

@client.command(
    name="About",
    description="Gives information about the bot, including it's version. When I remember to update this field.",
    brief="Info about the bot",
    aliases=['about', 'info', 'ver'],
    pass_context=True)
async def about(ctx):
    await ctx.send("2tBot re-write v3, version 1")
    print(f'About used:\n----------\nUser: {ctx.message.author}\n----------')

################COGS#####################

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
