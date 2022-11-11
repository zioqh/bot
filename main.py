#message counter + level system.
#you need 3 files:
#messages.json
#users.json
#levels.json

import discord
from discord.ext import commands
import emoji
import typing
import json
import random 

prefix = '.'
client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

#yourtoken = your bots token.


@client.event
async def on_ready():
  print(f"\n\nPrefix: {prefix}\nLogged in as: {client.user}")


@client.event
async def on_message(message):
  ri = random.randint(1, 5)
  if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, ri)
        await level_up(users, message.author, message)
   
        with open('users.json', 'w') as f:
            json.dump(users, f)
          
        with open('messages.json', 'r') as f:
            users = json.load(f)
          
        await update_messages(users, message.author)
        await add_msgs(users, message.author, 1)
    
        with open('messages.json', 'w') as f:
            json.dump(users, f)


@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open('users.json', 'w') as f:
        json.dump(users, f)
      
    with open('messages.json', 'r') as f:
        users = json.load(f)

    await update_messages(users, member)

    with open('messages.json', 'w') as f:
        json.dump(users, f)




async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp

async def add_msgs(users, user, msgs):
    users[f'{user.id}']['messages'] += msgs
  
async def level_up(users, user, message):
    with open('levels.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end

@client.command()
async def level(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'You are currently level **{lvl}**.')
    else:
        id = member.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'{member} is currently level **{lvl}**.')

@client.command()
async def xp(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['experience']
        await ctx.send(f'You are currently at **{lvl}** xp.')
    else:
        id = member.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['experience']
        await ctx.send(f'{member} is currently at **{lvl}** xp.')



async def update_messages(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['messages'] = 0


@client.command()
async def messages(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('messages.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['messages']
        await ctx.send(f'You currently have **{lvl}** messages.')
    else:
        id = member.id
        with open('messages.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['messages']
        await ctx.send(f'{member} currently has **{lvl}** messages.')


client.run(yourtoken)
