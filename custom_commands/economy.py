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

@bot.command()
@commands.cooldown(1, 86400, BucketType.user)
async def daily(ctx):
    for key, value in balances.items():
        if int(key) == ctx.message.author.id:
            bal = int(value)
            new_bal = bal+500
            balances[int(key)] == new_bal
            embed = discord.Embed(description="You claimed your daily $500!", timestamp=datetime.utcnow(), color=0x000000)
            embed.set_author(name="{}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
            return
    balances[ctx.message.author.id] == 500
    embed = discord.Embed(description="You claimed your daily $500!", timestamp=datetime.utcnow(), color=0x000000)
    embed.set_author(name="{}".format(ctx.message.author.name), icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed)
    return
