import sys

sys.path.insert(0, 'discord.py-self')
import discord
from discord.ext import commands
import os

import json
import tracemalloc
import requests

tracemalloc.start()

import random

from bs4 import BeautifulSoup

token = os.getenv("TOKEN")

with open('config/config.json') as f:
  config = json.load(f)
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
async def avatar(ctx, *, avamember: discord.Member = None):
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
  await ctx.send(f"<@{bot.user.id}> LTC is: LhBvQWcygiPKoYQtzneZADi4nfQp2z8JjY"
                 )


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

tos_basic_msg = """
**__NITRO BASIC LYF TOS__**
**[+] WE PROVIDE LYF WARRANTY IN OUR NITRO GIFTLINK..**
**[+] N1tr0 gift link = no autoclaim warranty**
**[+] IF OUR NITRO GETS REVOKE THEN YOU MUST PROVIDE SOME PROOFS MENTIONED BELOW:-**

**[+] RECORD A VIDEO WHILE CLAIMING OUR NITO GIFTLINK..**
**[+] SHOW ACCOUNT EMAIL **
**ON SAME VIDEO AFTER CLAIMING NITRO GIFTLINK..**
**[+] SEND SCREENSHOTS OF DISCORD U RECEIVED ON SAME EMAIL OF REVOKE..**
"""


# on >tos command send message with tos
@bot.command()
async def tos(ctx, type: str = None):
  if type == None:
    await ctx.send(tos_msg)
  elif type == "basic":
    await ctx.send(tos_basic_msg)


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
    LTC Balance: {"{:,.2f}".format(float(data['balance']))}
    LTC Total Received: {"{:,.2f}".format(float(data['total_received']))}
    LTC Total Sent: {"{:,.2f}".format(float(data['total_sent']))}
    LTC Unconfirmed Balance: {"{:,.2f}".format(float(data['unconfirmed_balance']))}
    ```
    """
  await ctx.send(message)


#on >btcinfo command send message with btc info
@bot.command()
async def btcinfo(ctx, address: str):
  req = requests.get('https://blockchair.com/litecoin/address/' + address)
  soup = BeautifulSoup(req.text, 'html.parser')
  values = soup.find_all('span', {"class": 'account-hash__balance__values'})
  balance = values[0]
  total_received = values[1]
  total_sent = values[2]

  message = f"""
    ```    
    LTC Address: {address}
    LTC Balance: {"{:,.2f} USD".format(float(balance.select('span.wb-ba')[1].text))}
    LTC Total Received: {"{:,.2f} USD".format(float(total_received.select('span.wb-ba')[1].text))}
    LTC Total Sent: {"{:,.2f} USD".format(float(total_sent.select('span.wb-ba')[1].text))}
    ```
    """
  await ctx.send(message)


# on >crypto command send message with crypto prices of btc, eth, ltc in usd and irn
@bot.command()
async def crypto(ctx):
  url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Clitecoin&vs_currencies=usd'
  r = requests.get(url)
  data = r.json()
  message = f"""
    ```    
    BTC: {"USD{:,.2f}".format(data['bitcoin']['usd'])}
    ETH: {"USD{:,.2f}".format(data['ethereum']['usd'])}
    LTC: {"USD{:,.2f}".format(data['litecoin']['usd'])}
    ```
    """
  await ctx.send(message)


#on >bal command send message with your ltc info
@bot.command()
async def bal(ctx):
  req = requests.get(
    'https://blockchair.com/litecoin/address/LhBvQWcygiPKoYQtzneZADi4nfQp2z8JjY'
  )
  soup = BeautifulSoup(req.text, 'html.parser')
  values = soup.find_all('span', {"class": 'account-hash__balance__values'})
  balance = values[0]
  total_received = values[1]
  total_sent = values[2]

  message = f"""
    ```    
    LTC Address: LhBvQWcygiPKoYQtzneZADi4nfQp2z8JjY
    LTC Balance: {"{:,.2f} USD".format(float(balance.select('span.wb-ba')[1].text))}
    LTC Total Received: {"{:,.2f} USD".format(float(total_received.select('span.wb-ba')[1].text))}
    LTC Total Sent: {"{:,.2f} USD".format(float(total_sent.select('span.wb-ba')[1].text))}
    ```
    """
  await ctx.send(message)


# >afk command which makes you afk and sends message when someone pings you and removed afk when you message
@bot.command()
async def afk(ctx, *, reason=None):
  await ctx.send(f"{ctx.author.mention} is now afk: {reason}")
  await ctx.author.edit(nick=f"[AFK] {ctx.author.name}")
  while True:
    msg = await bot.wait_for('message')
    if msg.author == ctx.author:
      await ctx.author.edit(nick=f"{ctx.author.name}")
      await ctx.send(f"{ctx.author.mention} is no longer afk")
      break
    if ctx.author.mentioned_in(msg):
      await ctx.send(f"{ctx.author.mention} is afk: {reason}")


# on >meme command send random meme gif from tenor
@bot.command()
async def meme(ctx):
  url = "https://g.tenor.com/v1/random?q=meme&key=LIVDSRZULELA&limit=1"
  r = requests.get(url)
  data = r.json()
  await ctx.send(data['results'][0]['url'])


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
    >bal
    >afk
    >meme
    >help```""")


bot.run(token)
