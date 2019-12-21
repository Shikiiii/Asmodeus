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
@commands.is_owner()
async def test(ctx):
  await player.send("```yaml\nAsmodeus 1.15.1 | SMP | Open NOW!\n\nBecause you registered with your name ``{}``, I'm here to invite you.\n\n**IP:** play.asmodeusdiscord.com")

@bot.command()
@commands.is_owner()
async def openServer(ctx):
  for key, value in mcIGNs.items():
    player = bot.get_user(int(key))
    try:
      await player.send("```yaml\nAsmodeus 1.15.1 | SMP | Open NOW!\n\nBecause you registered with your name ``{}``, I'm here to invite you.\n\n**IP:** play.asmodeusdiscord.com".format(str(value)))
    except:
      shiki = bot.get_user(237938976999079948)
      await shiki.send("Couldn't DM {} with ID {}.".format(player, player.id))
                      
@bot.command()
async def reg(ctx):
  regppl = 0
  for key, value in mcIGNs.items():
    regppl+=1 
  await ctx.send("There are currently **{}** players registered for the server.".format(regppl))

@bot.command()
async def setign(ctx, name: str):
  storage = bot.get_guild(646432280365236235)
  storageMC = bot.get_channel(651763336425373707)
  for key, value in mcIGNs.items():
    if key == ctx.message.author.id:
      mcIGNs[ctx.message.author.id] = name
      msgID = mcIGNsToDelete[ctx.message.author.id]
      msgOBJ = await storageMC.fetch_message(msgID)
      await msgOBJ.edit(content=f"{ctx.message.author.id}|{name}")
      await ctx.send("Your new **Minecraft In-Game Name** is: ``{}``".format(name))
      return
  mcIGNs[ctx.message.author.id] = name
  msg = await storageMC.send("{}|{}".format(ctx.message.author.id, name))
  mcIGNsToDelete[ctx.message.author.id] = msg.id
  await ctx.send("Your new **Minecraft In-Game Name** is: ``{}``".format(name))

    
@setign.error
async def setign_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Ok, your name is bob. Now enter a real in-game name. Thanks.")
  else:
    print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)







































