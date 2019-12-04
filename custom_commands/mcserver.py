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

# Bot Commands:
# 

# Teams: BLACK, RED

@bot.command()
async def setign(ctx, name: str):
  storage = bot.get_guild(646432280365236235)
  storageMC = bot.get_channel(651763336425373707)
  if mcIGNs[ctx.message.author.id] = name:
    mcIGNs[ctx.message.author.id] = name
    msg = mcIGNsToDelete[ctx.message.author.id]
    await msg.edit(content=f"{ctx.message.author.id}|{name}")
    return
  else:
    mcIGNs[ctx.message.author.id] = name
    msg = await storageMC.send("{}|{}".format(ctx.message.author.id, name))
    mcIGNsToDelete[ctx.message.author.id] = msg.id
    
@setign.error
async def setign_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Ok, your name is bob. Now enter a real in-game name. Thanks.")
  else:
    print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)







































