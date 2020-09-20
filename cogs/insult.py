import discord
from discord.ext import commands, tasks
import os

from discord.ext import commands
from discord.ext.commands import is_owner
import random


class insult(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('The role react module has loaded!')
        

    @commands.command(
    name="InsultMe",
    description="Will insult anyone without mercy",
    brief="Insults you",
    aliases=['insultme', 'insult'],
    pass_context=True)
    async def insultme(self, ctx):
            possible_responses = [
                'Your family tree LGBT', "Your parents come from Thottage Cottage",
                "Your ancestors incestors", "Your Granny Tranny",
                "Your sister a mister", "Your brother is your mother",
                "You come from The Thottage Cottage", "You come from the Hoe Home",
                "no u+1", "Your mum gay", "Your moe a hoe",
                "Hippity Hoppity you are now my Property",
                "Your mother is your Brother", "Hippity Hoppity your property is mine :)"
            ]
            insultmsg = random.choice(possible_responses)
            await ctx.send(insultmsg + ", " + ctx.message.author.mention)
            print(f'Insult command used:\n----------\nUser: {ctx.message.author}\nInsult: {insultmsg}\n----------')
        


def setup(client):
    client.add_cog(insult(client))
