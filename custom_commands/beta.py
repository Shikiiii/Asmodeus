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
async def purgeshit(ctx, *, word: str):
      if ctx.message.author.id != 680519129219727380:
            return
      chans = 0
      globalcount = 0
      for channel in ctx.message.guild.text_channels:
            await ctx.send("Checking {}...".format(channel.mention))
            i = 0
            chans += 1
            async for message in channel.history(limit=None):
                  if word in message.content.lower():
                        await message.delete()
                        i += 1
                        globalcount += 1
            await ctx.send("Deleted {} messages in {} that matched the search.".format(str(i), channel.mention))
      await ctx.send("Done! Checked {} text channels, deleted {} messages in total.".format(str(chans), str(globalcount)))
            

@bot.command(aliases=["rs", "starthis", "st"])
async def requeststar(ctx, id: int):
      message = None
      try:
            message = await ctx.message.channel.fetch_message(id)
            await message.add_reaction("⭐")
      except:
            await ctx.send("**{}**, message not found. Please make sure you're getting a valid message ID.".format(ctx.message.author.name))
      embed = discord.Embed(description="[**Click __HERE__ to jump to the message!**]({})".format(message.jump_url))
      left = 5
      for reaction in message.reactions:
            if reaction.emoji == "⭐":
                  left = left - reaction.count
      await ctx.send("**{}** is requesting to star a message. It requires **{}** more ⭐ reactions to get in <#687158464849379339>.".format(ctx.message.author.name, str(left)), embed=embed) 

@bot.command()
async def topic(ctx):
      questions = ["What weird food combinations do you really enjoy?", "What social stigma does society need to get over?", "What’s something you really resent paying for?", "What would a world populated by clones of you be like?","What would a world populated by clones of you be like?","Do you think that aliens exist?","Where are some unusual places you’ve been?","What are some red flags to watch out for in daily life?","What movie can you watch over and over without ever getting tired of?","When did something start out badly for you but in the end, it was great?","What’s wrong but sounds right?","Who is your favorite person in the server?","If you couldn’t be convicted of any one type of crime, what criminal charge would you like to be immune to?","In the past people were buried with the items they would need in the afterlife, what would you want buried with you so you could use it in the afterlife?","Who do you go out of your way to be nice to?","What food is delicious but a pain to eat?","What “old person” things do you do?","What’s the most expensive thing you’ve broken?","What’s your cure for hiccups?","What mythical creature do you wish actually existed?","What was the most unsettling film you’ve seen?","What are you interested in that most people aren’t?","Most Memorable Birthday?","What is your guilty pleasure?","What would be your last meal?","Do you eat fries with a sauce or without?","What is the worst food in your opinion?","What kind of person would you like to be?","What is your life goal?","What is your favorite game?","What’s on Your Bucket List?","Do you prefer coffee or tea?","Do you drink water cold or warm?"]
      await ctx.send(f"{random.choice(questions)}")
      
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
async def fixrolemenudms(ctx):
      chan = bot.get_channel(687158468381114409)
      msg = await chan.fetch_message(687280036520263740)
      dms = discord.Embed(description=":shaved_ice:«────── « ⋅ʚ♡ɞ⋅ » ──────»:shaved_ice:\n**✧༺༻✧♡༻∞　DMs　∞༺♡✧༺༻✧**\n\n꒰:cake:꒱ <@&687268281085722647> \n꒰:doughnut:꒱ <@&687268303915450448> \n꒰:candy:꒱ <@&687268333971701782>\n\n«────────────────────»", color=0x84659E)
      dms.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/683015150881603584/original_453.gif")
      await msg.edit(embed=dms)
      
            
            

@bot.command()
async def rolemenupost(ctx):
      age = discord.Embed(description=":cloud:«────── « ⋅ʚ♡ɞ⋅ » ──────»:cloud: \n**✧༺༻✧♡༻∞　Age　∞༺♡✧༺༻✧**\n\n꒰:rice_ball:꒱ <@&687266670162477068> \n꒰:rice:꒱ <@&687266974509695028>\n\n«────────────────────»", color=0x081154)
      age.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/683015137778729061/original_12_-_Copy.gif")
      gender = discord.Embed(description=":rice_ball:«─────── « ⋅ʚ♡ɞ⋅ » ───────»:rice_ball: \n**✧༺༻✧♡༻∞　Gender　∞༺♡✧༺༻✧**\n\n꒰:blossom:꒱ <@&710597909447704681> \n꒰:sunflower:꒱ <@&710597909971992598> \n꒰:tulip:꒱ <@&710597910747938917>\n\n«──────────────────────»", color=0x06D11B)
      gender.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/683015142191267880/original_3.gif")
      device = discord.Embed(description=":herb:«─────── « ⋅ʚ♡ɞ⋅ » ───────»:herb:\n**✧༺༻✧♡༻∞　Device　∞༺♡✧༺༻✧**\n\n꒰:leaves:꒱ <@&687267054591410205> \n꒰:avocado:꒱ <@&710586667983175741> \n꒰:tanabata_tree:꒱ <@&710597908226900028>\n\n«──────────────────────»", color=0xC0C2EB)
      device.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/683015135719063552/original_13.gif")
      pings = discord.Embed(description=":star2:«─────── « ⋅ʚ♡ɞ⋅ » ───────»:star2: \n**✧༺༻✧♡༻∞　Pings　∞༺♡✧༺༻✧**\n\n꒰:dizzy:꒱ <@&710597917194453012> \n꒰:sparkles:꒱ <@&710597917869604964> \n꒰:ringed_planet:꒱ <@&710597918494556180> \n꒰:zap:꒱ <@&710597919203393599>\n\n«──────────────────────»", color=0xFA4B88)
      pings.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/683015182909440111/tenor_6.gif")
      dms = discord.Embed(description=":shaved_ice:«────── « ⋅ʚ♡ɞ⋅ » ──────»:shaved_ice:\n**✧༺༻✧♡༻∞　DMs　∞༺♡✧༺༻✧**\n\n꒰:cake:꒱ <@&710597920885309552> \n꒰:doughnut:꒱ <@&710597921711587440> \n꒰:candy:꒱ <@&710597922865021038>\n\n«────────────────────»", color=0x84659E)
      dms.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/683015150881603584/original_453.gif")
      continent = discord.Embed(description=":fish_cake:«─────── « ⋅ʚ♡ɞ⋅ » ───────»:fish_cake: \n**✧༺༻✧♡༻∞　Continent　∞༺♡✧༺༻✧**\n\n꒰:tulip:꒱ <@&710597912358420570> \n꒰:hamburger:꒱ <@&710597913130041434> \n꒰:sunflower:꒱ <@&710597913763643444> \n꒰:sushi:꒱ <@&710597914568949782> \n꒰:cherry_blossom:꒱ <@&710597915185512458> \n꒰:fog:꒱ <@&710597915621720145>\n\n«────────────────────»", color=0xF261B1)
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
      yellow = discord.Embed(description=":crescent_moon:**⊱─────── {⋅. Yellow .⋅} ───────⊰**:crescent_moon: \n  .★・・・・・★・・・・・★・・・・・★.\n\n꒰:lemon:꒱ <@&706228599300030517>\n꒰:hatched_chick:꒱ <@&687222581937307648>\n꒰:bee:꒱ <@&687222629412896798>\n꒰:sunflower:꒱ <@&687223129017286658>\n\n.・。.・゜✭・.・✫・゜・。. ・。.・✭", color=0xFFF94A)
      yellow.set_image(url="https://media.discordapp.net/attachments/680498370636414994/680561077104148532/image0.gif")
      green = discord.Embed(description=":leaves:**⊱───── {⋅. Green .⋅} ─────⊰**:leaves: \n   .★・・・・★・・・・★・・・・★.\n\n꒰:herb:꒱ <@&687223178627514369>\n꒰:four_leaf_clover:꒱ <@&687264599744970752>\n꒰:avocado:꒱ <@&687264633396265002>\n꒰:evergreen_tree:꒱ <@&687264652643663909>\n\n.・。.・゜✭・.・✫・゜・。. ・。.・゜", color=0x15BF1E)
      green.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/682941700364042282/green.gif")
      blue = discord.Embed(description=":comet:**⊱────── {⋅. Blue .⋅} ──────⊰**:comet: \n   .★・・・・★・・・・★・・・・★.\n\n꒰:butterfly:꒱ <@&687264683652284489>\n꒰:ocean:꒱ <@&687264906910629928>\n꒰:dolphin:꒱ <@&687264932084973587>\n꒰:droplet:꒱ <@&687264992768426007>\n\n.・。.・゜✭・.・✫・゜・。. ・。.・゜", color=0x87ADFF)
      blue.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/682941697952448553/blue.gif")
      purple = discord.Embed(description=":grapes:**⊱─────── {⋅. Purple .⋅} ────────⊰**:grapes: \n   .★・・・・・★・・・・・★・・・・・★.\n\n꒰:unicorn:꒱ <@&687265020542976034>\n꒰:crystal_ball:꒱ <@&687265255092387851>\n꒰:grapes:꒱ <@&687265285203558562>\n꒰:umbrella2:꒱ <@&687265300466630669>\n꒰:octopus:꒱ <@&687265322771939379>\n\n.・。.・゜✭・.・✫・゜・。. ・。.・゜・.・", color=0x8C47BA)
      purple.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/682941693917659148/purple.gif")
      pink = discord.Embed(description=":cherry_blossom:**⊱────── {⋅. Pink .⋅} ──────⊰**:cherry_blossom: \n   .★・・・・★・・・・★・・・・★.\n\n꒰:tulip:꒱ <@&687265357270220838>\n꒰:squid:꒱ <@&687265712229580801>\n꒰:hibiscus:꒱ <@&687265738091921439>\n꒰:shaved_ice:꒱ <@&687265761500463104>\n꒰:birthday:꒱ <@&687265788499197984>\n\n.・。.・゜✭・.・✫・゜・。. ・。.・゜✭", color=0xFFC7F5)
      pink.set_image(url="https://cdn.discordapp.com/attachments/680532449989492750/682941715719782435/5f04eb43e13d279562651b833d8d2dd7.gif")
      black = discord.Embed(description=":rice_ball:**⊱────── {⋅. Black .⋅} ──────⊰**:rice_ball:\n   .★・・・・★・・・・★・・・・★.\n\n꒰:cloud:꒱ <@&687265812750532642>\n꒰:garlic:꒱ <@&687158421635465218>\n꒰:new_moon:꒱ <@&687221241240748042>\n꒰:black_heart:꒱ <@&687221338976288778>\n\n.・。.・゜✭・.・✫・゜・。. ・。.・゜✭", color=0x171717)
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
      embed = discord.Embed(title="«────── « ⋅ʚ♡ Rules ♡ɞ⋅ » ──────»", description="<:as_check:710602034318934156> ``1.`` Always follow the [Discord ToS](https://discordapp.com/terms) and the [Community Guidelines](https://discordapp.com/guidelines).\n\n<:as_check:710602034318934156> ``2.`` Being toxic __is__ allowed to a certain extend.\n<:as_check:710602034318934156> - You can banter with you friends and people who understand that you are joking, but no matter what don't go in to sensitive topics or anything against ToS.\n\n<:as_check:710602034318934156> ``3.`` Don't advertise.\n<:as_check:710602034318934156> - Don't advertise anything in the server nor in DMs. If anyone is DMing you something about join this or follow this report to staff.\n\n<:as_check:710602034318934156> ``4.`` No doxing.\n<:as_check:710602034318934156> - No leaking of any kind of personal information, no joining here to expose someone or anything alike that. No IP grabbers, DDoSing or treating to hack anyone.\n\n<:as_check:710602034318934156> ``5.`` Respect everyone in the server.\n<:as_check:710602034318934156> - Use your common sense when chatting the people here, we want everyone to have a fun time while using the server.\n\n<:as_check:710602034318934156> ``6.`` No racism,homophobia or any kind of discrimination.\n<:as_check:710602034318934156> - Mild slurs are okay but don't go too far.\n\n<:as_check:710602034318934156> ``7.`` Spamming and Trolling.\n<:as_check:710602034318934156> - No mass pings or spamming bot commands in <#687158469899452577>, also joining to troll will get you banned.\n\n<:as_check:710602034318934156> ``8.`` No drama.\n<:as_check:710602034318934156> - No creating drama with anyone, if you don't like someone ignore them. Or talk about it in DMs.\n\n<:as_check:710602034318934156> - ``9.`` No NSFW and gore.\n\n<:as_check:710602034318934156> If you find any mistakes/loopholes in the rules or in the general server. Please DM <@680519129219727380>.", color=0x505AC7, timestamp=datetime.utcnow())
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
                embed = discord.Embed(title=".・゜-: ✧ :-　Booster Perks　-: ✧ :-゜・．", description="<a:purple_hearts:687272661138800650>─ You will get permission to advertise whatever you want in <#680532434277630043>\n\n<a:purple_hearts:687272661138800650>─ You will get the booster role that is hoisted above the members.\n\n<a:purple_hearts:687272661138800650>─ You get a special role, which you personalize with name and color.\n\n<a:purple_hearts:687272661138800650>─ You get a custom response when someone mentions your name in the chat. \n\n<a:purple_hearts:687272661138800650>─ You can apply for staff even if the applications are closed.\n\n<a:purple_hearts:687272661138800650>─ Higher chances in winning future giveaways, also booster only giveaways. \n\n<a:purple_hearts:687272661138800650>─ You will get your own voice channel and text channel, alike a blog, where it can be public or private. You can invite your friends in it and do whatever your hearts desire. \n\n<a:purple_hearts:687272661138800650>─ You'll get access to the logs (join/leave, deleted and edit messages, etc) without having to be staff.", color=0xB6B3FC, timestamp=datetime.utcnow()) 
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

