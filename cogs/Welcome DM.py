import discord
from discord.ext import commands, tasks
import os

from discord.ext import commands
from discord.ext.commands import is_owner
from requests import get

server_id = 192537434280427520 #Server ID for identifying our main server
autheduser = 192537330509152257 #Proves 2t is the one sending the command in servers with other admins


class WelcomeDM(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('The welcome DM module has loaded!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        ####current_server = ctx.guild.id
        #if current_server == server_id:
        await member.create_dm() #Create a DM chat with the new user
        await member.dm_channel.send(f"Heya, {member.name}! Welcome to 2t and TheWhatGuy's special hell! \nPlease look over these rules:\n1. No NSFW content - keep it PG\n2. Keep content to its respective channel. If you don't know where it goes, it goes in other-spam.\n3. Staff have final say, if you feel they are abusing power, message 2tbc1887 or TheWhatGuy\n**These are the rules as of the latest update of this bot** ```20/09/2020```\n**Please check the rules channel to stay up to date.**\n*To obtain your roles, visit the roles channel.* We have game groups, as of current: Among Us\nI hope you enjoy your stay here!")
        print(f'User DM sent:\n----------\nUser: {member.name}\n----------')



def setup(client):
    client.add_cog(WelcomeDM(client))


