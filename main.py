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
    await ctx.send("Use '$youtube [link] [mp3/mp4]' . Just make sure the embed isn't hidden!")


@bot.command()
async def vote(ctx):
    

bot.run(os.environ.get("TOKEN"))
