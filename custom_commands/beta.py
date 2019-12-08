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
async def donate(ctx):
        embed1 = discord.Embed(title="__Nitro Boosting__", description="Want to help the server out? Check the list below and see if you meet these requirements:\n\n``1`` <a:hyperpin:> You got boosts that you aren't using?\n``2`` <a:hyperpin:> Do you like this server?\nWell then, feel free to boost our server! \n\n<a:hyperheart:> **Boosters get a lot of perks, if you'd like to see them all, use ``!tag boosting``.** <a:hyperheart:>", color=0xF216F2)
        await ctx.send(embed=embed1)
        await ctx.send("> Don't have Nitro? There are other ways:")
        embed2 = discord.Embed(title="__Donating__", description="<a:hyperpin:> Donating helps out the server **a lot**. If you've got a dollar or two to spare, please do!\n\n<a:redlight:> All donations go towards the server. This includes (but it's not only limited to):\n - <a:hypertada:> Buying promotions for the server.\n - <a:hypertada:> Hosting giveaways.\n - <a:hypertada:> Hosting events with rewards.\n\n<a:hyperpin:> You'll also get some cool stuff:\n    ; **5$** or __above__:\n    @here promotion + ChatMod\n    ; **10$** or _above__:\n    @everyone promotion + Mod\n\n[**Donate Now!**](https://www.paypal.me/asmodeusdiscord)", color=0xEEFF03)
        embed2.set_footer(text="If you don't want to pay with PayPal, please DM the owner. Other ways to pay are available. Every payment will stay as 'Pending' until I, the server owner, accept it. Meaning you have enough time to cancel the transaction if you decide to.")
        await ctx.send(embed=embed2)
        await ctx.send("> For any payment issues/questions please DM <@237938976999079948>. | Direct EMail for donations is ||asmodeus@abv.bg||. Thank you for being an amazing community.

@bot.command()
@commands.is_owner()
async def test(ctx):
        guild = bot.get_guild(646432280365236235)
        chan = guild.get_channel(646432846961049601)
        await chan.send("Testing!")

