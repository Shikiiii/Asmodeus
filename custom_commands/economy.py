import discord
from discord.ext import commands

import random
import sys
import traceback
import asyncio
import datetime
import json

from datetime import datetime

from common_vars import *

# Import for cooldowns.
from discord.ext.commands.cooldowns import BucketType

async def convertSecs(seconds: int):
    minutes = seconds/60
    seconds %= 60
    hours = minutes/60
    minutes %= 60
    return "{}H {}M {}S".format(int(hours), int(minutes), int(seconds))

@bot.command()
@commands.cooldown(1, 86400, BucketType.user)
async def daily(ctx):
    storage = bot.get_guild(646432280365236235)
    for key, value in balances.items():
        if int(key) == ctx.message.author.id:
            print(balances)
            bal = int(value)
            new_bal = bal+500
            balances[str(key)] = new_bal
            storageUP = storage.get_channel(646432281287852057)
            msg = None
            for key, value in balancesToDelete.items():
                if int(key) == ctx.message.author.id:
                    msg = await storageUP.fetch_message(int(value))
            marriedd = None
            for key, value in married.items():
                if int(key) == ctx.message.author.id:
                    try:
                        marriedd = bot.fetch_user(int(value))
                    except:
                        marriedd = 0
            if marriedd is None:
                marriedd = 0
            await msg.edit(content="{}|{}|{}".format(ctx.mesage.author.id, marriedd.id, new_bal))
            embed = discord.Embed(description="You claimed your daily $500!", timestamp=datetime.utcnow(), color=0x000000)
            embed.set_author(name="{}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
            return
    storageUP = storage.get_channel(646432281287852057)
    msg = None
    bal = 2500
    newDB = ctx.message.author.id
    try:
        msg = await storageUP.fetch_message(marriedToDelete[ctx.message.author.id])
    except:
        msg = None
    if msg is None:
        msgg = await storageUP.send("{}|0|{}".format(ctx.message.author.id, bal))
        balancesToDelete[str(newDB)] = msgg.id
    else:
        await msg.edit(content="{}|{}|{}".format(ctx.mesage.author.id, married, bal))
        balancesToDelete[str(newDB)] = msg.id
    balances[str(newDB)] = 2500
    embed = discord.Embed(description="Congratulations on getting your first money! Since this is your first daily, you've been given $2500!", timestamp=datetime.utcnow(), color=0x000000)
    embed.set_author(name="{}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed)
    return

@daily.error
async def daily_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        timeLeft = await convertSecs(int(error.retry_after))
        embed = discord.Embed(description="Whoa there! **Daily** means like, once per day, no? You'll be able to get it again in **{}**, glhf.".format(timeLeft), timestamp=datetime.utcnow())
        embed.set_author(name="{}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
@bot.command()
async def balance(ctx, *, user: discord.Member):
    for key, value in balances.items():
        if int(key) == user.id:
            balance = str(value)
            embed = discord.Embed(description="{}'s balance is $**{}**.".format(user.mention, balance), color=0x000000)
            embed.set_author(name="{}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
            return
    embed = discord.Embed(description="{} hasn't used an economy command yet, so their balance is $0.".format(user.mention), color=0x000000)
    embed.set_author(name="{}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed)
    return

@balance.error
async def balance_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        for key, value in balances.items():
            if int(key) == ctx.message.author.id:
                balance = str(value)
                embed = discord.Embed(description="Your balance is $**{}**.".format(balance), color=0x000000)
                embed.set_author(name="{}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
                await ctx.send(embed=embed)
                return
        embed = discord.Embed(description="You haven't used an economy command yet, so your balance is $0.", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
        return
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="Member not found.", color=0xFF1717, timestamp=datetime.utcnow())
        embed.set_author(name="{}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
