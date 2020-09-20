import discord
from discord.ext import commands, tasks
import os

from discord.ext import commands
from discord.ext.commands import is_owner
import random


class ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('The role react module has loaded!')

    @commands.command(name = '8ball',
                    description="Answers with some bullshit based on 2t's magical demon powers...",
                    brief="Bullshit and demon powers",
                    pass_context=True)
    async def eight_ball(self, ctx):
        possible_responses = [
                'That is a resounding no',
                "It isn't likely",
                "Unfortunately... No",
                "Too hard to tell",
                "It is possible",
                "Definitely",
            ]
        ranmsg = random.choice(possible_responses)
        await ctx.send(ranmsg + ", " + ctx.message.author.mention)
        print(f'8ball used:\n----------\nUser: {ctx.message.author}\nResponse: {ranmsg}\n----------')
        


def setup(client):
    client.add_cog(ball(client))
