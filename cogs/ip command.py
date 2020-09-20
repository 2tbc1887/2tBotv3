import discord
from discord.ext import commands, tasks
import os

from discord.ext import commands
from discord.ext.commands import is_owner
from requests import get

server_id = 192537434280427520 #Server ID for identifying our main server
autheduser = 192537330509152257 #Proves 2t is the one sending the command in servers with other admins


class IP(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('The IP command module has loaded!')
    @commands.command(name='IP',
                    description="Get 2t services IP",
                    brief="Server list",
                    aliases=['ip'],
                    pass_context=True)
    @commands.has_permissions(administrator=True)
    async def IP(self, ctx):
        current_server = ctx.message.guild.id
        author = ctx.author.id
        if current_server == server_id:
            embed = discord.Embed(
                colour=discord.Colour.red()
            )
            embed.set_author(name='IP Address')
            ipaddr = get('https://api.ipify.org').text
            embed.add_field(name="Current", value=ipaddr)
            await ctx.send(embed=embed)
            print(f'IP sent\n----------\nUser: {ctx.message.author}\n----------')
        elif current_server == 744847500749439048:
            embed = discord.Embed(
                colour=discord.Colour.red()
            )
            embed.set_author(name='IP Address')
            ipaddr = get('https://api.ipify.org').text
            embed.add_field(name="Current", value=ipaddr)
            await ctx.send(embed=embed)
            print(f'IP sent\n----------\nUser: {ctx.message.author}\n----------')
        else:
            await ctx.send(f'Sorry, {ctx.message.author}, this command is restricted to 2tbc1887s server!')

def setup(client):
    client.add_cog(IP(client))
