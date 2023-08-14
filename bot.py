import sys
sys.path.insert(0, 'discord.py-self')
import discord
from discord.ext import commands

import json
import tracemalloc
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

#on >ping command send message with pong
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# on >spam command send message x times
@bot.command()
async def spam(ctx, amount: int, *, message):
    for i in range(amount):
        await ctx.send(message)

# on >avatar command send message with avatar url
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

# on >gayrate command do something :smirk:
@bot.command()
async def gayrate(ctx, member: discord.Member):
    print(bot.user, member)

    if bot.user == member or int(member.id) == 864575191915823116:
        await ctx.send(f'{member.mention} is 0% Gay')
    else:
        await ctx.send(f'{member.mention} is {random.randint(30,100)}% Gay')

# on >UPI command send message with UPI
@bot.command()
async def UPI(ctx):
    await ctx.send(f"<@{bot.user.id}> UPI is: rishish-god@fam")

# on >ltc command send message with ltc
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

tos_msg = """
**__TOS OF VCC:__**

# **Must Use These VCC in NITRO PROMO LINKS**

# **DO NOT USE TO BUY 9$/99$ NITRO PLEASE**

# ** PLEASE DO NOT USE THIS VCC TO CLAIM OTHER ITEMS**

**Must Do Screen Recording Before Claiming VCC in Nitro Promo Links**
**Make Sure Account is 1 month old to claim nitro**
**Add address properly , Any mistakes = No replace ( Bcoz its ur fault putting wrong info)**
**1 Hr Warr after providing vcc**
**Validity depends every vcc stock [ask after taking vcc]**
**Payment method cannot be used = No replace/refund bcoz u wasted the vcc using in wrong place]**
**If any error askk , trying again and again will rape the vcc and stop working**

```
Address For VCC:

Card Name : Paradox
Country: Egypt
Adress : Cairo
Adress 2 : Cairo
City : Cairo
State/Province/Region : Cairo
Postal Code :11311
```
"""

# on >tos command send message with tos
@bot.command()
async def tos(ctx):
    await ctx.send(tos_msg)

# on >btcbalance command send message with btc balance 
@bot.command()
async def btcbalance(ctx, address: str):
    url = 'https://blockchain.info/q/addressbalance/'
    r = requests.get(url + address)
    await ctx.send(f"BTC Balance pf {address}: {r.text}")

#on >ltcinfo command send message with ltc info
@bot.command()
async def ltcinfo(ctx, address: str):
    url = 'https://api.blockcypher.com/v1/ltc/main/addrs/' + address
    r = requests.get(url)
    data = r.json()
    message = f"""
    ```    
    LTC Address: {data['address']}
    LTC Balance: {data['balance']}
    LTC Total Received: {data['total_received']}
    LTC Total Sent: {data['total_sent']}
    LTC Unconfirmed Balance: {data['unconfirmed_balance']}
    ```
    """
    await ctx.send(message)

#on >btcinfo command send message with btc info
@bot.command()
async def btcinfo(ctx, address: str):
    url = 'https://api.blockcypher.com/v1/btc/main/addrs/' + address
    r = requests.get(url)
    data = r.json()
    message = f"""
    ```    
    BTC Address: {data['address']}
    BTC Balance: {data['balance']}
    BTC Total Received: {data['total_received']}
    BTC Total Sent: {data['total_sent']}
    BTC Unconfirmed Balance: {data['unconfirmed_balance']}
    ```
    """
    await ctx.send(message)

# on >crypto command send message with crypto prices of btc, eth, ltc
@bot.command()
async def crypto(ctx):
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Clitecoin&vs_currencies=usd'
    r = requests.get(url)
    data = r.json()
    message = f"""
    ```    
    BTC: {data['bitcoin']['usd']}
    ETH: {data['ethereum']['usd']}
    LTC: {data['litecoin']['usd']}
    ```
    """
    await ctx.send(message)


# on >help command send message with help
@bot.command()
async def commands(ctx):
    await ctx.send("""```# Commands:
                   
    >ping
    >spam
    >avatar
    >mute
    >unmute
    >gayrate
    >UPI
    >ltc
    >calc
    >shop
    >tos
    >btcbalance
    >ltcinfo
    >btcinfo
    >help```""")





bot.run(token)
