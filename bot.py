import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = '!')


@bot.event
async def on_ready():
    print('Bot is online')


@bot.command()
async def ping(ctx):
    await ctx.send('Pong :ping_pong:')


@bot.command()
async def say(ctx, *, mesasge=None):
    await ctx.send(mesasge)

bot.run('Nzc0NzE2Mzc2NDU1NTc3NjMx.X6b02Q.f9pa9ROh7ZEEeTPLWGXqF6ACuR4')