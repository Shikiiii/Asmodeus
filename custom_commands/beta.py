import discord
from discord.ext import commands

import random
import sys
import traceback
import asyncio
import datetime
import json

from common_vars import *

from datetime import datetime

# Commands in this file:
# none
      
@bot.command()
async def colormenupost(ctx):
      red = discord.Embed(title="Red - ;;" description=":maple_leaf:⊱────── {⋅. Red .⋅} ──────⊰:maple_leaf: \n   ★・・・・★・・・・★・・・・★\n\n꒰:maple_leaf:꒱ @Pastel Red \n꒰:apple:꒱ @Light Red \n꒰:strawberry:꒱@Medium Red \n꒰:cherries:꒱ @Dark Red\n\n.・。.・゜✭・.・✫・゜・。. ・。.・✭", color=0xFA1D19)
      red.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/682945355674812487/ezgif-2-e3111241cfda.gif")
      orange = discord.Embed(title="Orange - ;;", color=0xFFA14A)
      orange.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/682941708572426292/orange.gif")
      yellow = discord.Embed(title="Yellow - ;;", color=0xFFF94A)
      yellow.set_image(url="https://media.discordapp.net/attachments/680498370636414994/680561077104148532/image0.gif")
      green = discord.Embed(title="Green - ;;", color=0x15BF1E)
      green.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/682941700364042282/green.gif")
      blue = discord.Embed(title="Blue - ;;", color=0x87ADFF)
      blue.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/682941697952448553/blue.gif")
      purple = discord.Embed(title="Purple - ;;", color=0x8C47BA)
      purple.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/682941693917659148/purple.gif")
      pink = discord.Embed(title="Pink - ;;", color=0xFFC7F5)
      pink.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/682941715719782435/5f04eb43e13d279562651b833d8d2dd7.gif")
      black = discord.Embed(title="Black - ;;", color=0x171717)
      black.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/682941690973257734/black.gif")
      await ctx.send(embed=red)
      await ctx.send(embed=orange)
      await ctx.send(embed=yellow)
      await ctx.send(embed=green)
      await ctx.send(embed=blue)
      await ctx.send(embed=purple)
      await ctx.send(embed=pink)
      await ctx.send(embed=black)
      
@bot.command()
async def postrules(ctx):
      if ctx.message.author.id != 680519129219727380:
            return
      embed = discord.Embed(title="Ａｓｍｏｄｅｕｓ| Rules", description="\n``1`` ;; __always__ follow the [discord tos](https://discordapp.com/terms) and the [community guidelines](https://discordapp.com/guidelines). thank u!\n\n``2`` ;; being toxic __is__ allowed, but do not overdo it. do not start beef with anyone.\n\n``3`` ;; don't advertise in the server nor in dms.\n\n``4`` ;; no linking of personal information without agreement \ no doxing.\n\n``5`` ;; respect all members, staff members and etc.\n\n``6`` ;; no racism, discrimination or etc.\n\n\nother than that, please have __common sense__ while you're using the server. this includes (but is not only limited to) spamming, being annoying, mass-mentioning and etc.\n\nif you've found any loopholes or people that break the rules, please let <@680519129219727380> know in dms.", color=0xF255E3, timestamp=datetime.utcnow())
      embed.set_image(url="https://cdn.discordapp.com/attachments/668462934774775818/680606317689307145/asmodeus_rules_gif.gif")
      embed.set_footer(text="Last edited at")
      await ctx.send(embed=embed)
      
@bot.command()
async def testingofdms(ctx):
      embed = discord.Embed(description="```yaml\nActive, non-toxic, friendly and welcoming community. Feel free to join and make new friends!```\n\n>  **10$ Nitro Giveaway happening NOW! JOIN TO ENTER**\n\n - __Chilled mods.__\n - __No useless pings.__\n - __Very addictive.__\n - __Giveaways and events.__\n - __Self-advertising.__", color=0xEBFA16, timestamp=datetime.utcnow())
      embed.set_author(name="Ａｓｍｏｄｅｕｓ💫˳⁺ 2.0", url="https://discord.gg/Qqzy2ds")
      await ctx.send("Asmodeus got deleted at 1K members on 29.12.2019. We've rebuilt the community, but better, more active and more friendly. Join the new server NOW! https://discord.gg/Qqzy2ds", embed=embed)

@bot.command()
async def senddmtoall(ctx):
    if ctx.message.author.id != 237938976999079948:
      return
    for user in bot.users:
        if user.id == 151991728801316864:
            continue
        asmodeus = bot.get_guild(660616924643721248)
        shiki = bot.get_user(237938976999079948)
        if user not in asmodeus.members:
            try:
                embed = discord.Embed(description="```yaml\nActive, non-toxic, friendly and welcoming community. Feel free to join and make new friends!```\n\n>  **10$ Nitro Giveaway happening NOW! JOIN TO ENTER**\n\n - __Chilled mods.__\n - __No useless pings.__\n - __Very addictive.__\n - __Giveaways and events.__\n - __Self-advertising.__", color=0xEBFA16, timestamp=datetime.utcnow())
                embed.set_author(name="Ａｓｍｏｄｅｕｓ💫˳⁺ 2.0", url="https://discord.gg/Qqzy2ds")
                await user.send("Asmodeus got deleted at 1K members on 29.12.2019. We've rebuilt the community, but better, more active and more friendly. Join the new server NOW! https://discord.gg/Qqzy2ds", embed=embed)
                await shiki.send(":white_check_mark: **{} | {}**".format(user, user.id))
            except:
                await shiki.send(":x: **{} | {}**".format(user, user.id))

@bot.command()
@commands.is_owner()
async def changeprice(ctx):
        msg = await bot.fetch_message(653655190137864222)
        embed2 = discord.Embed(title="__Donating__", description="<a:hyperpin:653053092128096256> Donating helps out the server **a lot**. If you've got a dollar or two to spare, please do! Donating **1$** or above will give you all stuff boosters get.\n\n<a:redlight:653053463965466634> All donations go towards the server. This includes (but it's not only limited to):\n - <a:hypertada:653053428469202949> Buying promotions for the server.\n - <a:hypertada:653053428469202949> Hosting giveaways.\n - <a:hypertada:653053428469202949> Hosting events with rewards.\n\n<a:hyperpin:653053092128096256> You'll also get some cool stuff:\n    ; <a:confetti:653053538532065306> **2$** or __above__:\n    @here promotion\n    ; <a:confetti:653053538532065306> **5$** or __above__:\n    @everyone promotion\n    ; <a:confetti:653053538532065306> **10$** or __above__:\n    JoinMessage for 2 weeks\n\n<a:hyperpin:653053092128096256> [Donate Now!](https://www.paypal.me/asmodeusdiscord)", color=0xEEFF03)
        embed2.set_footer(text="If you don't want to pay with PayPal, please DM the owner. Other ways to pay are available. Every payment will stay as 'Pending' until I, the server owner, accept it. Meaning you have enough time to cancel the transaction if you decide to.")
        await msg.edit(enbed=embed2)
  
@bot.command()
async def testingembed(ctx):
        embed = discord.Embed(description="```yaml\nSemi-active, non-toxic, friendly and welcoming community. Feel free to join and make new friends!```\n\n:tada: **Join the server to join the Nitro Giveaway!** :tada:", color=0xEBFA16, timestamp=datetime.utcnow())
        embed.set_author(name="Ａｓｍｏｄｅｕｓ❄🎄", url="https://discord.gg/h945y6T")
        await ctx.send("Hey! Asmodeus wants to thank you for your amazing support. We've ran over **1,000** commands now, and we want to celebrate that.\n\n**We're hosting a Nitro Giveaway in the bot's server. :tada:**\nhttps://discord.gg/h945y6T", embed=embed)

@bot.command()
async def serverAv(ctx):
        await ctx.send("{}".format(ctx.guild.icon_url))

@bot.command()
async def tag(ctx, *, type: str):
        if type == "boosting":
                await ctx.send(">>> We value every booster. That's why boosters get cool stuff.\n\n``1`` <a:hyper_pin:662953028428759042> You get your own custom **role** and **command**, as long as the command isn't very hard to do.\n``2`` <a:hyper_pin:662953028428759042> You get your own custom-response from our bot when someone says your name/mentions you.\n``3`` <a:hyper_pin:662953028428759042> You get to apply for a ChatMod even if the applications are closed.\n``4`` <a:hyper_pin:662953028428759042> Boosters only role, hoisted high in the members.\n``5`` <a:hyper_pin:662953028428759042> You get to participate in polls, events and giveaways for boosters only.\n``6`` <a:hyper_pin:662953028428759042> You get access to <#662797497143656509> where you can advertise your stuff, hoisted really high in the channels, so other people would see them./n``7`` <a:hyper_pin:662953028428759042> Our deepest love. We love every single booster! <a:hyper_pin:662953028428759042>\n\nPLEASE boost our server if you like it!")
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

