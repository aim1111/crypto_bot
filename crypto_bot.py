from discord.ext import commands
import requests_toolbelt
import requests
import discord
from dhooks import Webhook, Embed
from discord.ext import commands, tasks
from discord_webhook import DiscordEmbed, DiscordWebhook
import aiohttp
import asyncio
import time
from os import system
from typing import List
import aiohttp
from inspect import getsource
client = commands.Bot(command_prefix = '!')
import random
from random import choice
print('''
              Commands
    1. !address <btc address of your choice (tells you how much money the address has)
    2. !update <chanel id> (displays the price of bitcoin on the channel id specified)
    3. !help (this command)''')
token = input('Enter bot token :')
@client.command()
async def address(ctx, add):
    r = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
    rj = r.json()
    price = rj['data']['amount']
    r = requests.get(f'https://blockchain.info/q/addressbalance/{add}').text
    bal = r
    embed = discord.Embed(
        color= discord.Colour.gold() # or any color you want
    )
    embed.add_field(name='Addy' ,value=f'{add}', inline=False)
    embed.add_field(name='Balance in btc' ,value=f'{bal}', inline=False)

    await ctx.send(embed = embed)
@client.command()
async def update(ctx, iddd):
    while True:
        r = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
        rj = r.json()
        price = rj['data']['amount']
        channel = client.get_channel(iddd)
        new_name = f'btc price: {price}'
        await channel.edit(name=new_name)
        await client.change_presence(activity=discord.Game(f'btc price: {price}'))
        time.sleep(1000)
@client.command()
async def help(ctx):
    await ctx.send('''
    Commands
    1. !address <btc address of your choice (tells you how much money the address has)
    2. !update <chanel id> (displays the price of bitcoin on the channel id specified)
    3. !help (this command)''')
client.run(token)
