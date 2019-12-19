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
async def tag(ctx, *, type: str):
        if type == "boosting":
                await ctx.send(">>> We value every booster. That's why boosters get cool stuff.\n\n``1`` <a:hyperpin:653053092128096256> You get your own custom **role** and **command**, as long as the command isn't very hard to do.\n``2`` <a:hyperpin:653053092128096256> You get your own custom-response from our bot when someone says your name/mentions you.\n``3`` <a:hyperpin:653053092128096256> You get to apply for a ChatMod even if the applications are closed.\n``4`` <a:hyperpin:653053092128096256> Boosters only role, hoisted high in the members.\n``5`` <a:hyperpin:653053092128096256> You get to participate in polls, events and giveaways for boosters only.\n``6`` <a:hyperpin:653053092128096256> Our deepest love. We love every single booster! <a:hyperheart:653053504809861150>\n\nPLEASE boost our server if you like it!")
        elif type == "lang" or type == "language" or type == "english":
                await ctx.send("**__This is an english server.__**\n\nYou aren't allowed to chat in other languages. Please refrain from using them.\n**Staff is allowed to warn you a few times before taking action.**\n\nSpeaking in other languuages is however allowed.")
        elif type == "bot" or type == "bots":
                await ctx.send("**Bots are allowed, but spamming bot commands isn't.**\n\nWe all know its annoying to get moved to the bot channel for stuff like hug, kiss, etc. We allow these, but do not flood the chat with bot commands, you'll be muted.")

@bot.command()
@commands.is_owner()
async def checkPerms(ctx):
        guild = bot.get_guild(385378814584422413)
        role1 = discord.utils.get(guild.roles, name="Bots")
        role2 = discord.utils.get(guild.roles, name="Asmodeus")
        owner = await bot.fetch_user(237938976999079948)
        # Checking 'Bots'
        await owner.send("Checking role Bots:")
        if role1.permissions.kick_members == True:
                await owner.send("Can kick members!")
        if role1.permissions.ban_members == True:
                await owner.send("Can ban members!")
        if role1.permissions.send_messages == True:
                await owner.send("Can send messages!")
        if role1.permissions.manage_channels == True:
                await owner.send("Can manage channels!")
        if role1.permissions.manage_guild == True:
                await owner.send("Can manage guild!")
        if role1.permissions.manage_messages == True:
                await owner.send("Can manage messages!")
        if role1.permissions.mention_everyone == True:
                await owner.send("Can mention everyone!")
        if role1.permissions.manage_roles == True:
                await owner.send("Can manage roles!")
        # Checking 'Asmodeus'
        await owner.send("Checking role Asmodeus:")
        if role2.permissions.kick_members == True:
                await owner.send("Can kick members!")
        if role2.permissions.ban_members == True:
                await owner.send("Can ban members!")
        if role2.permissions.send_messages == True:
                await owner.send("Can send messages!")
        if role2.permissions.manage_channels == True:
                await owner.send("Can manage channels!")
        if role2.permissions.manage_guild == True:
                await owner.send("Can manage guild!")
        if role2.permissions.manage_messages == True:
                await owner.send("Can manage messages!")
        if role2.permissions.mention_everyone == True:
                await owner.send("Can mention everyone!")
        if role2.permissions.manage_roles == True:
                await owner.send("Can manage roles!")

@bot.command()
@commands.is_owner()
async def donate(ctx):
        embed1 = discord.Embed(title="__Nitro Boosting__", description="Want to help the server out? Check the list below and see if you meet these requirements:\n\n``1`` <a:hyperpin:653053092128096256> You got boosts that you aren't using?\n``2`` <a:hyperpin:653053092128096256> Do you like this server?\nWell then, feel free to boost our server! \n\n<a:hyperheart:653053504809861150> **Boosters get a lot of perks, if you'd like to see them all, use ``!tag boosting``.** <a:hyperheart:653053504809861150>", color=0xF216F2)
        await ctx.send(embed=embed1)
        await ctx.send("> Don't have Nitro? There are other ways:")
        embed2 = discord.Embed(title="__Donating__", description="<a:hyperpin:653053092128096256> Donating helps out the server **a lot**. If you've got a dollar or two to spare, please do! Donating **1$** or above will give you all stuff boosters get.\n\n<a:redlight:653053463965466634> All donations go towards the server. This includes (but it's not only limited to):\n - <a:hypertada:653053428469202949> Buying promotions for the server.\n - <a:hypertada:653053428469202949> Hosting giveaways.\n - <a:hypertada:653053428469202949> Hosting events with rewards.\n\n<a:hyperpin:653053092128096256> You'll also get some cool stuff:\n    ; <a:confetti:653053538532065306> **2$** or __above__:\n    @here promotion\n    ; <a:confetti:653053538532065306> **5$** or __above__:\n    @everyone promotion + apply for ChatMod\n\n<a:hyperpin:653053092128096256> [Donate Now!](https://www.paypal.me/asmodeusdiscord)", color=0xEEFF03)
        embed2.set_footer(text="If you don't want to pay with PayPal, please DM the owner. Other ways to pay are available. Every payment will stay as 'Pending' until I, the server owner, accept it. Meaning you have enough time to cancel the transaction if you decide to.")
        await ctx.send(embed=embed2)
        await ctx.send("> For any payment issues/questions please DM <@237938976999079948>. | Direct EMail for donations is ||asmodeus@abv.bg||. Thank you for being an amazing community.")

@bot.command()
@commands.is_owner()
async def test(ctx):
        guild = bot.get_guild(646432280365236235)
        chan = guild.get_channel(646432846961049601)
        await chan.send("Testing!")

