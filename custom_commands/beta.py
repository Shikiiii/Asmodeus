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
async def movingservers(ctx):
      if ctx.message.author.id != 680519129219727380:
            return
      old_asmo = bot.get_guild(680186413588676649)
      new_asmo = bot.get_guild(680527521762246701)
      for user in old_asmo.members:
            member = new_asmo.get_member(user.id)
            if member is None:
                  try:
                        await user.send("asmodeus, a server you are in, moved to a new server.\nif you'd like to know why: <#684934881360216071>\nplease make sure to join the new one: discord.gg/PRBxdkZ\nthank you!")
                  except:
                        shiki = old_asmo.get_member(680519129219727380)
                        await shiki.send("Couldn't DM {}".format(user))
            elif member is not None:
                  await user.kick()

@bot.command()
async def fixrolemenupings(ctx):
      chan = bot.get_channel(680532444553674773)
      msg = await chan.fetch_message(683687197974724703)
      pings = discord.Embed(description=":star2:«─────── « ⋅ʚ♡ɞ⋅ » ───────»:star2: \n**✧༺༻✧♡༻∞　Pings　∞༺♡✧༺༻✧**\n\n꒰:dizzy:꒱ <@&680813408958021665> \n꒰:sparkles:꒱ <@&680813442747203605> \n꒰:ringed_planet:꒱ <@&680813479333986386> \n꒰:zap:꒱ <@&684408442366328832>\n\n«──────────────────────»", color=0xFA4B88)
      pings.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/683015182909440111/tenor_6.gif")
      await msg.edit(embed=pings)
      
            
            

@bot.command()
async def rolemenupost(ctx):
      age = discord.Embed(description=":cloud:«────── « ⋅ʚ♡ɞ⋅ » ──────»:cloud: \n**✧༺༻✧♡༻∞　Age　∞༺♡✧༺༻✧**\n\n꒰:rice_ball:꒱ <@&687266974509695028> \n꒰:rice:꒱ <@&687266990980857866>\n\n«────────────────────»", color=0x081154)
      age.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/683015137778729061/original_12_-_Copy.gif")
      gender = discord.Embed(description=":rice_ball:«─────── « ⋅ʚ♡ɞ⋅ » ───────»:rice_ball: \n**✧༺༻✧♡༻∞　Gender　∞༺♡✧༺༻✧**\n\n꒰:blossom:꒱ <@&687267497308979262> \n꒰:sunflower:꒱ <@&687267510994862120> \n꒰:tulip:꒱ <@&687267531739627562>\n\n«──────────────────────»", color=0x06D11B)
      gender.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/683015142191267880/original_3.gif")
      device = discord.Embed(description=":herb:«─────── « ⋅ʚ♡ɞ⋅ » ───────»:herb:\n**✧༺༻✧♡༻∞　Device　∞༺♡✧༺༻✧**\n\n꒰:leaves:꒱ <@&687267104239386654> \n꒰:avocado:꒱ <@&687267133214031882> \n꒰:tanabata_tree:꒱ <@&687267263073746966>\n\n«──────────────────────»", color=0xC0C2EB)
      device.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/683015135719063552/original_13.gif")
      pings = discord.Embed(description=":star2:«─────── « ⋅ʚ♡ɞ⋅ » ───────»:star2: \n**✧༺༻✧♡༻∞　Pings　∞༺♡✧༺༻✧**\n\n꒰:dizzy:꒱ <@&687267882635100268> \n꒰:sparkles:꒱ <@&687268022754213892> \n꒰:ringed_planet:꒱ <@&687268043990237237> \n꒰:zap:꒱ <@&687268178169954448>\n\n«──────────────────────»", color=0xFA4B88)
      pings.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/683015182909440111/tenor_6.gif")
      dms = discord.Embed(description=":shaved_ice:«────── « ⋅ʚ♡ɞ⋅ » ──────»:shaved_ice:\n**✧༺༻✧♡༻∞　DMs　∞༺♡✧༺༻✧**\n\n꒰:cake:꒱ <@&687267631731965974> \n꒰:doughnut:꒱ <@&687268303915450448> \n꒰:candy:꒱ <@&687268333971701782>\n\n«────────────────────»", color=0x84659E)
      dms.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/683015150881603584/original_453.gif")
      continent = discord.Embed(description=":fish_cake:«─────── « ⋅ʚ♡ɞ⋅ » ───────»:fish_cake: \n**✧༺༻✧♡༻∞　Continent　∞༺♡✧༺༻✧**\n\n꒰:tulip:꒱ <@&687267631731965974> \n꒰:hamburger:꒱ <@&687267653915770920> \n꒰:sunflower:꒱ <@&687267673331073054> \n꒰:sushi:꒱ <@&687267693858258955> \n꒰:cherry_blossom:꒱ <@&687267710190747660> \n꒰:fog:꒱ <@&687267733422997531>\n\n«────────────────────»", color=0xF261B1)
      continent.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/683018281736863822/original_487.gif")
      await ctx.send(embed=age)
      await ctx.send(embed=gender)
      await ctx.send(embed=device)
      await ctx.send(embed=pings)
      await ctx.send(embed=dms)
      await ctx.send(embed=continent)
      
@bot.command()
async def colormenupost(ctx):
      red = discord.Embed(description=":maple_leaf:**⊱────── {⋅. Red .⋅} ──────⊰**:maple_leaf: \n   . ★・・・・★・・・・★・・・・★ .\n\n꒰:maple_leaf:꒱ <@&687221624713379853>\n꒰:apple:꒱ <@&687221652181745668>\n꒰:strawberry:꒱ <@&687221670226034690>\n꒰:cherries:꒱ <@&687221694506598410>\n\n.・。.・゜✭・.・✫・゜・。. ・。.・✭", color=0xFA1D19)
      red.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/682945355674812487/ezgif-2-e3111241cfda.gif")
      orange = discord.Embed(description=":ringed_planet:**⊱─────── {⋅. Orange .⋅} ───────⊰**:ringed_planet: \n  .★・・・・・★・・・・・★・・・・・★.\n\n꒰:fried_shrimp:꒱ <@&687221992079753262>\n꒰:fire:꒱ <@&687222017182924800>\n꒰:ringed_planet:꒱ <@&687222037416378389>\n꒰:tangerine:꒱ <@&687222059474223128>\n\n.・。.・゜✭・.・✫・゜・。. ・。.・゜✭・.・", color=0xFFA14A)
      orange.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/682941708572426292/orange.gif")
      yellow = discord.Embed(description=":crescent_moon:**⊱─────── {⋅. Yellow .⋅} ───────⊰**:crescent_moon: \n  .★・・・・・★・・・・・★・・・・・★.\n\n꒰:lemon:꒱ <@&687222581937307648>\n꒰:hatched_chick:꒱ <@&687222629412896798>\n꒰:bee:꒱ <@&687223129017286658>\n꒰:sunflower:꒱ <@&687223178627514369>\n\n.・。.・゜✭・.・✫・゜・。. ・。.・✭", color=0xFFF94A)
      yellow.set_image(url="https://media.discordapp.net/attachments/680498370636414994/680561077104148532/image0.gif")
      green = discord.Embed(description=":leaves:**⊱───── {⋅. Green .⋅} ─────⊰**:leaves: \n   .★・・・・★・・・・★・・・・★.\n\n꒰:herb:꒱ <@&687264599744970752>\n꒰:four_leaf_clover:꒱ <@&687264633396265002>\n꒰:avocado:꒱ <@&687264652643663909>\n꒰:evergreen_tree:꒱ <@&687264683652284489>\n\n.・。.・゜✭・.・✫・゜・。. ・。.・゜", color=0x15BF1E)
      green.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/682941700364042282/green.gif")
      blue = discord.Embed(description=":comet:**⊱────── {⋅. Blue .⋅} ──────⊰**:comet: \n   .★・・・・★・・・・★・・・・★.\n\n꒰:butterfly:꒱ <@&687264906910629928>\n꒰:ocean:꒱ <@&687264932084973587>\n꒰:dolphin:꒱ <@&687264992768426007>\n꒰:droplet:꒱ <@&687265020542976034>\n\n.・。.・゜✭・.・✫・゜・。. ・。.・゜", color=0x87ADFF)
      blue.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/682941697952448553/blue.gif")
      purple = discord.Embed(description=":grapes:**⊱─────── {⋅. Purple .⋅} ────────⊰**:grapes: \n   .★・・・・・★・・・・・★・・・・・★.\n\n꒰:unicorn:꒱ <@&687265255092387851>\n꒰:crystal_ball:꒱ <@&687265285203558562>\n꒰:grapes:꒱ <@&687265300466630669>\n꒰:umbrella2:꒱ <@&687265322771939379>\n꒰:octopus:꒱ <@&687265357270220838>\n\n.・。.・゜✭・.・✫・゜・。. ・。.・゜・.・", color=0x8C47BA)
      purple.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/682941693917659148/purple.gif")
      pink = discord.Embed(description=":cherry_blossom:**⊱────── {⋅. Pink .⋅} ──────⊰**:cherry_blossom: \n   .★・・・・★・・・・★・・・・★.\n\n꒰:tulip:꒱ <@&687265712229580801>\n꒰:squid:꒱ <@&687265738091921439>\n꒰:hibiscus:꒱ <@&687265761500463104>\n꒰:shaved_ice:꒱ <@&687265788499197984>\n꒰:birthday:꒱ <@&687265812750532642>\n\n.・。.・゜✭・.・✫・゜・。. ・。.・゜✭", color=0xFFC7F5)
      pink.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/682941715719782435/5f04eb43e13d279562651b833d8d2dd7.gif")
      black = discord.Embed(description=":rice_ball:**⊱────── {⋅. Black .⋅} ──────⊰**:rice_ball:\n   .★・・・・★・・・・★・・・・★.\n\n꒰:cloud:꒱ <@&687158421635465218>\n꒰:garlic:꒱ <@&687221241240748042>\n꒰:new_moon:꒱ <@&687221338976288778>\n꒰:black_heart:꒱ <@&687221285062836246>\n\n.・。.・゜✭・.・✫・゜・。. ・。.・゜✭", color=0x171717)
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
      if ctx.message.author.id != 680519129219727380 and ctx.message.author.id != 569641643641143306:
            return
      embed = discord.Embed(title="«────── « ⋅ʚ♡ Rules ♡ɞ⋅ » ──────»", description="<a:purpleverify:687274842588053511> **1.Always follow the Discord ToS and the Community Guidelines.\n\n<a:purpleverify:687274842588053511> **2. Being toxic __is__ allowed to a certain extend.**\n<a:purplehearts:687272661138800650> - You can banter with you friends and people who understand that you are joking, but no matter what don't go in to sensitive topics or anything against ToS.\n<a:purpleverify:687274842588053511>**3. Don't advertise.**\n<a:purplehearts:687272661138800650> - Don't advertise anything in the server nor in DMs. If anyone is DMing you something about join this or follow this report to staff.\n<a:purpleverify:687274842588053511>**4. No Doxing.**\n<a:purplehearts:687272661138800650> - No leaking of any kind of personal information, no joining here to expose someone or anything alike that. No IP grabbers, DDoSing or treating to hack anyone. \n<a:purpleverify:687274842588053511>**5. Respect everyone in the server.**\n<a:purplehearts:687272661138800650> - Use your common sense when chatting the people here, we want everyone to have a fun time while using the server.\n\n<a:purpleverify:687274842588053511>**6.No racism,homophobia or any kind of discrimination.**\n<a:purplehearts:687272661138800650> - Mild slurs are okay but don't go too far.\n<a:purpleverify:687274842588053511>**7.Spamming and Trolling.**\n<a:purplehearts:687272661138800650> - No mass pings or spamming bot commands in <#687158469899452577>, also joining to troll will get you banned.\n\n<a:purpleverify:687274842588053511>**8.No drama.**\n<a:purplehearts:687272661138800650> - No creating drama with anyone, if you don't like someone ignore them. Or talk about it in __DMS___.\n\n<a:purplehearts:687272661138800650>If you find any mistakes/loopholes in the rules or in the general server. Please DM <@680519129219727380> or <@569641643641143306>.", color=0x505AC7, timestamp=datetime.utcnow())
      embed.set_image(url="https://cdn.discordapp.com/attachments/680570992036413481/684400862205837339/giphy_7.gif")
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
                embed = discord.Embed(title=".・゜-: ✧ :-　Booster Perks　-: ✧ :-゜・．", description="<a:purplehearts:684377574507544631>─ You will get permission to advertise whatever you want in <#680532434277630043>\n\n<a:purplehearts:684377574507544631>─ You will get the booster role that is hoisted above the members.\n\n<a:purplehearts:684377574507544631>─ You get a special role, which you personalize with name and color.\n\n<a:purplehearts:684377574507544631>─ You get a custom response when someone mentions your name in the chat. \n\n<a:purplehearts:684377574507544631>─ You can apply for staff even if the applications are closed.\n\n<a:purplehearts:684377574507544631>─ Higher chances in winning future giveaways, also booster only giveaways. \n\n<a:purplehearts:684377574507544631>─ You will get your own voice channel and text channel, alike a blog, where it can be public or private. You can invite your friends in it and do whatever your hearts desire.", color=0xB6B3FC, timestamp=datetime.utcnow()) 
                await ctx.send(embed=embed)
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

