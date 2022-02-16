import asyncio
import discord as d
import os
from discord.ext import commands
from discord_components import Button, Select, SelectOption, ComponentsBot, ButtonStyle
import math
import psycopg2
from db_helper import checkT, createT

bot = ComponentsBot('$')

bot.remove_command('help')

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))

@bot.command()
async def help(ctx):
    await ctx.send("+join : register yourself \n+vote : to vote")

@bot.command()
async def create(ctx,table_name):
    table= table_name
    check = checkT(table)
    if check :
        await ctx.send(f"{table} Created")
    else:
        await ctx.send(f"{table} Already Existing ")

@bot.command()
async def createV(ctx):
    
    c = createT()
    if c :
        await ctx.send(f"Created")
    else:
        await ctx.send(f"Already Existing ")



@bot.command()
async def vote(ctx):
    member = ctx.author
    m_channel = await member.create_dm()
    await m_channel.send("test")
    em = d.Embed(title="Test",description="test",color=0x0000FF)
    await m_channel.send(embed=em)
    e = d.Embed(title="Click The Button To Invite Me", color=0x00ff00)
    m_url = "https://www.google.com"
    inv = await m_channel.send(embeds=[e],components=[Button(style=ButtonStyle.URL, label="Invite Me !", url=m_url)])

bot.run(os.environ.get("TOKEN"))
