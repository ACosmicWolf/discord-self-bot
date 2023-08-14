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


import random


with open('config/config.json') as f:
    config = json.load(f)
    token = config['token']
    prefix = config['prefix']

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

# mute user
@bot.command()
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
    await ctx.send(f'{member.mention} has been muted')

# unmute user
@bot.command()
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
    await ctx.send(f'{member.mention} has been unmuted')

@bot.command()
async def gayrate(ctx, member: discord.Member):
    # check if member is the bot
    if member == bot.user:
        await ctx.send(f'{member.mention} is 0% Gay')
    else:
        await ctx.send(f'{member.mention} is {random.randint(30,100)}% Gay')

@bot.command()
async def UPI(ctx):
    await ctx.send(f"<@{bot.user.id}> UPI is: rishish-god@fam")

@bot.command()
async def ltc(ctx):
    await ctx.send(f"<@{bot.user.id}> LTC is: LhBvQWcygiPKoYQtzneZADi4nfQp2z8JjY")

# simple calculator
@bot.command()
async def calc(ctx, num1: int, op, num2: int):
    if op == "+":
        await ctx.send(f"{num1} + {num2} = {num1 + num2}")
    elif op == "-":
        await ctx.send(f"{num1} - {num2} = {num1 - num2}")
    elif op == "*":
        await ctx.send(f"{num1} * {num2} = {num1 * num2}")
    elif op == "/":
        await ctx.send(f"{num1} / {num2} = {num1 / num2}")
    else:
        await ctx.send("Invalid operator")

# on >shop command send message with server link
@bot.command()
async def shop(ctx):
    await ctx.send("https://discord.gg/WsuEQQM4Sb")

bot.run(token)
