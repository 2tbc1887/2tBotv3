import discord
from discord.ext import commands, tasks
import os

from discord.ext import commands
from discord.ext.commands import is_owner


class CodeCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('The Code command module has loaded!')

    @commands.command(name='code',
                description="Repeat provided string as an embed code",
                brief="Send code",
                aliases=['codes', 'codesend'],
                pass_context=True)
    @commands.has_permissions(administrator=True)
    async def code(self, ctx, *, message):
        current_server = ctx.message.guild.id
        author = ctx.author.id
        if current_server == server_id:
            embed = discord.Embed(
                title='Code', 
                description=f'{message}', 
                colour=discord.Colour.red()
            )
            await ctx.send(embed=embed)
            await ctx.message.delete()
            print(f'Code Sent:\n----------\nUser: {ctx.message.author}\nMessage: {message}\n----------')
        else: 
            if author == autheduser:
                embed = discord.Embed(
                title='Code', 
                description=f'{message}', 
                colour=discord.Colour.red()
                )
                await ctx.send(embed=embed)
                await ctx.message.delete()
                print(f'Code Sent:\n----------\n!!FOREGIN SERVER!!User: {ctx.message.author}\nMessage: {message}\n----------')
            else:
                await ctx.send(f'Sorry, {ctx.message.author}, but you are not authorised to use that command in this server!')
            


def setup(client):
    client.add_cog(CodeCommand(client))
