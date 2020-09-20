import discord
from discord.ext import commands, tasks
import os

from discord.ext import commands
from discord.ext.commands import is_owner
import random


class insultgen(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('The role react module has loaded!')
        

    @commands.command(
    name="InsultMegen",
    description="Will insult anyone without mercy",
    brief="Randomly generated insults",
    aliases=['insultmegen', 'insultgen', 'Insultmegen'],
    pass_context=True)
    async def insultmegen(self, ctx):
        possible_responses1 = ['smallest', 'biggest', 'weirdest', 'dumbest', 'drunkest', 'thottiest']
        possible_responses2 = ['thot of them all', "accident", 'dumbass', 'child']
        insultmsg = (random.choice(possible_responses1) + ' ' + random.choice(possible_responses2))
        await ctx.send("You are the " + insultmsg + ", " + ctx.message.author.mention)
        print(f'Insult generator used:\n----------\nUser: {ctx.message.author}\nInsult generator: {insultmsg}\n----------')
        


def setup(client):
    client.add_cog(insultgen(client))
