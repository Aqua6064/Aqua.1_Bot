import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
   channel = bot.get_channel(828213844576305173)
   await channel.send(f'{member} join')

@bot.event
async def on_member_remove(member):
   channel = bot.get_channel(828213881436504084)
   await channel.send(f'{member} leave')

bot.run('ODI4MTg5NTIyOTExMTY2NDg2.YGl9mQ.Eim98uu820pkDNb9wa_pnUObYIc')