import sys
sys.path.insert(0, 'discord.py-self')
import discord
from discord.ext import commands

import aiohttp
import asyncio
import json
import re
import tracemalloc
import os
import requests
tracemalloc.start()

from dotenv import load_dotenv

load_dotenv()


token = os.getenv('TOKEN')
prefix = ">"

bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    print("Logged in!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def spam(ctx, amount: int, *, message):
    for i in range(amount):
        await ctx.send(message)

@bot.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar
    await ctx.send(userAvatarUrl)

@bot.command()
async def mute(ctx, member: discord.Member):
    await member.edit(mute=True)

@bot.command()
async def unmute(ctx, member: discord.Member):
    await member.edit(mute=False)



bot.run(token)
