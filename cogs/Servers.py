import discord
from discord.ext import commands, tasks
import os

from discord.ext import commands
from discord.ext.commands import is_owner

server_id = 192537434280427520
autheduser = 192537330509152257

class Servers(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('The server list module has loaded!')

    @commands.command(name='Servers',
                description="List the servers the bot is connected to",
                brief="Server list",
                aliases=['servers', 'serverlist', 'serverslist'],
                pass_context=True)
    @commands.has_permissions(administrator=True)
    async def servers(self, ctx):
        current_server = ctx.message.guild.id
        author = ctx.author.id
        if current_server == server_id:
            serverno = 0
            embed = discord.Embed(
                colour=discord.Colour.red()
            )
            embed.set_author(name='Servers')
            for guild in self.client.guilds:#Repeat for each guild the client is connected to
                embed.add_field(name=str(serverno + 1), value=str(guild.name))#Add each guild to the list
            await ctx.send(embed=embed)
            print(f'Servers listed\n----------\nUser: {ctx.message.author}\n----------')
        else: 
            if author == autheduser:
                serverno = 0
                embed = discord.Embed(
                    colour=discord.Colour.red()
                )
                embed.set_author(name='Servers')
                for guild in self.client.guilds:#Repeat for each guild the client is connected to
                    embed.add_field(name=str(serverno + 1), value=str(guild.name))#Add each guild to the list
                await ctx.send(embed=embed)
                print(f'Servers listed\n----------\nUser: {ctx.message.author}\n----------')
            else:
                await ctx.send(f'Sorry, {ctx.message.author}, but you are not authorised to use that command in this server!')  
            


def setup(client):
    client.add_cog(Servers(client))
