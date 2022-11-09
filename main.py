import discord 
from discord.ext import commands

#rolechannelid = the channel you want reaction roles in, it will send a msg to there on event #1.
#roleid = the id of the role you want to give.
#yourtoken = your bots token not discord token

prefix = '.'
client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

#event #1
@client.event
async def on_ready():
  print("\n\ngit bot is on!\n\n")
  channel = client.get_channel(rolechannelid)
  text = "React for roles!"
  await channel.purge(limit=10)
  channel = await channel.send(text)
  await channel.add_reaction('🥳')
  await channel.add_reaction('😀')

#command ping
@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def ping(ctx):
  await ctx.send(f"{client.latency} is my ping!")
  
#test if reaction that was done was in the reaction role channel
@client.event
async def on_reaction_add(reaction, user):
  channel = client.get_channel(rolechannelid)
  if reaction.message.channel.id != channel.id:
    return
  if reaction.emoji == '🥳':
    role = user.guild.get_role(yourroleid)
    await user.add_roles(role)
  if reaction.emoji == '😀':
    role = user.guild.get_role(yourroleid)
    await user.add_roles(role)
    
#test if reaction that was done was in the reaction role channel    
@client.event
async def on_reaction_remove(reaction, user):
  channel = client.get_channel(rolechannelid)
  if reaction.message.channel.id != channel.id:
    return
  if reaction.emoji == '🥳':
    role = user.guild.get_role(yourroleid)
    await user.remove_roles(role)
  if reaction.emoji == '😀':
    role = user.guild.get_role(yourroleid)
    await user.remove_roles(role)
    
#ping error for ping command
@ping.error
async def ping_error(ctx, error):
  if isinstance(error, commands.errors.CommandOnCooldown):
    await ctx.send(f"Please try again in {error.retry_after:.2f} seconds!")




  
client.run(yourtoke)
