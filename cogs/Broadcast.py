import discord
from discord.ext import commands, tasks
import os

from discord.ext import commands
from discord.ext.commands import is_owner
server_id = 192537434280427520
autheduser = 192537330509152257


class broadcast(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('The broadcast module has loaded!')
        

    @commands.command(name='Broadcast',
                description="Broadcast a message to any room this bot can access via channel ID",
                brief="Message Broadcast",
                aliases=['broadcast'],
                pass_context=True)
    @commands.has_permissions(administrator=True)
    async def broadcast(self, ctx, channel : int, *, message):
        current_server = ctx.message.guild.id
        author = ctx.author.id
        if current_server == server_id:
            channel = self.client.get_channel(channel)
            await channel.send(message)
            print(f'Broadcast sent\n----------\nUser: {ctx.message.author}\nChannel: {channel}\nMessage: {message}\n----------')
        else: 
            if author == autheduser:
                channel = self.client.get_channel(channel)
                await channel.send(message)
                print(f'Broadcast sent\n----------\n!!FOREIGN SERVER!!User: {ctx.message.author}\nChannel: {channel}\nMessage: {message}\n----------')
            else:
                await ctx.send(f'Sorry, {ctx.message.author}, but you are not authorised to use that command in this server!')

    @broadcast.error
    @commands.has_permissions(manage_messages=True)
    async def broadcast_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please send all required info needed to run this command.\n(Example: 2!broadcast [channel_id] [your_message])")
            


def setup(client):
    client.add_cog(broadcast(client))
