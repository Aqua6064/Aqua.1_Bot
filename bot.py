import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
   channel = bot.get_channel(828163823939616779)
   await channel.send(f'{member} join')

@bot.event
async def on_member_remove(member):
   channel = bot.get_channel(828163823939616779)
   await channel.send(f'{member} leave')

@bot.command()
async def ping(ctx):
   await ctx.send(f'{round(bot.latency*1000)} (ms)')

bot.run('ODI4MTg5NTIyOTExMTY2NDg2.YGl9mQ.Eim98uu820pkDNb9wa_pnUObYIc')