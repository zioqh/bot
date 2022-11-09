import discord 
from discord.ext import commands

prefix = '.'
client = discord.Bot(prefix=prefix, intents=discord.Intents.all())

@client.event
async def on_ready():
  print("\n\ngit bot is on!\n\n")
  
client.run(yourtoken)
