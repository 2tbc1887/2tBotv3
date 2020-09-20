import discord
from discord.ext import commands, tasks
import os

from discord.ext import commands
from discord.ext.commands import is_owner

server_id = 192537434280427520
autheduser = 192537330509152257

class StatusUpdate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('The status update module has loaded!')
        
    @commands.command(name='StatusUpdate',
                description="Update the status of the bot through command",
                brief="Update bot status",
                aliases=['status'],
                pass_context=True)
    @commands.has_permissions(administrator=True)
    async def statusupdate(self, ctx, *, message):
        current_server = ctx.message.guild.id
        author = ctx.author.id
        print("YEET")
        if current_server == server_id:
            await self.client.change_presence(activity=discord.Game(message))
            await ctx.send(f'Status has been changed to {message}')
            print(f'Status change made:\n----------\nUser: {ctx.message.author}\nMessage: {message}\n----------')
        else: 
            if author == autheduser:
                await ctx.change_presence(activity=discord.Game(message))
                await ctx.send(f'Status has been changed to {message}')
                print(f'Status change made:\n----------\nUser: {ctx.message.author}\nMessage: {message}\n----------')
            else:
                await ctx.send(f'Sorry, {ctx.message.author}, but you are not authorised to use that command in this server!')
##    @statusupdate.error
##    @commands.has_permissions(manage_messages=True)
##    async def broadcast_error(self, ctx, error):
##        if isinstance(error, commands.MissingRequiredArgument):
##            await ctx.send("Please send all required info needed to run this command.\n(Example: 2!status [message])")
                


def setup(client):
    client.add_cog(StatusUpdate(client))
