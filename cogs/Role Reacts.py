import discord
from discord.ext import commands, tasks
import os

from discord.ext import commands
from discord.ext.commands import is_owner


class NAMEOFCOMMAND(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('The role react module has loaded!')

    @commands.Cog.listener()
    async def on_raw_reaction_add(payload):
        message_id1 = payload.message_id
        if message_id1 == 710034544975413328:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

            if payload.emoji.name == 'nkoShrug':
                role = discord.utils.get(guild.roles, name='StreamPing')
            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print(f'{member} has joined {role}\n----------')
                else:
                    print("Member not found.")
            else:
                print("Role not found.")


        message_id2 = payload.message_id
        if message_id2 == 710042354245173268:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
            print(guild_id)

            if payload.emoji.name == 'Drew':
                role = discord.utils.get(guild.roles, name='StreamPing')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

                if member is not None:
                    await member.add_roles(role)

                    print(f'{member} has joined {role}\n----------')
                else:
                    print("Member not found.")
            else:
                print("Role not found.")


        message_id3 = payload.message_id
        if message_id3 == 756847794144280597:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
            print(guild_id)

            if payload.emoji.name == 'smug':
                role = discord.utils.get(guild.roles, name='AmongUs')
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

                if member is not None:
                    await member.add_roles(role)

                    print(f'{member} has joined {role}\n----------')
                else:
                    print("Member not found.")
            else:
                print("Role not found.")

################REMOVE#########################

    @commands.Cog.listener()
    async def on_raw_reaction_remove(payload):
        message_id1 = payload.message_id
        if message_id1 == 710034544975413328:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

            if payload.emoji.name == 'nkoShrug':
                role = discord.utils.get(guild.roles, name='StreamPing')
            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print(f'{member} has left {role}\n----------')
                else:
                    print("Member not found.")
            else:
                print("Role not found.")

                
        message_id2 = payload.message_id
        if message_id2 == 710042354245173268:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

            if payload.emoji.name == 'Drew':
                role = discord.utils.get(guild.roles, name='StreamPing')
            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print(f'{member} has left {role}\n----------')
                else:
                    print("Member not found.")
            else:
                print("Role not found.")


        message_id3 = payload.message_id
        if message_id3 == 756847794144280597:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

            if payload.emoji.name == 'smug':
                role = discord.utils.get(guild.roles, name='AmongUs')
            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print(f'{member} has left {role}\n----------')
                else:
                    print("Member not found.")
            else:
                print("Role not found.")
        


def setup(client):
    client.add_cog(NAMEOFCOMMAND(client))
