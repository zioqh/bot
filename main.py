import discord 
from discord.ext import commands

prefix = '.'
client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

@client.event
async def on_ready():
  print("\n\ngit bot is on!\n\n")
  
client.run(yourtoken')
