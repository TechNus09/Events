import asyncio
import discord as d
import os
from discord.ext import commands

bot = commands.Bot(command_prefix = '$')

bot.remove_command('help')

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))

@bot.command()
async def help(ctx):
    await ctx.send("+join : register yourself \n+vote : to vote")


@bot.command()
async def vote(ctx):
    member = ctx.author
    m_channel = await member.create_dm()
    await m_channel.send("test")

bot.run(os.environ.get("TOKEN"))
