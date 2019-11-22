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
# confess

@bot.command()
async def confess(ctx, *, msg: str):
    await ctx.message.delete()
    chan = discord.utils.get(ctx.message.author.guild.channels, name="x【confessions】x")
    tosend = ctx.message.content[9:]
    embed = discord.Embed(title="Confession", description="{}".format(tosend))
    await chan.send(embed=embed)


@confess.error
async def confess_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="You didn't give me a confession.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

