import asyncio
import discord as d
import os
from discord.ext import commands
from discord_components import Button, Select, SelectOption, ComponentsBot, ButtonStyle
import math

bot = ComponentsBot('$')

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
    em = d.embed(title="Test",description="test",color=0x0000FF)
    await m_channel.send(embed=em)

bot.run(os.environ.get("TOKEN"))
