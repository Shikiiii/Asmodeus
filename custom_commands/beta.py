import discord
from discord.ext import commands

import random
import sys
import traceback
import asyncio
import datetime
import json

from common_vars import *

# Commands in this file:
# none
        
@bot.command()
@commands.is_owner()
async def test(ctx):
    guild = bot.get_guild(646432280365236235)
    chan = guild.get_channel(646432846961049601)
    await chan.send("Testing!")

