# a custom bot made for the Asmodeus server by shiki, glow & zaf

# 02/09/2019 | 2020-2019

# (c) MIT License @ Shiki

import discord
from discord import Message, Guild, Member
from discord.ext.commands import Bot
from typing import Optional, Set
from discord.ext import commands

import os
import sys
import traceback
import asyncio
from datetime import datetime
import datetime
import random
import http.client
import json
import requests

bot = Bot(command_prefix='!')
bot.remove_command('help')

#server: Optional[Guild] = None

guild: Optional[Guild] = None

shiki: Optional[Member] = None

msgsCounterr = 0
msgsCounterrr = 0
allTimeMessages = 0
	
# bot status.

@bot.event
async def on_ready():
    #global server
    #server = bot.get_guild(618048944840245248)

    global guild
    guild = bot.get_guild(618048944840245248)
    testguild = bot.get_guild(617866004978073620)
    thischannell = bot.get_channel(632904178100076565)
    msggg = await thischannell.fetch_message(633576140409405440)

    allTimeMessages = int(msggg.content)

    #global shiki
    #shiki = server.get_member(393839495859929089)

    await bot.change_presence(activity=discord.Game(name='!help'))
    print('started.')

    await bot.wait_until_ready()
    guildd = bot.get_guild(618048944840245248)
    #print("+++++++++++++++ \n" + str(guildd) + "+++++++++++++++++++")
    #while True:
        #chann = bot.get_channel(633785042606489655)
        #await chann.send("<@393839495859929089>")
        #await asyncio.sleep(2)

    while True:
        global msgsCounterrr
        msgsCounterrr = 0
        await asyncio.sleep(3600)

# welcome message

@bot.event
async def on_member_join(member):
    if(member.guild.id == 627928375989764138):
        rol = discord.utils.get(member.guild.roles, name="Members 💖")
        await member.add_roles(rol)
        mbrcnt = bot.get_channel(628144020715077642)
        await mbrcnt.edit(name="{} LOVIES ღ".format(member.guild.member_count))
        channel = bot.get_channel(629056727186407445)
        channel2 = bot.get_channel(629849552215867405)
        channel3 = bot.get_channel(628308702587518987)
        channel4 = bot.get_channel(629061888646316032)
        embed = discord.Embed(description="Welcome to **[Ａｓｍｏｄｅｕｓ](https://discord.gg/GJ5UDth)**! You're the **{}th** member. \n\n Make sure to read: {}  \n\nRoles: {} \nColors: {}.".format(member.guild.member_count, channel2.mention, channel3.mention, channel4.mention), color=0x000000)
        embed.set_author(name="{}".format(member), icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.guild.icon_url)
        await channel.send("{}".format(member.mention), embed=embed)
        #channel4 = discord.utils.get(member.guild.channels, name="♥‿♥welcome-goodbye♥‿♥")
        #await channel4.send("Welcome to **defying ღ thots**, **{}** ({}) has joined the server. We now have **{}** members.".format(member, member.mention, member.guild.member_count))
        loggg = discord.utils.get(member.guild.channels, name="join-leave-logs")
        await loggg.send(f"{member} ({member.mention}, {member.id}) joined.")

        #await channel.send("Welcome {} to **e nightclub!** You’re the **{}** member. \n\n Make sure to read: {}  |  Roles: {}  |  For help:  {}.".format(member.mention, member.guild.member_count, channel2.mention, channel3.mention, channel4.mention))
        chan = bot.get_channel(628308702587518987)
        msg = await chan.send(f"Hi {member.mention}, check out our roles!")
        await asyncio.sleep(60)
        await msg.delete()


# leave message & join message.

@bot.event
async def on_member_remove(member):
    if(member.guild.id == 627928375989764138):
        mbrcnt = bot.get_channel(628144020715077642)
        await mbrcnt.edit(name="{} LOVIES ღ".format(member.guild.member_count))
        #channel = discord.utils.get(member.guild.channels, name="♥‿♥welcome-goodbye♥‿♥")
        #await channel.send("**{}** ({}) has left the server. We now have **{}** members.".format(member, member.mention, member.guild.member_count))
        loggg = discord.utils.get(member.guild.channels, name="join-leave-logs")
        await loggg.send(f"{member} ({member.mention}, {member.id}) left.")
# EMBED MESSAGES

@bot.event
async def on_message(message: Message):
    global msgsCounterr
    global msgsCounterrr
    global allTimeMessages
    msgsCounterr += 1
    msgsCounterrr += 1
    allTimeMessages += 1
    if message.guild is None:
        await bot.process_commands(message)
        return
    if message.content == "/get bot_invite":
        embed = discord.Embed(description="You can invite me from [here](https://discordapp.com/oauth2/authorize?client_id=594131533745356804&scope=bot&permissions=477752407)!")
        await message.channel.send(embed=embed)
    if message.content == "/get repo":
        embed = discord.Embed(description="[My insides~](https://www.github.com/Shikiiii/Asmodeus)")
        await message.channel.send(embed=embed)
    if message.channel.id == 629061888646316032:
        role_names = {"Light Red", "Light Orange", "Light Purple", "Light Yellow", "Light Cyan", "Light Blue", "Light Green", "Light Pink", "Dark Red", "Dark Blue", "Dark Purple", "Dark Pink", "Dark Red", "Crimson", "Black", "Gray", "Indigo", "Lavender", "Violet", "White", "Magenta"}
        await message.delete()
        if message.content =="none":
            toremove = []
            for role in message.author.roles:
                if role.name in role_names:
                    toremove.append(role)
            for role in toremove:
                await message.author.remove_roles(role)
            return
        new_role = discord.utils.get(message.author.guild.roles, name=message.content)
        if hasattr(new_role, "id"):
            toremove = []
            for role in message.author.roles:
                if role.name in role_names:
                    toremove.append(role)
            for role in toremove:
                await message.author.remove_roles(role)
            await message.author.add_roles(new_role)
    if message.guild.id == 627928375989764138 and message.channel.id == 627947531325669386:
        chan = discord.utils.get(message.guild.channels, name="x【lounge】x")
        await chan.send("{}".format(message.content))
    if len(message.mentions) > 0:
        if message.author.id != 594131533745356804:
            for key in afklist:
                usr = message.guild.get_member(key)
                if usr.mentioned_in(message):
                    reason = afklist[key]
                    await message.channel.send("{} is AFK: **{}**".format(usr.mention, str(reason)))
    if message.author.id in afklist:
        oldnick = str(message.author.display_name)
        newnick = oldnick[6:]
        await message.author.edit(nick="{}".format(newnick))
        del afklist[message.author.id]
        await message.channel.send("Welcome back, {}! I removed your AFK.".format(message.author.mention))
    if(message.content == "!welcome" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**༚ ✧˳⁺ __Welcome to Ａｓｍｏｄｅｕｓ!__  ⁺˳✧ ༚**", description="- We are so glad to have you join our server! By joining this server you agreed to our rules. \r\n\r\n - We have over 100+ roles, channels and some bots to play different games and much more! \r\n\r\n - Our channels are not aggressively moderated so feel free to join any conversation you like.", color=0x000000)
        embed2 = discord.Embed(color=0x000000)
        embed2.set_image(url="https://media.giphy.com/media/dXKnyjh6RfxOpEVshY/giphy.gif")
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed1)
    elif(message.content == "!rules" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**༚ ✧˳⁺ __Server rules__ ⁺˳✧ ༚**", description="__``1``__ • Make sure to follow the [Discord TOS](https://discordapp.com/terms) and the [Community Guidelines](https://discordapp.com/guidelines). \r\n\r\n __``2``__ • Keep content in the appropriate channels. This includes only posting NSFW content in NSFW marked channels. \r\n\r\n __``3``__ • No Doxing / Do not leak someone's IP address / Do not share personal information of anyone. \r\n\r\n __``4``__ • Any type of serious harassment will result in a ban. If you're not sure about whether something you've done is harassment, check out the [guidelines](https://discordapp.com/guidelines). \r\n\r\n __``5``__ • No advertising (Including PM advertisement). \r\n\r\n __``6``__ • Do NOT tell people to kill themselves (even if it's a joke). \r\n\r\n __``7``__ • Do not impersonate other users. Impersonating our staff team or discord staff will result in a permanent ban. \r\n\r\n __``8``__ • Remember that this server is English only! Try to avoid using any other languages so everyone can understand each other and have fun. \r\n\r\n __``9``__ • Respect all staff and follow their instruction(s). \r\n\r\n __``10``__ • Do NOT set people up against each other. \r\n\r\n __``11``__ • Respect people's wishes considering revealing their age, face reveal etc. \r\n\r\n __``12``__ • Asking for nudes or for other information is ABSOLUTELY not accepted here and will result in a ban. \r\n\r\n **- Please contact <@393839495859929089> if you have any issues with our staff team and/or the rules posted above.** \r\n\r\n **- Thank you for joining Ａｓｍｏｄｅｕｓ! We hope you have a great stay here!**", color=0x000000)
        embed2 = discord.Embed(color=0x000000)
        embed2.set_image(url="https://media.giphy.com/media/kD0G3PwfsUhUzQu3QQ/giphy.gif")
        embed3 = discord.Embed(title="**༚ ✧˳⁺ __Voice Chat rules__ ⁺˳✧ ༚**", description="__``1``__ • Don't ear rape other people with music or with your mic. \r\n\r\n __``2``__ • Do not spam music, let other people play their song. \r\n\r\n __``3``__ • Do not stop the music if there are still others in the voice channel. \r\n\r\n __``4``__ • Do not mic spam, yell or disturb others. \r\n\r\n __``5``__ • Do NOT be toxic or be racist.", color=0x000000)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed3)
        await message.channel.send(embed=embed1)
    elif(message.content == "!faq" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="*__**FAQ**:__*", description="__**How can I level up?**__ \r\n\r\n To level up you have to be active in any channel in the server, avoid spamming. Spamming won't level you up. \r\n\r\n __**Is there a way to get picture perms/embed links?**__ \r\n\r\n Yes there is a way to get these perms, when you reach **level 10+** you'll be able to post pictures or links.. \r\n\r\n __**Someone is advertising in my DMS what do I do?**__ \r\n\r\n Dm a staff member and they'll ban them as soon as possible. \r\n\r\n __**Staff is abusing his perms, what do I do?**__ \r\n\r\n DM <@393839495859929089>. \r\n\r\n __**Do you guys do giveaways and events?**__ \r\n\r\n Yes we do events and giveaways sometimes. \r\n\r\n __**I want to apply for a Partner Manager, how can I do that?**__ \r\n\r\n DM <@393839495859929089>.", color=0x000000)
        embed2 = discord.Embed(color=0x000000)
        embed2.set_image(url="https://media.giphy.com/media/WtISnEdn9w4jjSZNtC/giphy.gif")
        embed3 = discord.Embed(title="", description="__**Can we be partners?**__ \r\n\r\n Sure! You can be partner with us by messaging one of the PMs.\r\n\r\n __**I got banned for no reason, what do I do?**__ \r\n\r\n Simply DM the owner <@393839495859929089> and I'll unban you as soon as possible! \r\n\r\n __**Can I get a color?**__ \r\n\r\n Yes, you can pick a color form our [colors menu](https://discordapp.com/channels/627928375989764138/629061888646316032/629220377637421067). \r\n\r\n __**Someone leaked my pictures, IP, phone number. What do I do?**__ \r\n\r\n DM one of the staff members and they'll ban them. \r\n\r\n __**When was this server created?**__ \r\n\r\n created on 29/9/2019, but was released public on 14/10/2019. \r\n\r\n __**Is this a dating server?**__ \r\n\r\n Nope, this is a chill server to talk to new people and make friends. However, we won't stop you if you're dating **__AND__** you're 18 or above.", color=0x000000)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed1)
        await message.channel.send(embed=embed3)
    elif(message.content == "!staff" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**__Staff Members:__**", description="☆ - Owners: glow <@514392208254959618> | Shiki <@393839495859929089>. \r\n\r\n ☆ - Co Owners: zyzz <@543885407071371340>\r\n\r\n☆ - Admins: zip <@267631540811464704> \r\n\r\n ☆ - Mods: Alex <@444751983786852362> | System <@316988095562252290>", color=0xFF93F0)
        embed2 = discord.Embed(color=0xFF93F0)
        embed2.set_image(url="https://media.giphy.com/media/Xy1debdAWrNLK3cnHk/giphy.gif")
        embed3 = discord.Embed(title="**__Perm invite links:__**", description="🔗 Perm invite link: https://discord.gg/GJ5UDth", color=0xFF93F0)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed1)
        await message.channel.send(embed=embed3)
    elif(message.content == "!verification" and (message.author.id == 393839495859929089 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**༚ ✧˳⁺ Verification ⁺˳✧ ༚**", description="✧ - Post selfie in <#627942893448986713> with \"Shiki\" written on a piece of paper. \r\n\r\n ✧ - Verified role gives you access to <#627942990186283039> or <#627943195069775912> depends on your gender. \r\n\r\n If you're feeling uncomfortable with posting your selfie, you can DM the selfie to the owner.", color=0x000000)
        embed2 = discord.Embed(color=0xFF93F0)
        await message.channel.send(embed=embed1)
    elif message.content == "info":
        await message.channel.send("Hi! I'm currently in **{}** guilds, seeing a total of **{}** users.\n**{}** messages were sent in the past hour, and **{}** messages were sent since last restart.\n**{}** messages were sent in global (LAST RESET: 13/10/19 @ 2:55PM GTM+3)".format(len(bot.guilds), len(bot.users), msgsCounterrr, msgsCounterr, allTimeMessages))
    elif message.content == "invite":
        online = 0
        for member in message.guild.members:
            if member.status != discord.Status.offline:
                online += 1
        embed = discord.Embed(description="\n[Ａｓｍｏｄｅｕｓ](https://discord.gg/ANQSkTq) \n\n- e-girls, fun, socializing, chilling and more! \n\n⬤ {} Online ⭘ {} Members".format(online, message.guild.member_count), color=0x000000)
        embed.set_author(name="YOU'VE BEEN INVITED TO JOIN A SERVER\n", icon_url=message.author.avatar_url)
        embed.set_thumbnail(url=message.guild.icon_url)
        await message.channel.send(embed=embed)
        msg = await message.channel.send("Get the direct link DMed to you by reacting here!")
        await msg.add_reaction("📧")
        
        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '📧'
        
        try:
            reaction, user = await bot.wait_for('reaction_add', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await msg.delete()
        else:
            try:
                await message.author.send("Direct link: https://discord.gg/ANQSkTq", embed=embed)
            except:
                await message.channel.send("{}, your DMs are disabled, so I couldn't DM you the invite link!".format(ctx.message.author.mention))
            await msg.delete()
# dy  & shiki dms commands:

  #  if "xxx" in message.content:
     #   await message.author.send("Hi")
    #elif shiki in message.mentions:
        #await message.author.send(f"Hey there, {message.author.mention}! \nPlease don't abusively mention the Devs without a reason. If you want to just talk to them, it's okay, but don't don it oftenly without a real reason. But while you're here... \n\n Are you looking for **cheap** and sometimes **free** __bot developing and hosting__? Our **custom bot**, <@593090256560193549> was made by the user you just pinged, {shiki.mention}. \n\n If you're interesting in having a custom bot like this one, **DM {shiki.mention}** and we'll talk about it there. \n\n > This automatic action was fired because you pinged either the Bot Coder role or {shiki.mention}.")
    elif message.content == "shiki":
        await message.channel.send("dm <@393839495859929089> with thigh pics for free admin aha x")
    elif message.content == "!!apply":
        await message.channel.send("Thank you for applying! Please check your DMs to complete the application.")
    elif message.content == "no u" and message.author.id != 594131533745356804:
        await message.channel.send("no u")
    elif message.content == "glow":
        await message.channel.send("O_O")
    elif message.content == "alex":
        await message.channel.send("biggest retard")
    elif message.content == "kam" or message.content == "kamera":
        await message.channel.send("dm <@567799351368482826> for a Daddy :wink:")

    await bot.process_commands(message)

@bot.event
async def on_disconnect():
	chan = bot.get_channel(632904178100076565)
	msg = chan.fetch_message(632905000980316180)
	global allTimeMessages
	await msg.edit(content="{}".format(allTimeMessages))
		
@bot.command()
async def servers(ctx):
    serverss = bot.guilds
    strings = []
    for guild in serverss:
        strings.append("{}".format(guild.name))
    readme = "/n".join(strings)
    await ctx.send("```{}```".format(readme))

async def guildConvert(ctx, arg):
    try:
        guild = bot.get_guild(int(arg))
        if test is None:
            return "None"
        else:
            return guild
    except ValueError:
        guild = bot.utils.get(bot.guilds, name="{}".format(arg))
        if test is None:
            return "None"
        else:
            return guild
        

@bot.command()
async def server(ctx, *, server: guildConvert):
    hi = True
    try:
        if server == "None":
            await ctx.send("not found")
        else:
            for channel in server.channels:
                while hi:
                    invite = await.channel.create_invite()
                    await ctx.send("{}".format(invite.url))
                    hi = False
                    return
    except:
        for channel in server.channels:
            while hi:
                invite = await channel.create_invite()
                await ctx.send("{}".format(invite.url))
                hi = False
                return

tosnipe = {}
tosnipeauthors = {}
tosnipetime = {}
			
@bot.event
async def on_message_delete(message: Message):
	if message.author.bot == False:
		logch = discord.utils.get(message.author.guild.channels, name="logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Deleted a message in {}: \n{}\n\nUsers ID: {}".format(message.channel.mention, message.content, message.author.id), color=0xFFFFFF)
		log.set_author(name="{}".format(message.author), icon_url=message.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=message.author.avatar_url)
		await logch.send(embed=log)

	if message.author.bot == False:
		if message.content.startswith("!confess"):
			print("Confess was ignored from !snipe.")
		else:
			tosnipe[message.channel.id] = message.content
			tosnipeauthors[message.channel.id] = message.author
			timestamp2 = datetime.datetime.now()
			corfor = timestamp2.strftime("%d %b, %Y at %H:%M")
			tosnipetime[message.channel.id] = timestamp2
		

toeditsnipe = {}
toeditsnipeauthors = {}
toeditsnipetime = {}
	
@bot.event
async def on_message_edit(before, after):
	if before.author.bot == False:
		#print(before)
		#print(after)
		logch = discord.utils.get(before.author.guild.channels, name="logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Edited a message in {}: \n``Old:``\n{}\n``New:``\n{}\n\nUsers ID: {}".format(before.channel.mention, before.content, after.content, before.author.id), color=0xFFFFFF)
		log.set_author(name="{}".format(before.author), icon_url=before.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=before.author.avatar_url)
		await logch.send(embed=log)
		
		toeditsnipe[before.channel.id] = before.content
		toeditsnipeauthors[before.channel.id] = before.author
		timestamp2 = datetime.datetime.now()
		corfor = timestamp2.strftime("%d %b, %Y at %H:%M")
		toeditsnipetime[before.channel.id] = timestamp2
# BETA COMMANDS:
takenBotSurvey = []
takenServerSurvey = []
curBotSurvey = []
curServerSurvey = []

@bot.command()
async def survey(ctx):
    surveyBot = False
    surveyServer = False
    surveyBotAnswers = {}
    surveyServerAnswers = {}
    usr = ctx.message.author
    def check(m):
        return m.author.id == usr.id and m.guild is None
    if ctx.guild is None:
        if ctx.message.author.id in curBotSurvey or ctx.message.author.id in curServerSurvey:
            await ctx.send("Not gonna lie, but I think you're already taking a survey.")
            return
        botAv = " "
        serverAv = " "
        if ctx.message.author.id in takenBotSurvey:
            botAv = ":x:"
        else:
            botAv = "``1``"
        if ctx.message.author.id in takenServerSurvey:
            serverAv = ":x:"
        else:
            serverAv = "``2``"
        await asyncio.sleep(1)
        await ctx.send(f"Alright, {ctx.message.author.mention}. Thanks for taking your time to answer the surveys. Here are the current surveys:\n\n   {botAv} **BOT SURVEY**\n   {serverAv} **SERVER SURVEY**\n\nRespond with either 1 or 2.")
        #print(takenServerSurvey + " " + takenBotSurvey)
        msg1 = await bot.wait_for('message', check=check)
        if (msg1.content == "2") and (usr.id not in takenServerSurvey):
            surveyServer = True
            curServerSurvey.append(usr.id)
        elif (msg1.content == "1") and (usr.id not in takenBotSurvey):
            surveyBot = True
            curBotSurvey.append(usr.id)
        else:
            await usr.send("You've either already taken this survey or you didn't enter a correct number. Try again.")
            return
    if surveyBot:
        await usr.send("You're now taking the **bot survey**. Cancel anytime using ``cancel``.")
        await usr.send("**QUESTION 1**: What features do you currently use of the bot?")
        msg1 = await bot.wait_for('message', check=check)
        if msg1.content == "cancel":
            await usr.send("Canceling the survey. All answers are getting wiped out...")
            curBotSurvey.remove(usr.id)
            return
        else:
            surveyBotAnswers['answer1'] = msg1.content
        await asyncio.sleep(1)
        await usr.send("**QUESTION 2**: If you don't use the bot, what features would make you use it?")
        msg2 = await bot.wait_for('message', check=check)
        if msg2.content == "cancel":
            await usr.send("Canceling the survey. All answers are getting wiped out...")
            curBotSurvey.remove(usr.id)
            return
        else:
            surveyBotAnswers['answer2'] = msg2.content
        await asyncio.sleep(1)
        await usr.send("**QUESTION 3**: What features are currently not in the bot that are required in every bot?")
        msg3 = await bot.wait_for('message', check=check)
        if msg3.content == "cancel":
            await usr.send("Canceling the survey. All answers are getting wiped out...")
            curBotSurvey.remove(usr.id)
            return
        else:
            surveyBotAnswers['answer3'] = msg3.content
        await asyncio.sleep(1)
        await usr.send("**QUESTION 4**: Is the bot good enough for you to add it to your server yet?")
        msg4 = await bot.wait_for('message', check=check)
        if msg4.content == "cancel":
            await usr.send("Canceling the survey. All answers are getting wiped out...")
            curBotSurvey.remove(usr.id)
            return
        else:
            surveyBotAnswers['answer4'] = msg4.content
        await asyncio.sleep(1)
        await usr.send("**QUESTION 5**: If you answered ``no`` on the previous question, what features are still required so you'd add the bot to your server?")
        msg5 = await bot.wait_for('message', check=check)
        if msg5.content == "cancel":
            await usr.send("Canceling the survey. All answers are getting wiped out...")
            curBotSurvey.remove(usr.id)
            return
        else:
            surveyBotAnswers['answer5'] = msg5.content
        await asyncio.sleep(1)
        await usr.send("**QUESTION 6**: Do you think the bot's name should be changed?")
        msg6 = await bot.wait_for('message', check=check)
        if msg6.content == "cancel":
            await usr.send("Canceling the survey. All answers are getting wiped out...")
            curBotSurvey.remove(usr.id)
            return
        else:
            surveyBotAnswers['answer6'] = msg6.content
        await asyncio.sleep(1)
        await usr.send("**QUESTION 7**: If the developer team makes the bot better, would you consider donating?")
        msg7 = await bot.wait_for('message', check=check)
        if msg7.content == "cancel":
            await usr.send("Canceling the survey. All answers are getting wiped out...")
            curBotSurvey.remove(usr.id)
            return
        else:
            surveyBotAnswers['answer7'] = msg7.content
        await asyncio.sleep(1)
        await usr.send("**QUESTION 8**: Anything else to say?")
        msg8 = await bot.wait_for('message', check=check)
        if msg8.content == "cancel":
            await usr.send("Canceling the survey. All answers are getting wiped out...")
            curBotSurvey.remove(usr.id)
            return
        else:
            surveyBotAnswers['answer8'] = msg8.content
        await asyncio.sleep(1)
        await usr.send("Alright, sending your answers to the dev team. Thank you for your support.")
        takenBotSurvey.append(usr.id)
        curBotSurvey.remove(usr.id)
        shiki = await bot.fetch_user(393839495859929089)
        await shiki.send(f"NEW BOT SURVEY TAKEN ({usr}, {usr.id}). ANSWERS:")
        for answer, value in surveyBotAnswers.items():
            await shiki.send(f"{value}\n----------------------")

    if surveyServer:
        await usr.send("You're now taking the **server survey**. Cancel anytime using ``cancel``.")
        await usr.send("**QUESTION 1**: What do you think about the server in its current state?")
        msg1 = await bot.wait_for('message', check=check)
        if msg1.content == "cancel":
            await usr.send("Canceling the survey. All answers are getting wiped out...")
            curServerSurvey.remove(usr.id)
            return
        else:
            surveyServerAnswers['answer1'] = msg1.content
        await asyncio.sleep(1)
        await usr.send("**QUESTION 2**: What do you think will speed up the server growth?")
        msg2 = await bot.wait_for('message', check=check)
        if msg2.content == "cancel":
            await usr.send("Canceling the survey. All answers are getting wiped out...")
            curServerSurvey.remove(usr.id)
            return
        else:
            surveyServerAnswers['answer2'] = msg2.content
        await asyncio.sleep(1)
        await usr.send("**QUESTION 3**: What do you think will boost the server activity?")
        msg3 = await bot.wait_for('message', check=check)
        if msg3.content == "cancel":
            await usr.send("Canceling the survey. All answers are getting wiped out...")
            curServerSurvey.remove(usr.id)
            return
        else:
            surveyServerAnswers['answer3'] = msg3.content
        await asyncio.sleep(1)
        await usr.send("**QUESTION 4**: If we gave you nitro, would you boost our server?")
        msg4 = await bot.wait_for('message', check=check)
        if msg4.content == "cancel":
            await usr.send("Canceling the survey. All answers are getting wiped out...")
            curServerSurvey.remove(usr.id)
            return
        else:
            surveyServerAnswers['answer4'] = msg4.content
        await asyncio.sleep(1)
        await usr.send("**QUESTION 5**: Would you be active if the chat is active too?")
        msg5 = await bot.wait_for('message', check=check)
        if msg5.content == "cancel":
            await usr.send("Canceling the survey. All answers are getting wiped out...")
            curServerSurvey.remove(usr.id)
            return
        else:
            surveyServerAnswers['answer5'] = msg5.content
        await asyncio.sleep(1)
        await usr.send("**QUESTION 6**: Why do people stay in a server, and what improvements to our server would make people stay in it and possibly be active?")
        msg6 = await bot.wait_for('message', check=check)
        if msg6.content == "cancel":
            await usr.send("Canceling the survey. All answers are getting wiped out...")
            curServerSurvey.remove(usr.id)
            return
        else:
            surveyServerAnswers['answer6'] = msg6.content
        await asyncio.sleep(1)
        await usr.send("**QUESTION 7**: Anything left to say?")
        msg7 = await bot.wait_for('message', check=check)
        if msg7.content == "cancel":
            await usr.send("Canceling the survey. All answers are getting wiped out...")
            curServerSurvey.remove(usr.id)
            return
        else:
            surveyServerAnswers['answer7'] = msg7.content
        await asyncio.sleep(1)
        await usr.send("Alright, sending your answers to the server owners. Thank you for your support.")
        takenServerSurvey.append(usr.id)
        curServerSurvey.remove(usr.id)
        shiki = await bot.fetch_user(393839495859929089)
        await shiki.send(f"NEW SERVER SURVEY TAKEN ({usr}, {usr.id}). ANSWERS:")
        for answer, value in surveyServerAnswers.items():
            await shiki.send(f"{value}\n----------------------")




# - Afk command:
afklist = {}

@bot.command()
async def afk(ctx, *, reason: str):
	#global afklist
	user = ctx.message.author
	oldnick = str(user.display_name)
	try:
		await user.edit(nick="[AFK] {}".format(oldnick))
	except:
		embed = discord.Embed(description="Your role is higher or equal to mines, no [AFK] to your nickname.", color=0xebf533)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	if len(reason) == 0:
		if str(ctx.message.author.id) not in afklist.keys():
			afklist[user.id] = reason
			list = ["Fapping to pornhub.com", "Fuckin yo mom", "Doin something", "Im too lazy to type what I'm afk for", "Hi"]
			afkk = random.choice(list)
			await ctx.send("{}, I set your AFK: **{}**.".format(ctx.message.author.mention, afkk))
			#return
	elif len(reason) > 0:
		if str(ctx.message.author.id) not in afklist.keys():
			afklist[user.id] = reason
			await ctx.send("{}, I set your AFK: **{}**.".format(ctx.message.author.mention, reason))
			#return

@afk.error
async def afk_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		user = ctx.message.author
		oldnick = str(user.display_name)
		try:
			await user.edit(nick="[AFK] {}".format(oldnick))
		except:
			embed = discord.Embed(description="Your role is higher or equal to mines, no [AFK] to your nickname.", color=0xebf533)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
		if str(ctx.message.author.id) not in afklist.keys():
			afklist[user.id] = reason
			list = ["Fapping to pornhub.com", "Fuckin yo mom", "Doin something", "Im too lazy to type what I'm afk for", "Hi"]
			afkk = random.choice(list)
			await ctx.send("{}, I set your AFK: **{}**.".format(ctx.message.author.mention, afkk))
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

# - Fun Commands:
@bot.command()
async def help(ctx, *, mdl: str):
	selfbotasmember = ctx.guild.get_member(594131533745356804)
	print(selfbotasmember)
	if mdl == "general":
		embed = discord.Embed(title="Module: General", description="To view more info about a command, use ``!cmdhelp command``.", color=0x000000)
		embed.add_field(name="Commands:", value="``afk``, ``define``, ``ping``, ``snipe``, ``editsnipe``, ``reminder``, ``remindercancel``, ``reminderdm``, ``reminderdmcancel``, ``avatar``, ``avatarid``, ``userinfo``")
		embed.set_author(name="{}".format(str(bot.user.name)), icon_url=str(bot.user.avatar_url))
		await ctx.send(embed=embed)
	elif mdl == "fun":
		embed = discord.Embed(title="Module: Fun", description="To view more info about a command, use ``!cmdhelp command``.", color=0x000000)
		embed.add_field(name="Commands:", value="``kiss``, ``hug``, ``cuddle``, ``slap``, ``howgay``, ``howlesbian``, ``thotrate``, ``8ball``, ``rate``, ``roast``, ``penis``, ``ship``, ``coinflip``")
		embed.set_author(name="{}".format(str(bot.user.name)), icon_url=str(bot.user.avatar_url))
		await ctx.send(embed=embed)
	elif mdl == "mod":
		embed = discord.Embed(title="Module: Moderation", description="To view more info about a command, use ``!cmdhelp command``.", color=0x000000)
		embed.add_field(name="Commands:", value="``kick``, ``mute``, ``unmute``, ``purge``, ``clean``, ``serverinfo``, ``membercount``")
		embed.set_author(name="{}".format(str(bot.user.name)), icon_url=str(bot.user.avatar_url))
		await ctx.send(embed=embed)
	elif mdl == "admin":
		embed = discord.Embed(title="Module: Administration", description="To view more info about a command, use ``!cmdhelp command``.", color=0x000000)
		embed.add_field(name="Commands:", value="``members``, ``ban``, ``banid``, ``unban``, ``role``, ``bots``, ``lockdown``")
		embed.set_author(name="{}".format(str(bot.user.name)), icon_url=str(bot.user.avatar_url))
		await ctx.send(embed=embed)
	elif mdl == "bot_owners":		
		embed = discord.Embed(title="Module: Owners", description="To view more info about a command, use ``!cmdhelp command``.", color=0x000000)
		embed.add_field(name="Commands:", value="``say``, ``status``")
		embed.set_author(name="{}".format(str(bot.user.name)), icon_url=str(bot.user.avatar_url))
		await ctx.send(embed=embed)
	else:
		embed = discord.Embed(title="Modules:", description="``!help general`` | General Commands\n``!help fun`` | Fun Commands\n``!help mod`` | Moderation Commands\n``!help admin`` | Administration Commands\n``!help bot_owners`` | Bot Owners Commands", color=0x000000)
		embed.set_author(name="{}".format(str(bot.user.name)), icon_url=str(bot.user.avatar_url))
		await ctx.send(embed=embed)
		
@help.error
async def help_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Modules:", description="``!help general`` | General Commands\n``!help fun`` | Fun Commands\n``!help mod`` | Moderation Commands\n``!help admin`` | Administration Commands\n``!help bot_owners`` | Bot Owners Commands", color=0x000000)
		embed.set_author(name="{}".format(str(bot.user.name)), icon_url=str(bot.user.avatar_url))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def cmdhelp(ctx, *, cmd: str):
	if(cmd == "help"):
		embed = discord.Embed(title="!help [module]", description="Gets the help menu with the modules / of a module. It includes all commands.\n\nExample: ``!help fun``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "afk"):
		embed = discord.Embed(title="!afk [message]", description="Sets your AFK, the [message] will be displayed whenever someone @mentions you.\n\nExample: ``!afk eating``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "define"):
		embed = discord.Embed(title="!define [term]", description="Searches for a definition in UrbanDictionary.\nAlias: ``!urban``.\n\nExample: ``!define jkjk``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "ping"):
		embed = discord.Embed(title="!ping", description="Gets the bot's ping.", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "snipe"):
		embed = discord.Embed(title="!snipe", description="Gets the last deleted message in the channel.", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "editsnipe"):
		embed = discord.Embed(title="!editsnipe", description="Gets the last edited message in the channel, showing the message before the edit.", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "reminder"):
		embed = discord.Embed(title="!reminder [time] [message]", description="Sets a reminder that will be send in the channel you used the command in. Correct time uses are ``s`` for seconds, ``m`` for minutes, ``h`` for hours and ``d`` for days. Maximum is 7 days. You are allowed to 1 reminder at the same time. \n\nExample: ``!reminder 2h read that new book I got``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "remindercancel"):
		embed = discord.Embed(title="!remindercancel", description="Cancels your current reminder.", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "reminderdm"):
		embed = discord.Embed(title="!reminderdm [time] [message]", description="Sets a reminder that will be send in your DMs. Correct time uses are ``s`` for seconds, ``m`` for minutes, ``h`` for hours and ``d`` for days. Maximum is 7 days. You are allowed to 1 reminder at the same time. \n\nExample: ``!reminderdm 2h fap idk``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "reminderdmcancel"):
		embed = discord.Embed(title="!reminderdmcancel", description="Cancels your current DM reminder.", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "avatar"):
		embed = discord.Embed(title="!avatar [user]", description="Gets someone's avatar. Your avatar will be shown if ``user`` is None.\nAlias: ``!av``.\n\nExample: ``!avatar @Shiki``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "avatarid"):
		embed = discord.Embed(title="!aavatarid [id]", description="Gets someone's avatar. This command can get the avatar of a user that's not in the server. Works with IDs.\nAlias: ``!avid``.\n\nExample: ``!avatarid 393839495859929089``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "userinfo"):
		embed = discord.Embed(title="!userinfo [user]", description="Gets someone's account info.\nAlias: ``!uf``, ``!whois``.\n\nExample: ``!userinfo dy``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "kiss"):
		embed = discord.Embed(title="!kiss [user]", description="Kisses someone, showing a random gif from Tenor. If ``user`` is None, the command will still work.\n\nExample: ``!kiss @Shiki``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "hug"):
		embed = discord.Embed(title="!hug [user]", description="Hugs someone, showing a random gif from Tenor. If ``user`` is None, the command will still work.\n\nExample: ``!hug @dy``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "cuddle"):
		embed = discord.Embed(title="!cuddle [user]", description="Cuddles someone, showing a random gif from Tenor. If ``user`` is None, the command will still work.\n\nExample: ``!cuddle @idk``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "slap"):
		embed = discord.Embed(title="!slap [user]", description="Slaps someone, showing a random gif from Tenor. If ``user`` is None, the command will still work.\n\nExample: ``!slap @youmom``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "howgay"):
		embed = discord.Embed(title="!howgay [user]", description="Shows the gayness of the user you gave.\n\nExample: ``!howgay @dy``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "howlesbian"):
		embed = discord.Embed(title="!howlesbian [user]", description="Shows how lesbian someone is.\n\nExample: ``!howlesbian @idk``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "thotrate"):
		embed = discord.Embed(title="!thotrate [user]", description="Shows the thot rate of the user you gave.\n\nExample: ``!thotrate @Shiki(LOL NO PLEASE)``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "rate"):
		embed = discord.Embed(title="!rate [dy/shiki] [user]", description="Rates the user you gave with the rate you chose, either ``dy`` or ``shiki``.\n\nExample: ``!rate shiki @dy``", color=0x000000)
		await ctx.send(embed=embed)
	elif(cmd == "8ball"):
		embed = discord.Embed(title="!8ball [question]", description="Answers your question using magic.\n\nExample: ``!8ball am i cool?``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "roast"):
		embed = discord.Embed(title="!roast [user]", description="Roasts the user you gave. The roasts are fire.\n\nExample: ``!roast @someone``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "penis"):
		embed = discord.Embed(title="!penis [user]", description="Shows someone's pee pee size.\n\nExample: ``!penis @dy``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "ship"):
		embed = discord.Embed(title="!ship [user1] [user2]", description="Matches 2 users. Lovely.\n\nExample: ``!match @shiki @idk``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "coinflip"):
		embed = discord.Embed(title="!coinflip", description="Flips a coin. Lands either on heads or trails.\nAlias: ``!cf``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "kick"):
		embed = discord.Embed(title="!kick [user] [reason]", description="Kicks the user you gave.\n\nExample: ``!kick @dy idk``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "mute"):
		embed = discord.Embed(title="!mute [user] [reason]", description="Mutes the user you gave for permanet.\n\nExample: ``!mute @Shiki idk``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "unmute"):
		embed = discord.Embed(title="!unmute [user] [reason]", description="Unmutes the user you gave.\n\nExample: ``!unmute @Shiki idk``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "purge"):
		embed = discord.Embed(title="!purge [amount] [user]", description="Purges ``amount`` messages. User is optional. Maximum is 200.\n\nExample: ``!purge 10 @Shiki``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "clean"):
		embed = discord.Embed(title="!clean", description="Cleans up to 100 of the bot's messages in this channel.", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "serverinfo"):
		embed = discord.Embed(title="!serverinfo", description="Shows the server info.", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "membercount"):
		embed = discord.Embed(title="!membercount", description="Shows the member count of the server.", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "members"):
		embed = discord.Embed(title="!members [role]", description="Shows the members that have the given role.\n\nExample: ``!members owner``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "ban"):
		embed = discord.Embed(title="!ban [user] [reason]", description="Bans the given user.\n\nExample: ``!ban @dy idk``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "banid"):
		embed = discord.Embed(title="!banid [id]", description="Bans a user that's not in the server using their ID.\n\nExample: ``!banid 395802215190888498``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "unban"):
		embed = discord.Embed(title="!unban [id]", description="Unbans the given user with their ID.\n\nExample: ``!unban 395802215190888498``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "status"):
		embed = discord.Embed(title="!status [o/i/d] [p/w/l] [message]", description="Changes the bot's status. Online, idle or do not disturb. Playing, watching or listening to.\n\nExample: ``!status o w you sleep.``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	#elif(cmd == "verify"):
	#		embed = discord.Embed(title="!verify [user] [male/female]", description="Verifies the user to either male or female.\nAlias: ``!v``\n\nExample: ``!verify @dy m``", color=0x000000)
	#		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	#		await ctx.send(embed=embed)
	elif(cmd == "lockdown"):
		embed = discord.Embed(title="!lockdown", description="Locks the channel where the message was sent in. To unlock, type !lockdown again.", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "role"):
		embed = discord.Embed(title="!role [user] [role]", description="Gives/Removes the given role to/from the given user.\n\nExample: ``!role @Shiki retard``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "say"):
		embed = discord.Embed(title="!say [channel] [message]", description="The bot says whatever the [message] is. Channel is optional.\n\nExample: ``!say #asd asd``", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif(cmd == "bots"):
		embed = discord.Embed(title="!bots", description="Lists all the bots in the server.", color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	else:
			embed = discord.Embed(description="This isn't a valid command.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)

@bot.command()
async def nick(ctx, user: discord.Member, *, msg: str):
	if ctx.message.author.id == user.id:
		try:
			await ctx.message.author.edit(nick="{}".format(msg))
		except:
			embed = discord.Embed(description="Their role is higher or equal to mines, can't change their nickname.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
		embed = discord.Embed(description="Changed your nickname to **{}**.".format(user.mention, msg), color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_thumbnail(url=user.avatar_url)
		await ctx.send(embed=embed)
	#elif ((role1 or role2 or role3 or role4 or role5) in ctx.message.author.roles):
	#	try:
	#		await user.edit(nick="{}".format(msg))
	#	except:
	#		embed = discord.Embed(description="Their role is higher or equal to mines, can't change their nickname.", color=0xFF3639)
	#		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	##		await ctx.send(embed=embed)
	#		return
	#	embed = discord.Embed(description="Changed {}'s nickname to **{}**.".format(user.mention, msg), color=0x000000)
	#	embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	#	embed.set_thumbnail(url=user.avatar_url)
	#	await ctx.send(embed=embed)
	else:
		embed = discord.Embed(description="You can only change your own nickname with your current permissions.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	
@nick.error
async def nick_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		name = ctx.message.content[6:]
		try:
			await ctx.message.author.edit(nick="{}".format(name))
		except:
			embed = discord.Embed(description="Their role is higher or equal to mines, can't change their nickname.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
		embed = discord.Embed(description="Changed your nickname to **{}**.".format(name), color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_thumbnail(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	elif isinstance(error, commands.BadArgument):
		name = ctx.message.content[6:]
		try:
			await ctx.message.author.edit(nick="{}".format(name))
		except:
			embed = discord.Embed(description="Their role is higher or equal to mines, can't change their nickname.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
		embed = discord.Embed(description="Changed your nickname to **{}**.".format(name), color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_thumbnail(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

tenorkey = "6JKJQX4V4OHD"
limit = 50
media_filter = "basic"
kiss = "animekiss"
hug = "animehug"
slap = "animeslap"
cuddle = "animecuddle"
blush = "animeblush"

kissgifs = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (kiss, tenorkey, limit, media_filter))
huggifs = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (hug, tenorkey, limit, media_filter))
slapgifs = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (slap, tenorkey, limit, media_filter))
cuddlegifs = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (cuddle, tenorkey, limit, media_filter))
blushgifs = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (blush, tenorkey, limit, media_filter))

kiss_gifs = json.loads(kissgifs.content)
hug_gifs = json.loads(huggifs.content)
slap_gifs = json.loads(slapgifs.content)
cuddle_gifs = json.loads(cuddlegifs.content)
blush_gifs = json.loads(blushgifs.content)
			
#print(json.dumps(kiss_gifs, sort_keys=True, indent=4))
			
@bot.command()
async def kiss(ctx, *, user: discord.Member):
	embed = discord.Embed(title="{} kisses {}.".format(ctx.message.author, user), color=0x000000)
	result = random.choice(kiss_gifs["results"])
	chosen_media = result["media"][0]
	url = chosen_media["gif"]["url"]
	embed.set_image(url=url)
	await ctx.send(embed=embed)
	
@kiss.error
async def kiss_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(title="I couldn't find this member, so I'll kiss you instead.", color=0x000000)
		result = random.choice(kiss_gifs["results"])
		chosen_media = result["media"][0]
		url = chosen_media["gif"]["url"]
		embed.set_image(url=url)
		await ctx.send(embed=embed)
	elif isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Aww, looks like you're lonely, I'll kiss you.", color=0x000000)
		result = random.choice(kiss_gifs["results"])
		chosen_media = result["media"][0]
		url = chosen_media["gif"]["url"]
		embed.set_image(url=url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def hug(ctx, *, user: discord.Member):
	embed = discord.Embed(title="{} hugs {}.".format(ctx.message.author, user), color=0x000000)
	result = random.choice(hug_gifs["results"])
	chosen_media = result["media"][0]
	url = chosen_media["gif"]["url"]
	embed.set_image(url=url)
	await ctx.send(embed=embed)
	
@hug.error
async def hug_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(title="I couldn't find this member, so I'll hug you instead.", color=0x000000)
		result = random.choice(hug_gifs["results"])
		chosen_media = result["media"][0]
		url = chosen_media["gif"]["url"]
		embed.set_image(url=url)
		await ctx.send(embed=embed)
	elif isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Aww, looks like you're lonely, I'll hug you.", color=0x000000)
		result = random.choice(hug_gifs["results"])
		chosen_media = result["media"][0]
		url = chosen_media["gif"]["url"]
		embed.set_image(url=url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def slap(ctx, *, user: discord.Member):
	embed = discord.Embed(title="{} slaps {}.".format(ctx.message.author, user), color=0x000000)
	result = random.choice(slap_gifs["results"])
	chosen_media = result["media"][0]
	url = chosen_media["gif"]["url"]
	embed.set_image(url=url)
	await ctx.send(embed=embed)
	
@slap.error
async def slap_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(title="I couldn't find this member, so I'll slap you instead.", color=0x000000)
		result = random.choice(slap_gifs["results"])
		chosen_media = result["media"][0]
		url = chosen_media["gif"]["url"]
		embed.set_image(url=url)
		await ctx.send(embed=embed)
	elif isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Aww, looks like you're too weak to slap someone, so I'll slap you.", color=0x000000)
		result = random.choice(slap_gifs["results"])
		chosen_media = result["media"][0]
		url = chosen_media["gif"]["url"]
		embed.set_image(url=url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def cuddle(ctx, *, user: discord.Member):
	embed = discord.Embed(title="{} cuddles {}.".format(ctx.message.author, user), color=0x000000)
	result = random.choice(cuddle_gifs["results"])
	chosen_media = result["media"][0]
	url = chosen_media["gif"]["url"]
	embed.set_image(url=url)
	await ctx.send(embed=embed)
	
@cuddle.error
async def cuddle_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(title="I couldn't find this member, so I'll cuddle you instead.", color=0x000000)
		result = random.choice(cuddle_gifs["results"])
		chosen_media = result["media"][0]
		url = chosen_media["gif"]["url"]
		embed.set_image(url=url)
		await ctx.send(embed=embed)
	elif isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Aww, looks like you're lonely, I'll cuddle you.", color=0x000000)
		result = random.choice(cuddle_gifs["results"])
		chosen_media = result["media"][0]
		url = chosen_media["gif"]["url"]
		embed.set_image(url=url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def blush(ctx):
	embed = discord.Embed(title="{} blushes.".format(ctx.message.author), color=0x000000)
	result = random.choice(blush_gifs["results"])
	chosen_media = result["media"][0]
	url = chosen_media["gif"]["url"]
	embed.set_image(url=url)
	await ctx.send(embed=embed)

conn = http.client.HTTPSConnection("mashape-community-urban-dictionary.p.rapidapi.com")

	
@bot.command()
async def define(ctx, *, term: str):
	headers = {
		'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
		'x-rapidapi-key': "41e03ab49dmsh4d6a1ebe8db51dep1009b5jsnc4d2da773e2f"
	}
	conn.request("GET", f"/define?term={term}", headers=headers)
	try:
		res = conn.getresponse()
	except:
		embed = discord.Embed(description="No definition found.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
		
	list = res.read()
	my_json = json.loads(list)
	
	try:
		entry = my_json["list"][0]
	except IndexError:
		embed = discord.Embed(description="No definition found.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
		
	if len(entry["example"]) == 0:
		entry["example"] = "-"
	
	embed = discord.Embed(title=f"Definition of {entry['word']}", description=f"``Top Definition``\n{entry['definition']}\n\n ``Example``\n{entry['example']}\n\n :thumbsup: {entry['thumbs_up']} | :thumbsdown: {entry['thumbs_down']}", color=0x000000)
	embed.set_footer(text=f"Powered by UrbanDictionary")
	embed.set_thumbnail(url=ctx.message.author.avatar_url)
	
	
	await ctx.send(embed=embed)

@define.error
async def define_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="How did this error get raised to begin with?", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="Can't define nothing.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def urban(ctx, *, term: str):
	headers = {
		'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
		'x-rapidapi-key': "41e03ab49dmsh4d6a1ebe8db51dep1009b5jsnc4d2da773e2f"
	}
	conn.request("GET", f"/define?term={term}", headers=headers)
	try:
		res = conn.getresponse()
	except:
		embed = discord.Embed(description="No definition found.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
		
	list = res.read()
	my_json = json.loads(list)
	
	try:
		entry = my_json["list"][0]
	except IndexError:
		embed = discord.Embed(description="No definition found.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
		
	if len(entry["example"]) == 0:
		entry["example"] = "-"
	
	embed = discord.Embed(title=f"Definition of {entry['word']}", description=f"``Top Definition``\n{entry['definition']}\n\n ``Example``\n{entry['example']}\n\n :thumbsup: {entry['thumbs_up']} | :thumbsdown: {entry['thumbs_down']}", color=0x000000)
	embed.set_footer(text=f"Powered by UrbanDictionary")
	embed.set_thumbnail(url=ctx.message.author.avatar_url)
	
	
	await ctx.send(embed=embed)

@urban.error
async def urban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="How did this error get raised to begin with?", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="Can't define nothing.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def penis(ctx, *, user: discord.Member):
	sizes = ["8D", "8=D", "8==D", "8===D", "8====D", "8=====D", "8======D", "8=======D", "8========D", "8=========D", "8==========D", "8===========D", "8============D", "8=============D", "8==============D", "8===============D"]
	if user.id == 393839495859929089:
		size = "sorry bro, my dick so big this message can't fit it, for more info ask your mom, ily"
	else:
		size = random.choice(sizes)
	embed = discord.Embed(description=f"{user}'s pee pee size \n\n{size}", color=0x000000)
	embed.set_author(name=f"{ctx.message.author}", icon_url=ctx.message.author.avatar_url)
	embed.set_thumbnail(url=user.avatar_url)
	await ctx.send(embed=embed)

@penis.error
async def penis_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="How did this error get raised to begin with?", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        sizes = ["8D", "8=D", "8==D", "8===D", "8====D", "8=====D", "8======D", "8=======D", "8========D", "8=========D", "8==========D", "8===========D", "8============D", "8=============D", "8==============D", "8===============D"]
        size = random.choice(sizes)
        embed = discord.Embed(description=f"{ctx.message.author}'s pee pee size \n\n{size}", color=0x000000)
        embed.set_author(name=f"{ctx.message.author}", icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Owner")
async def say(ctx, chan: discord.TextChannel, *, msg: str=""):
	#channels = ctx.message.channel_mentions
	#if len(channels) > 0:
		#for channel in channels:
	await ctx.message.delete()
	try:
		await chan.send(f"{msg}")
	except discord.HTTPException as exception:
		ilove = ["Shiki", "Dy"]
		you = random.choice(ilove)
		await chan.send(f"I love {you}.")
	

@say.error
async def say_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		tosend = ctx.message.content[5:]
		await ctx.message.delete()
		await ctx.send(f"{tosend}")
	elif isinstance(error, commands.MissingRequiredArgument):
		await ctx.message.delete()
		ilove = ["Shiki", "Glow"]
		you = random.choice(ilove)
		await ctx.send(f"I love {you}.")
	elif isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def thotrate(ctx, *, user: discord.Member):
    les = random.randint(0, 100)
    embed = discord.Embed(description="{} is a **{}**% thot. <:shiki_is_cool:612767957570945024>".format(user.mention, str(les)),
                          color=0xef42f5)
    embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

@thotrate.error
async def thotrate_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this member.", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        les = random.randint(0, 100)
        embed = discord.Embed(
            description="{} is a **{}**% thot. <:shiki_is_cool:612767957570945024>".format(ctx.message.author.mention, str(les)),
            color=0xef42f5)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def howlesbian(ctx, *, user: discord.Member):
    les = random.randint(0, 101)
    embed = discord.Embed(description="{} is **{}**% lesbian. <:lesbian22:612745721883656203>".format(user.mention, str(les)),
                          color=0xef42f5)
    embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

@howlesbian.error
async def howlesbian_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this member.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        les = random.randint(0, 101)
        embed = discord.Embed(
            description="{} is **{}**% lesbian. <:lesbian22:612745721883656203>".format(ctx.message.author.mention, str(les)),
            color=0xef42f5)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def ping(ctx):
    #print("Testing ping!")
    delta = datetime.datetime.now() - ctx.message.created_at
    delta_ping = round(delta.microseconds / 1000)
    if delta_ping < 100:
        embed = discord.Embed(title=f"Pong! :ping_pong:",
                              description=":heartbeat: **{}ms**".format(delta_ping),
                              color=0x00ff00)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.message.channel.send(embed=embed)
        return
    elif delta_ping < 200:
        embed = discord.Embed(title=f"Pong! :ping_pong:",
                              description=":heartbeat: **{}ms**".format(delta_ping),
                              color=0xfe9a2e)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await message.channel.send(embed=embed)
        return
    else:
        embed = discord.Embed(title=f"Pong! :ping_pong:",
                              description=":heartbeat: **{}ms**".format(delta_ping),
                              color=0xff0000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.message.channel.send(embed=embed)
		
@bot.command(name="8ball")
async def ball(ctx, *, message: str):
	if len(message) > 0:
		responds = ["yes duh", "no wtf", "ig?", "naw", "pew pew", "ur mom a hoe", "u retarded fuck, its obv yes", "ew, no", "ur pp smol", "ye", "no u", "as i see it nigga, yes", "without a fucking doubt", "tbh most likely", "sorry to inform that its a yes", "i doubt that fr", "ofc its a fucking no", "sorry nigga, but its a no", "what the fuck"]
		choice = random.choice(responds)
		embed1 = discord.Embed(description="__8Ball__\n\n...", color=0xffffff)
		embed1.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		msg = await ctx.send(embed=embed1)
		await asyncio.sleep(1)
		embed2 = discord.Embed(description="__8Ball__\n\n**{}**".format(choice), color=0xf252e8)
		embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await msg.edit(embed=embed2)
	else:
		embed1 = discord.Embed(description="__8Ball__\n\nI couldn't answer you because you didn't give me a question.", color=0x000000)
		embed1.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed1)
		
@ball.error
async def ball_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="How did this error get raised to begin with?", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="__8Ball__\n\nI couldn't answer you because you didn't give me a question.", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def roast(ctx, *, user: discord.Member):
	responds = ["are you sure youre not mentally retarded?", "that's gay..", "can't roast him, he doesn't have parents", "this is why no one likes you", "just stfu retard", "they got no balls dawg", "can u speak chong bong?", "what u want pussy?", "!!", "couldn't roast"]
	choice = random.choice(responds)
	embed2 = discord.Embed(description="{}".format(choice), color=0xf252e8)
	embed2.set_author(name="{}".format(user), icon_url=user.avatar_url)
	embed2.set_footer(text="Roasted by {}".format(ctx.message.author))
	await ctx.send(embed=embed2)
		
@roast.error
async def roast_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this member. No roasing.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="Give me a member to roast.", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def ship(ctx, user: discord.Member, user2: discord.Member):
    percent = random.randint(0, 100)
    strr = " "
    if percent < 11 and percent > 0:
        strr = "horrible"
    if percent < 21 and percent > 10:
        strr = "very bad"
    if percent < 31 and percent > 20:
        strr = "bad"
    if percent < 41 and percent > 30:
        strr = "worse than avarage"
    if percent < 51 and percent > 40:
        strr = "avarage"
    if percent < 61 and percent > 50:
        strr = "better than avarage"
    if percent == 69:
        strr = ":wink:"
    if percent < 71 and percent > 69 and percent < 69 and percent > 60:
        strr = "good"
    if percent == 68:
        strr = "good"
    if percent < 81 and percent > 70:
        strr = "very good"
    if percent < 91 and percent > 80:
        strr = "almost perfect"
    if percent < 101 and percent > 90:
        strr = "amazing"
    embed = discord.Embed(title=":two_hearts:  MATCHMAKING: :two_hearts: ", description="**{}** :heart: **{}**\n\n**{}%**! That's **{}**.".format(user.name, user2.name, str(percent), strr), color=0x000000)
    await ctx.send(embed=embed)

@ship.error
async def ship_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="You didn't give me 2 correct users.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="You didn't give me 2 users.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def rate(ctx, who, *, user: discord.Member):
    if who == "dy":
        cool = random.randint(0,10)
        embed = discord.Embed(title="👀", description="{} is a **{}**/10.".format(user.mention, str(cool)), color=0xffffff)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    #    embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text="Rated by Dy")
        await ctx.send(embed=embed)
        return
    if who == "shiki":
        cool = random.randint(0,10)
        embed = discord.Embed(title="<:thonk:611367036282732574>", description="{} is a **{}**/10. <a:smileg:611367087201320991>".format(user.mention, str(cool)), color=0x4287f5)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    #    embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text="Rated by Shiki")
        await ctx.send(embed=embed)
        return
    else:
        embed = discord.Embed(description="You didn't provide a valid argument, ``rate`` accepts only **dy** and **shiki**.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
        return

@rate.error
async def rate_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this member.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="You actually have to give me a member to rate.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def howgay(ctx, *, user: discord.Member):
    gay = random.randint(0,101)
    embed = discord.Embed(description="{} is **{}**% gay. :gay_pride_flag:".format(user.mention, str(gay)), color=0xef42f5)
    embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

@howgay.error
async def howgay_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this member.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="Just give me a member and I'll tell you their gayness.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def howhot(ctx, *, user: discord.Member):
    gay = random.randint(0,101)
    embed = discord.Embed(description="{} is **{}**% hot. :sweat_drops:".format(user.mention, str(gay)), color=0xef42f5)
    embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)

@howgay.error
async def howhot_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this member.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="Just give me a member and I'll tell you their hotness(?).", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def coinflip(ctx):
    embed1 = discord.Embed(description="Flipping... \n\nResults:", color=0xffffff)
    embed1.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    msg = await ctx.send(embed=embed1)
    await asyncio.sleep(5)
    rn = random.randint(0,100)
    results = " "
    if rn < 51:
        results = "HEADS"
    if rn > 50:
        results = "TAILS"
    embed2 = discord.Embed(description="Flipped. \n\nResults: **{}**.".format(results), color=0xe9f542)
    embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    await msg.edit(embed=embed2)

@bot.command()
async def cf(ctx):
    embed1 = discord.Embed(description="Flipping... \n\nResults:", color=0xffffff)
    embed1.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    msg = await ctx.send(embed=embed1)
    await asyncio.sleep(5)
    rn = random.randint(0,100)
    results = " "
    if rn < 51:
        results = "HEADS"
    if rn > 50:
        results = "TAILS"
    embed2 = discord.Embed(description="Flipped. \n\nResults: **{}**.".format(results), color=0xe9f542)
    embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    await msg.edit(embed=embed2)

@bot.command()
async def snipe(ctx):
	for key in tosnipe:
		if key == ctx.message.channel.id:
			msg = tosnipe[key]
			author = tosnipeauthors[key]
			time = tosnipetime[key]
			embed = discord.Embed(description="{}".format(str(msg)), color=0x000000)
			embed.set_author(name="{}".format(author), icon_url=author.avatar_url)
			corfor = time.strftime("%d %b, %Y at %H:%M")
			embed.set_footer(text="{}".format(str(corfor)))
			await ctx.send(embed=embed)

@bot.command()
async def editsnipe(ctx):
	for key in toeditsnipe:
		if key == ctx.message.channel.id:
			msg = toeditsnipe[key]
			author = toeditsnipeauthors[key]
			time = toeditsnipetime[key]
			embed = discord.Embed(description="{}".format(str(msg)), color=0x000000)
			embed.set_author(name="{}".format(author), icon_url=author.avatar_url)
			corfor = time.strftime("%d %b, %Y at %H:%M")
			embed.set_footer(text="{}".format(str(corfor)))
			await ctx.send(embed=embed)

# - Reminder Commands:
remindersserver = []

@bot.command()
async def reminder(ctx, intime, *, remindmsg: str=""):
	if ctx.message.author.id in remindersserver:
		embed = discord.Embed(description="You already have an ongoing reminder! If you want to make a new one, you have to remove the old one using ``!remindercancel``.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
	if len(remindmsg) == 0:
			embed = discord.Embed(description="Fatal error. Check the ``message`` parameter and try again. Please note that __you need to give me a message to remind you with__.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
	else:
		n = intime[:-1]
		type = intime[-1]

		try:
			number = int(n)
		except:
			embed = discord.Embed(description="Fatal error. Check the ``time`` parameter and try again. Please note that **this is a correct format**: 3s (3 seconds), 5m (5 minutes), 7h (7 hours), 1d (1 day). There is also a limit of 7 days.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
		if type == "s":
			if number > 604800:
				embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
			embed = discord.Embed(description="Alright, I'll remind you in **{}** second(s). I'll only notify you in here. To have a DMs reminder, use !remiderdm. Your reminder message is ``{}``.".format(str(number), remindmsg), color=0x03fc03)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			#embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder too.")
			remindersserver.append(ctx.message.author.id)
			await ctx.send(embed=embed)
			#await ctx.send(embed=embed2)
			
			await asyncio.sleep(float(number))
			
			if ctx.message.author.id in remindersserver:
				embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
				await ctx.send("{},".format(ctx.message.author.mention))
				await ctx.send(embed=embed)
				#try:
				#	await ctx.message.author.send(embed=embed)
				#except discord.HTTPException as exception:
				#	
				remindersserver.remove(ctx.message.author.id)
				return
			else:
				return
		if type == "m":
			if number > 10080:
				embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
			embed = discord.Embed(description="Alright, I'll remind you in **{}** minute(s). I'll only notify you in here. To have a DMs reminder, use !remiderdm. Your reminder message is ``{}``.".format(str(number), remindmsg), color=0x03fc03)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			#embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder too.")
			remindersserver.append(ctx.message.author.id)
			await ctx.send(embed=embed)
			#await ctx.send(embed=embed2)
			
			await asyncio.sleep(float(number) * 60)
			
			if ctx.message.author.id in remindersserver:
				embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
				await ctx.send("{},".format(ctx.message.author.mention))
				await ctx.send(embed=embed)
				#try:
				#	await ctx.message.author.send(embed=embed)
				#except discord.HTTPException as exception:
				#	
				remindersserver.remove(ctx.message.author.id)
				return
			else:
				return
		if type == "h":
			if number > 168:
				embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
			embed = discord.Embed(description="Alright, I'll remind you in **{}** hour(s). I'll only notify you in here. To have a DMs reminder, use !remiderdm. Your reminder message is ``{}``.".format(str(number), remindmsg), color=0x03fc03)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			#embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder too.")
			remindersserver.append(ctx.message.author.id)
			await ctx.send(embed=embed)
			#await ctx.send(embed=embed2)
			
			await asyncio.sleep(float(number) * 60 * 60)
			
			if ctx.message.author.id in remindersserver:
				embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
				await ctx.send("{},".format(ctx.message.author.mention))
				await ctx.send(embed=embed)
				#try:
				#	await ctx.message.author.send(embed=embed)
				#except discord.HTTPException as exception:
				#	
				remindersserver.remove(ctx.message.author.id)
				return
			else:
				return
		if type == "d":
			if number > 7:
				embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
			embed = discord.Embed(description="Alright, I'll remind you in **{}** day(s). I'll only notify you in here. To have a DMs reminder, use !remiderdm. Your reminder message is ``{}``.".format(str(number), remindmsg), color=0x03fc03)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			#embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder too.")
			remindersserver.append(ctx.message.author.id)
			await ctx.send(embed=embed)
			#await ctx.send(embed=embed2)
			
			await asyncio.sleep(float(number) * 60 * 60 * 24)
			
			if ctx.message.author.id in remindersserver:
				embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
				await ctx.send("{},".format(ctx.message.author.mention))
				await ctx.send(embed=embed)
				#try:
				#	await ctx.message.author.send(embed=embed)
				#except discord.HTTPException as exception:
				#	
				remindersserver.remove(ctx.message.author.id)
				return
			else:
				return
				
@reminder.error
async def reminder_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="Fatal error. Are you sure you're giving me a member?", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="You're missing required arguments. Here's an example of how to use this command: \n``!reminder 3h going to appreciate this godly command``", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def remindercancel(ctx):
	if ctx.message.author.id in remindersserver:
		embed = discord.Embed(description="Reminder successfully canceled.", color=0xffffff)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		remindersserver.remove(ctx.message.author.id)
	else:
		embed = discord.Embed(description="You don't have a reminder to cancel. Set one by using ``!reminder``.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)

remindersdm = []

@bot.command()
async def reminderdm(ctx, intime, *, remindmsg: str=""):
	if ctx.message.author.id in remindersdm:
		embed = discord.Embed(description="You already have an ongoing reminder! If you want to make a new one, you have to remove the old one using ``!remindercancel``.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
	if len(remindmsg) == 0:
			embed = discord.Embed(description="Fatal error. Check the ``message`` parameter and try again. Please note that __you need to give me a message to remind you with__.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
	else:
		n = intime[:-1]
		type = intime[-1]
		
		try:
			number = int(n)
		except:
			embed = discord.Embed(description="Fatal error. Check the ``time`` parameter and try again. Please note that **this is a correct format**: 3s (3 seconds), 5m (5 minutes), 7h (7 hours), 1d (1 day). There is also a limit of 7 days.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
		if type == "s":
			if number > 604800:
				embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
			embed = discord.Embed(description="Alright, I'll remind you in **{}** second(s). I'll notify you in DMs. Your reminder message is ``{}``.".format(str(number), remindmsg), color=0x03fc03)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder.")
			remindersdm.append(ctx.message.author.id)
			await ctx.send(embed=embed)
			await ctx.send(embed=embed2)
			
			await asyncio.sleep(float(number))
			
			if ctx.message.author.id in remindersdm:
				embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
				#await ctx.send("{},".format(ctx.message.author.mention))
				await ctx.message.author.send(embed=embed)
				try:
					await ctx.message.author.send(embed=embed)
				except discord.HTTPException as exception:
					await ctx.send("{}, I couldn't DM you with your reminder, so I'll post it here.".format(ctx.message.author.mention))
					await ctx.send(embed=embed)
				remindersdm.remove(ctx.message.author.id)
				return
			else:
				return
		if type == "m":
			if number > 10080:
				embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
			embed = discord.Embed(description="Alright, I'll remind you in **{}** minute(s). I'll notify you in DMs. Your reminder message is ``{}``.".format(str(number), remindmsg), color=0x03fc03)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder.")
			remindersdm.append(ctx.message.author.id)
			await ctx.send(embed=embed)
			await ctx.send(embed=embed2)
			
			await asyncio.sleep(float(number) * 60)
			
			if ctx.message.author.id in remindersdm:
				embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
				#await ctx.send("{},".format(ctx.message.author.mention))
				await ctx.message.author.send(embed=embed)
				try:
					await ctx.message.author.send(embed=embed)
				except discord.HTTPException as exception:
					await ctx.send("{}, I couldn't DM you with your reminder, so I'll post it here.".format(ctx.message.author.mention))
					await ctx.send(embed=embed)
				remindersdm.remove(ctx.message.author.id)
				return
			else:
				return
		if type == "h":
			if number > 168:
				embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
			embed = discord.Embed(description="Alright, I'll remind you in **{}** hour(s). I'll notify you in DMs. Your reminder message is ``{}``.".format(str(number), remindmsg), color=0x03fc03)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder.")
			remindersdm.append(ctx.message.author.id)
			await ctx.send(embed=embed)
			await ctx.send(embed=embed2)
			
			await asyncio.sleep(float(number) * 60 * 60)
			
			if ctx.message.author.id in remindersdm:
				embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
				#await ctx.send("{},".format(ctx.message.author.mention))
				await ctx.message.author.send(embed=embed)
				try:
					await ctx.message.author.send(embed=embed)
				except discord.HTTPException as exception:
					await ctx.send("{}, I couldn't DM you with your reminder, so I'll post it here.".format(ctx.message.author.mention))
					await ctx.send(embed=embed)
				remindersdm.remove(ctx.message.author.id)
				return
			else:
				return
		if type == "d":
			if number > 7:
				embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
			embed = discord.Embed(description="Alright, I'll remind you in **{}** day(s). I'll notify you in DMs. Your reminder message is ``{}``.".format(str(number), remindmsg), color=0x03fc03)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder.")
			remindersdm.append(ctx.message.author.id)
			await ctx.send(embed=embed)
			await ctx.send(embed=embed2)
			
			await asyncio.sleep(float(number) * 60 * 60 * 24)
			
			if ctx.message.author.id in remindersdm:
				embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
				#await ctx.send("{},".format(ctx.message.author.mention))
				await ctx.message.author.send(embed=embed)
				try:
					await ctx.message.author.send(embed=embed)
				except discord.HTTPException as exception:
					await ctx.send("{}, I couldn't DM you with your reminder, so I'll post it here.".format(ctx.message.author.mention))
					await ctx.send(embed=embed)
				remindersdm.remove(ctx.message.author.id)
				return
			else:
				return
				
@reminderdm.error
async def reminderdm_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="Fatal error. Are you sure you're giving me a member?", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="You're missing required arguments. Here's an example of how to use this command: \n``!reminder 3h going to appreciate this godly command``", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def reminderdmcancel(ctx):
	if ctx.message.author.id in remindersserver:
		embed = discord.Embed(description="DM reminder successfully canceled.", color=0xffffff)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		remindersdm.remove(ctx.message.author.id)
	else:
		embed = discord.Embed(description="You don't have a DM reminder to cancel. Set one by using ``!reminderdm``.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)

# - Verify command:
@bot.command()
@commands.has_any_role("Admin ･˚｡", "Co Owner˚ ༄", "Owner")
async def verify(ctx, user: discord.Member, gender: str=" "):
	verm = discord.utils.get(ctx.message.author.guild.roles, name="Verified Male")
	verf = discord.utils.get(ctx.message.author.guild.roles, name="Verified Female")
	verchan = discord.utils.get(ctx.message.author.guild.channels, name="ღverificationღ")

	failtover = discord.Embed(description="Try verifying this member again, but specify either **f** / **female** or **m** / **male**. \nExample: ``!verify @cooluser m``", color=0xFF3639)
	failtover.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	failtover.set_footer(text="Error raised on: {}".format(ctx.message.content))
	
	alrver = discord.Embed(description="This user is already verified.", color=0xFF3639)
	alrver.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	alrver.set_footer(text="Error raised on: {}".format(ctx.message.content))
	if(verm in user.roles or verf in user.roles):
		await ctx.message.delete()
		msg = await ctx.send(embed=alrver)
		await asyncio.sleep(float(10))
		await msg.delete()
		return
	if(gender == "m" or gender == "male"):
		#verr = " ".join(m)
		ver = discord.Embed(description="༚ ✧˳⁺ {} has received the **Verified Male** role. ⁺˳✧ ༚ ".format(user.mention), color=0xFF93F0)
		ver.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		ver.set_thumbnail(url=user.avatar_url)
		await user.add_roles(verm)
		await ctx.message.delete()
		await ctx.send(embed=ver)
		if ctx.message.channel != verchan:
			await verchan.send(embed=ver)
		return
	elif(gender == "f" or gender == "female"):
		#verr = " ".join(f)
		ver = discord.Embed(description="༚ ✧˳⁺ {} has rece9ved the **Verified Female** role. ⁺˳✧ ༚ ".format(user.mention), color=0xFF93F0)
		ver.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		ver.set_thumbnail(url=user.avatar_url)
		await user.add_roles(verf)
		await ctx.message.delete()
		await ctx.send(embed=ver)
		if ctx.message.channel != verchan:
			await verchan.send(embed=ver)
		return
	else:
		await ctx.message.delete()
		fail = await ctx.send(embed=failtover)
		await asyncio.sleep(float(10))
		await fail.delete()
		return
	
@verify.error
async def verify_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Are you sure this ID is correct?", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		msg = await ctx.send(embed=embed)
		await ctx.message.delete()
		await asyncio.sleep(float(10))
		await msg.delete()
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="Try again, but give me a user to verify.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		msg =await ctx.send(embed=embed)
		await ctx.message.delete()
		await asyncio.sleep(float(10))
		await msg.delete()
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		msg = await ctx.send(embed=embed)
		await ctx.message.delete()
		await asyncio.sleep(float(10))
		await msg.delete()
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
@commands.has_any_role("Head Admin ✧˚*:･", "Co Owner ‧₊˚ ༄", "Bot Coder", "$ dy")
async def v(ctx, user: discord.Member, gender: str=" "):
	verm = discord.utils.get(ctx.message.author.guild.roles, name="Verified Male")
	verf = discord.utils.get(ctx.message.author.guild.roles, name="Verified Female")
	verchan = discord.utils.get(ctx.message.author.guild.channels, name="ღverificationღ")

	failtover = discord.Embed(description="Try verifying this member again, but specify either **f** / **female** or **m** / **male**. \nExample: ``!verify @cooluser m``", color=0xFF3639)
	failtover.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	failtover.set_footer(text="Error raised on: {}".format(ctx.message.content))
	
	alrver = discord.Embed(description="This user is already verified.", color=0xFF3639)
	alrver.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	alrver.set_footer(text="Error raised on: {}".format(ctx.message.content))
	if(verm in user.roles or verf in user.roles):
		await ctx.message.delete()
		msg = await ctx.send(embed=alrver)
		await asyncio.sleep(float(10))
		await msg.delete()
		return
	if(gender == "m" or gender == "male"):
		#verr = " ".join(m)
		ver = discord.Embed(description="༚ ✧˳⁺ {} has received the **Verified Male** role. ⁺˳✧ ༚ ".format(user.mention), color=0xFF93F0)
		ver.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		ver.set_thumbnail(url=user.avatar_url)
		await user.add_roles(verm)
		await ctx.message.delete()
		await ctx.send(embed=ver)
		if ctx.message.channel != verchan:
			await verchan.send(embed=ver)
		return
	elif(gender == "f" or gender == "female"):
		#verr = " ".join(f)
		ver = discord.Embed(description="༚ ✧˳⁺ {} has received the **Verified Female** role. ⁺˳✧ ༚ ".format(user.mention), color=0xFF93F0)
		ver.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		ver.set_thumbnail(url=user.avatar_url)
		await user.add_roles(verf)
		await ctx.message.delete()
		await ctx.send(embed=ver)
		if ctx.message.channel != verchan:
			await verchan.send(embed=ver)
		return
	else:
		await ctx.message.delete()
		fail = await ctx.send(embed=failtover)
		await asyncio.sleep(float(10))
		await fail.delete()
		return
	
@v.error
async def v_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Are you sure this ID is correct?", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		msg = await ctx.send(embed=embed)
		await ctx.message.delete()
		await asyncio.sleep(float(10))
		await msg.delete()
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="Try again, but give me a user to verify.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		msg =await ctx.send(embed=embed)
		await ctx.message.delete()
		await asyncio.sleep(float(10))
		await msg.delete()
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		msg = await ctx.send(embed=embed)
		await ctx.message.delete()
		await asyncio.sleep(float(10))
		await msg.delete()
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

# - Info commands:

@bot.command()
@commands.has_any_role("Admin ･˚｡", "Admin ･˚｡", "Owner", "Co Owner")
async def membercount(ctx):
	time = datetime.datetime.now()
	corfor = time.strftime("%d %b, %Y at %H:%M")
	
	online = 0
	for member in ctx.message.author.guild.members:
		if member.status != discord.Status.offline:
			online += 1
	bots = 0
	for member in ctx.message.author.guild.members:
		if member.bot == True:
			bots += 1
	humans = 0
	for member in ctx.message.author.guild.members:
		if member.bot == False:
			humans += 1
	
	embed = discord.Embed(color=0x000000)
	embed.add_field(name="Members", value="{}".format(ctx.message.author.guild.member_count), inline=True)
	embed.add_field(name="Online", value="{}".format(online), inline=True)
	embed.add_field(name="Humans", value="{}".format(humans), inline=True)
	embed.add_field(name="Bots", value="{}".format(bots), inline=True)
	embed.set_footer(text="ID: {} | {}".format(ctx.message.author.guild.id, corfor))
	embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)

	await ctx.send(embed=embed)

@membercount.error
async def membercount_error(ctx, error):
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)


@bot.command()
@commands.has_any_role("Admin ･˚｡", "Admin ･˚｡", "Owner", "Co Owner")
async def serverinfo(ctx):
	time = ctx.message.author.guild.created_at 
	
	corfor = time.strftime("%d %b, %Y at %H:%M")
	
	channels = ctx.message.author.guild.text_channels
	voicechans = ctx.message.author.guild.voice_channels
	categories = ctx.message.author.guild.categories
	roles = ctx.message.author.guild.roles
	online = 0
	for member in ctx.message.author.guild.members:
		if member.status != discord.Status.offline:
			online += 1
	bots = 0
	for member in ctx.message.author.guild.members:
		if member.bot == True:
			bots += 1
	humans = 0
	for member in ctx.message.author.guild.members:
		if member.bot == False:
			humans += 1
	#fa = " "
	if ctx.message.author.guild.mfa_level == 0:
		fa = "No"
	if ctx.message.author.guild.mfa_level == 1:
		fa = "Yes"
	#ver = " "

	embed = discord.Embed(title="Info of {}".format(ctx.message.author.guild.name), description="Owned by {}".format(ctx.message.author.guild.owner), color=0x000000)
	embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
	embed.set_footer(text="ID: {} | Created at: {}".format(ctx.message.author.guild.id, corfor))
	embed.add_field(name="Server region", value="{}".format(ctx.message.author.guild.region), inline=True)
	embed.add_field(name="Channels count", value="{}".format(len(channels)), inline=True)
	embed.add_field(name="Voice channels count", value="{}".format(len(voicechans)), inline=True)
	embed.add_field(name="Categories count", value="{}".format(len(categories)), inline=True)
	embed.add_field(name="Roles count", value="{}".format(len(roles)), inline=True)
	embed.add_field(name="Members", value="{}".format(ctx.message.author.guild.member_count), inline=True)
	embed.add_field(name="Online", value="{}".format(online), inline=True)
	embed.add_field(name="Humans", value="{}".format(humans), inline=True)
	embed.add_field(name="Bots", value="{}".format(bots), inline=True)
	#embed2 = discord.Embed(color=0x000000)
	embed.add_field(name="Requires 2FA", value="{}".format(fa), inline=True)
	embed.add_field(name="Boosters", value="{}".format(ctx.message.author.guild.premium_subscription_count), inline=True)
	embed.add_field(name="Boost level", value="{}".format(ctx.message.author.guild.premium_tier), inline=True)
	if str(ctx.message.author.guild.verification_level) == "none":
		ver = "None"
		embed.add_field(name="Verification level", value="{}".format(ver))
		#print(ver)
	elif str(ctx.message.author.guild.verification_level) == "low":
		ver = "Must have a verified email"
		embed.add_field(name="Verification level", value="{}".format(ver))
	elif str(ctx.message.author.guild.verification_level) == "medium":
		ver = "Must have a verified email and be registered for 5 mins"
		embed.add_field(name="Verification level", value="{}".format(ver))
	elif str(ctx.message.author.guild.verification_level) == "high":
		ver = "Must have a verified email, be registered for 5 minutes and be a member for 10 mins"
		embed.add_field(name="Verification level", value="{}".format(ver))
	elif str(ctx.message.author.guild.verification_level) == "extreme":
		ver = "Must have a verified phone number"
		embed.add_field(name="Verification level", value="{}".format(ver))
	
	await ctx.send(embed=embed)
	#await ctx.send(embed=embed2)

@serverinfo.error
async def serverinfo_error(ctx, error):
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def bots(ctx):
	if ctx.message.author.id == 495680416422821888 or ctx.message.author.id == 393839495859929089:
		bots = []
		for member in ctx.message.author.guild.members:
			if member.bot:
				bots.append(member.mention)
		embed = discord.Embed(title="All bots in this server:", description="\n".join(bots), color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_thumbnail(url=bot.user.avatar_url)
		try:
			await ctx.send(embed=embed)
		except discord.HTTPException as exception:
			embed = discord.Embed(description="Too many bots, can't send the message.", color=FF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
	else:
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		
@bot.command()
@commands.has_any_role("Admin ･˚｡", "Co Owner", "Owner")
async def members(ctx, *, rolee: str):
	role = await parse_roles(ctx, rolee)
	members = []
	for member in ctx.message.author.guild.members:
		if role in member.roles:
			members.append(member.mention)
	embed = discord.Embed(title="All members that have the {} role:".format(str(role)), description="\n".join(members), color=0x000000)
	embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	embed.set_thumbnail(url=bot.user.avatar_url)
	try:
                await ctx.send(embed=embed)
	except discord.HTTPException as exception:
                embed = discord.Embed(description="Too many members, can't send the message.", color=0xFF3639)
                embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
                await ctx.send(embed=embed)
		
@members.error
async def members_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this role.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    # await ctx.send("{} look now, do i look like a magician? just mention a user and i'll ban them \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="You didn't give me a role to get the members of.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    # await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to ban? \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
    elif isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

# - Fun commands:
@bot.command()
async def avatar(ctx, user: discord.Member):
	embed = discord.Embed(title="Avatar of {}".format(user), color=0x000000)
	embed.set_image(url=user.avatar_url)
	await ctx.send(embed=embed)
	
@avatar.error
async def avatar_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(title="Member not found, ping a user to get their avatar.", color=0xFF3639)
		#embed.set_image(url=bot.user.avatar_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Avatar of {}".format(ctx.message.author), color=0x000000)
		embed.set_image(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def av(ctx, user: discord.Member):
	embed = discord.Embed(title="Avatar of {}".format(user), color=0x000000)
	embed.set_image(url=user.avatar_url)
	await ctx.send(embed=embed)
	
@av.error
async def av_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(title="Member not found, ping a user to get their avatar.", color=0xFF3639)
		#embed.set_image(url=ctx.message.author.guild.icon_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(title="Avatar of {}".format(ctx.message.author), color=0x000000)
		embed.set_image(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
async def avatarid(ctx, id: int):
	try:
		user = await bot.fetch_user(id)
	except discord.HTTPException:
		embed = discord.Embed(description="I dunno man, it doesn't look like there's a member like this.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
	
	embed = discord.Embed(title="Avatar of {}".format(user), color=0x000000)
	embed.set_image(url=user.avatar_url)
	await ctx.send(embed=embed)
		
@avatarid.error    
async def avatarid_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Are you sure this ID is correct?", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="I couldn't get the avatar of.. no one? Try giving me an ID so I can get an avatar..", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def avid(ctx, id: int):
	try:
		user = await bot.fetch_user(id)
	except discord.HTTPException:
		embed = discord.Embed(description="I dunno man, it doesn't look like there's a member like this.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
	
	embed = discord.Embed(title="Avatar of {}".format(user), color=0x000000)
	embed.set_image(url=user.avatar_url)
	await ctx.send(embed=embed)
		
@avid.error    
async def avid_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Are you sure this ID is correct?", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="I couldn't get the avatar of.. no one? Try giving me an ID so I can get an avatar..", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

# - Admin commands: 

@bot.command()
@commands.has_any_role("Owner")
async def masskick(ctx, *, users: str):
	desc = "Mass kick started. May take a while. \n\n" 
	embed = discord.Embed(description=desc, color=0x000000)
	embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	msg = await ctx.send(embed=embed)
	mentions = ctx.message.mentions
	for user in mentions:
		#desc = desc + "\n{}".format(user)
		try:
			await user.kick()
		except:
			#desc = desc + "\n :x: | {}".format(user)
			await ctx.send(f"Couldn't kick {user.mention} because of missing permissions.")
		#await msg.edit(embed=embed)
		
@masskick.error
async def masskick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="No @mentioned users were found with the information you gave.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="No @mentioned users were found with the information you gave.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
@commands.has_any_role("Owner")
async def massmute(ctx, *, users: str):
	desc = "Mass mute started. May take a while. \n\n" 
	role = discord.utils.get(ctx.message.author.guild.roles, name="Muted")
	embed = discord.Embed(description=desc, color=0x000000)
	embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	msg = await ctx.send(embed=embed)
	mentions = ctx.message.mentions
	for user in mentions:
		#desc = desc + "\n{}".format(user)
		try:
			await user.add_roles(role)
		except:
			#desc = desc + "\n :x: | {}".format(user)
			await ctx.send(f"Couldn't kick {user.mention} because of missing permissions.")
		#await msg.edit(embed=embed)
		
@massmute.error
async def massmute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="No @mentioned users were found with the information you gave.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="No @mentioned users were found with the information you gave.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Owner", "Admin ･˚｡", "Co Owner")
async def lockdown(ctx):
	enightclubrole = discord.utils.get(ctx.message.guild.roles, name="@everyone")
	check = ctx.message.channel.overwrites_for(enightclubrole)
	if check.send_messages == False:
		await ctx.send(":warning: **defying ღ thots** | **Lockdown** mode turned __off__ for **this channel** by {}.".format(ctx.message.author.mention))
		await ctx.message.channel.set_permissions(enightclubrole, send_messages=True)
	elif check.send_messages == True:
		await ctx.send(":warning: **defying ღ thots** | **Lockdown** mode turned __on__ for **this channel** by {}.".format(ctx.message.author.mention))
		await ctx.message.channel.set_permissions(enightclubrole, send_messages=False)
	else:
		await ctx.send(":warning: **defying ღ thots** | **Lockdown** mode turned __on__ for **this channel** by {}.".format(ctx.message.author.mention))
		await ctx.message.channel.set_permissions(enightclubrole, send_messages=False)

@lockdown.error
async def lockdown_error(ctx, error):
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.".format(ctx.message.author.mention), color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

@bot.command()
@commands.has_any_role("Admin ･˚｡", "Co Owner", "Owner")
async def ban(ctx, user: discord.Member, *, reason: str):
	if len(reason) == 0:
		embed = discord.Embed(title="Successfully banned {}.".format(user), description="**{}** was __banned__ from **[defying ღ thots](https://discord.gg/GJ5UDth)**. \nThe reason of their ban is **none, not provided**. \n Banned for permanent.".format(user.mention), color=0x000000)
		embed.set_thumbnail(url=user.avatar_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		#await ctx.send("**{}** was __banned__ from **defying ღ thots**.\n>> Banned by: **{}**\n>> Reason: **i guess the dummy that used the command forgot to enter a reason, so i'd say they got clapped justcuz**".format(user.mention, ctx.message.author.mention))
		try:
			embed = discord.Embed(title="You were banned from defying ღ thots.", description="You were banned by **{}**. \nThe reason for your ban is **none, not provided**. \nThis ban is permanent. \n\n [ - The defying ღ thots staff team.](https://discord.gg/GJ5UDth)".format(ctx.message.author), color=0x000000)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			await user.send(embed=embed)
			#await user.send("You've been banned from **defying ღ thots**. You were banned by **{}**, and you were banned for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
		except:
			embed = discord.Embed(description="I tried to DM the user, but I'm not allowed to because we don't share any guilds.", color=0xebf533)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			#await ctx.send("I failed to DM {}, so I didn't inform them for their ban. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
		logch = discord.utils.get(ctx.message.author.guild.channels, name="logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Used command ``!ban`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
		log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=user.avatar_url)
		await logch.send(embed=log)	
	else:
		embed = discord.Embed(title="Successfully banned {}.".format(user), description="**{}** was __banned__ from **[defying ღ thots](https://discord.gg/GJ5UDth)**. \nThe reason of their ban is **{}**. \n Banned for permanent.".format(user.mention, reason), color=0x000000)
		embed.set_thumbnail(url=user.avatar_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		#await ctx.send("**{}** was __banned__ from **defying ღ thots**.\n>> Banned by: **{}**\n>> Reason: **{}**".format(user.mention, ctx.message.author.mention, reason))
		try:
			embed = discord.Embed(title="You were banned from defying ღ thots.", description="You were banned by **{}**. \nThe reason for your ban is **{}**. \nThis ban is permanent. \n\n [ - The defying ღ thots staff team.](https://discord.gg/GJ5UDth)".format(ctx.message.author, reason), color=0x000000)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			await user.send(embed=embed)
			#await user.send("You've been banned from **defying ღ thots**. You were banned by **{}**, and you were banned for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
		except:
			embed = discord.Embed(description="I tried to DM the user, but I'm not allowed to because we don't share any guilds.", color=0xebf533)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			#await ctx.send("I failed to DM {}, so I didn't inform them for their ban. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
		logch = discord.utils.get(ctx.message.author.guild.channels, name="logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Used command ``!ban`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
		log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=user.avatar_url)
		await logch.send(embed=log)
	await user.ban()

@ban.error    
async def ban_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} look now, do i look like a magician? just mention a user and i'll ban them \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="Give me a user to ban. \n``TIP:`` If you want to ban a user that's not in the server, try using !banid.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to ban? \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Admin ･˚｡", "Co Owner", "Owner")
async def banid(ctx, id: int, *, reason: str):
	user = await bot.fetch_user(id)
	if user is None:
		embed = discord.Embed(description="User doesn't exist.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		#await ctx.send(f"{ctx.message.author.mention}, this user doesn't exist.")
		return
	#banEntry = await ctx.message.guild.fetch_ban(user)
	#if BanEntry is None:
	#if reason is None:
	#	await ctx.send("**{}** was __banned__ from **defying ღ thots**.\n>> Banned by: **{}**\n>> Reason: **i guess the dummy that used the command forgot to enter a reason, so i'd say they got clapped justcuz**".format(user.mention, ctx.message.author.mention))
	##	try:
	#		await user.send("You've been banned from **defying ღ thots**. You were banned by **{}**, and you were banned for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
	#	except:
	#		await ctx.send("I failed to DM {}, so I didn't inform them for their ban. \n Obvious reason: his command bans people that are not in the server, it would make sense to not have the perms to DM them.".format(user.mention))
	#else:
	#	await ctx.send("**{}** was __banned__ from **defying ღ thots**.\n>> Banned by: **{}**\n>> Reason: **{}**".format(user.mention, ctx.message.author.mention, reason))
	#	try:
	##		await user.send("You've been banned from **defying ღ thots**. You were banned by **{}**, and you were banned for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
	#	except:
	#		await ctx.send("I failed to DM {}, so I didn't inform them for their ban. \n Obvious reason: this command bans people that are not in the server, it would make sense to not have the perms to DM them..".format(user.mention))
	if len(reason) == 0:
		embed = discord.Embed(title="Successfully banned {}.".format(user), description="**{}** was __banned__ from **[defying ღ thots](https://discord.gg/GJ5UDth)**. \nThe reason of their ban is **none, not provided**. \n Banned for permanent.".format(user.mention), color=0x000000)
		embed.set_thumbnail(url=user.avatar_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		#await ctx.send("**{}** was __banned__ from **defying ღ thots**.\n>> Banned by: **{}**\n>> Reason: **i guess the dummy that used the command forgot to enter a reason, so i'd say they got clapped justcuz**".format(user.mention, ctx.message.author.mention))
		try:
			embed = discord.Embed(title="You were banned from defying ღ thots.", description="You were banned by **{}**. \nThe reason for your ban is **none, not provided**. \nThis ban is permanent. \n\n [ - The defying ღ thots staff team.](https://discord.gg/GJ5UDth)".format(ctx.message.author), color=0x000000)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			await user.send(embed=embed)
			#await user.send("You've been banned from **defying ღ thots**. You were banned by **{}**, and you were banned for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
		except:
			embed = discord.Embed(description="I tried to DM the user, but I'm not allowed to because we don't share any guilds.", color=ebf533)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			#await ctx.send("I failed to DM {}, so I didn't inform them for their ban. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
		logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Used command ``!banid`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
		log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=user.avatar_url)
		await logch.send(embed=log)
	else:
		embed = discord.Embed(title="Successfully banned {}.".format(user), description="**{}** was __banned__ from **[defying ღ thots](https://discord.gg/GJ5UDth)**. \nThe reason of their ban is **{}**. \n Banned for permanent.".format(user.mention, reason), color=0x000000)
		embed.set_thumbnail(url=user.avatar_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		#await ctx.send("**{}** was __banned__ from **defying ღ thots**.\n>> Banned by: **{}**\n>> Reason: **{}**".format(user.mention, ctx.message.author.mention, reason))
		try:
			embed = discord.Embed(title="You were banned from defying ღ thots.", description="You were banned by **{}**. \nThe reason for your ban is **{}**. \nThis ban is permanent. \n\n [ - The defying ღ thots staff team.](https://discord.gg/GJ5UDth)".format(ctx.message.author, reason), color=0x000000)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			await user.send(embed=embed)
			#await user.send("You've been banned from **defying ღ thots**. You were banned by **{}**, and you were banned for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
		except:
			embed = discord.Embed(description="I tried to DM the user, but I'm not allowed to because we don't share any guilds.", color=0xebf533)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			#await ctx.send("I failed to DM {}, so I didn't inform them for their ban. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
		logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Used command ``!banid`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
		log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=user.avatar_url)
		await logch.send(embed=log)

	await ctx.message.guild.ban(discord.Object(id=id))
	#else:
		#ctx.send(f"{ctx.message.author.mention}, seems like this user is already banned.")

@banid.error    
async def banid_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Is the ID correct?", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} look now, do i look like a magician? just mention a user and i'll ban them \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="Give me ID of an user to ban.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to ban? \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Co Owner", "Owner")
async def massban(ctx, *, users: str):
	desc = "Mass ban started. May take a while. \n\n" 
	embed = discord.Embed(description=desc, color=0x000000)
	embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	msg = await ctx.send(embed=embed)
	mentions = ctx.message.mentions
	for user in mentions:
		#desc = desc + "\n{}".format(user)
		try:
			await user.ban()
		except:
			#desc = desc + "\n :x: | {}".format(user)
			await ctx.send(f"Couldn't ban {user.mention} because of missing permissions.")
		#await msg.edit(embed=embed)
		
@massban.error
async def massban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="No @mentioned users were found with the information you gave.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="No @mentioned users were found with the information you gave.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Admin ･˚｡", "Co Owner", "Owner")
async def unban(ctx, id: int, *, reason: str = ""):
	#print("I got the user!")
	#print("ID: " + id)
	user = await bot.fetch_user(id)
	if user is None:
		embed = discord.Embed(description="User doesn't exist.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		#await ctx.send(f"{ctx.message.author.mention}, this user doesn't exist.")
		return
	#print("I fetched this user!")
	banEntry = await ctx.message.guild.fetch_ban(user)
	if banEntry is None:
		#print("This user is not banned!")
		#await ctx.send(f"{ctx.message.author.mention}, are you sure this user is banned?")
		embed = discord.Embed(description="This user is not banned.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
	else:
		if banEntry.reason is None:
			#print("Going without a reason!")
			#await ctx.send("**{}** was __unbanned__. \n"
			#				">> Unbanned by: **{}**\n"
			#				">> Reason: **who even puts reasons on unban lol**"
			#				.format(banEntry.user, ctx.message.author.mention))
			embed = discord.Embed(title="Successfully unbanned {}".format(user), description="**{}** was unbanned from [**defying ღ thots**](https://discord.gg/GJ5UDth). \nThe reason of the unban is **reasons on unban? seems gay to me**".format(banEntry.user, ctx.message.author.mention), color=0x000000)
			embed.set_thumbnail(url=user.avatar_url)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
			timestamp=datetime.datetime.now()
			corfor = timestamp.strftime("%d %b, %Y at %H:%M")
			log = discord.Embed(description="Used command ``!unban`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
			log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			log.set_footer(text="{}".format(corfor))
			log.set_thumbnail(url=user.avatar_url)
			await logch.send(embed=log)
		else:
			#print("Going with a reason!")
			#await ctx.send("**{}** was __unbanned__. \n"
			#				">> Unbanned by: **{}**\n"
			#				">> Reason: **{}**"
			#				.format(banEntry.user, ctx.message.author.mention, reason))
			embed = discord.Embed(title="Successfully unbanned {}".format(user), description="**{}** was unbanned from [**defying ღ thots**](https://discord.gg/GJ5UDth). \nThe reason of the unban is **{}**".format(banEntry.user, ctx.message.author.mention, reason), color=0x000000)
			embed.set_thumbnail(url=user.avatar_url)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
			timestamp=datetime.datetime.now()
			corfor = timestamp.strftime("%d %b, %Y at %H:%M")
			log = discord.Embed(description="Used command ``!unban`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
			log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			log.set_footer(text="{}".format(corfor))
			log.set_thumbnail(url=user.avatar_url)
			await logch.send(embed=log)
		#print("I unbanned the user!")
		await ctx.message.guild.unban(banEntry.user, reason="Ban reason goes here")
		
@unban.error    
async def unban_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Is the ID correct?", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
        	#await ctx.send("{} look now, do i look like a magician? just give me the id of an user and i'll unban them \n example: ``!unban id how did this happen to begin with``".format(ctx.message.author.mention))
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="I couldn't  unban.. no one? Try giving me the ID of an user.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
        	#await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to unban? \n example: ``!unban id how did this happen to begin with``".format(ctx.message.author.mention))
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} r u dumb or hella dumb? this command is for admins and mods only, nice try tho, i must give u that.".format(ctx.message.author.mention))
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Admin ･˚｡", "Co Owner", "Owner", "Admin ･˚｡")
async def kick(ctx, user: discord.Member, *, reason: str):
	if len(reason) == 0:
		embed = discord.Embed(title="Successfully kicked {}.".format(user), description="**{}** was __kicked__ from **[defying ღ thots](https://discord.gg/GJ5UDth)**. \nThe reason of their kick is **none, not provided**.".format(user.mention), color=0x000000)
		embed.set_thumbnail(url=user.avatar_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		#await ctx.send("**{}** was __kicked__ from **defying ღ thots**.\n>> Kicked by: **{}**\n>> Reason: **i guess the dummy that used the command forgot to enter a reason, so i'd say they got slapped justcuz**".format(user.mention, ctx.message.author.mention))
		try:
			embed = discord.Embed(title="You were kicked from [**defying ღ thots**](https://discord.gg/GJ5UDth).", description="You were kicked by **{}**. \nThe reason for your kick is **none, not provided**. \n\n [ - The defying ღ thots staff team.](https://discord.gg/GJ5UDth)".format(ctx.message.author), color=0x000000)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			await user.send(embed=embed)
			#await user.send("You've been kicked from **defying ღ thots**. You were kicked by **{}**, and you were kicked for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
		except:
			embed = discord.Embed(description="I tried to DM the user, but I'm not allowed to because their DMs weren't enabled.", color=ebf533)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			#await ctx.send("I failed to DM {}, so I didn't inform them for their kick. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
		logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Used command ``!kick`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
		log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=user.avatar_url)
		await logch.send(embed=log)
	else:
		embed = discord.Embed(title="Successfully kicked {}.".format(user), description="**{}** was __kicked__ from **[defying ღ thots](https://discord.gg/GJ5UDth)**. \nThe reason of their kick is **{}**.".format(user.mention, reason), color=0x000000)
		embed.set_thumbnail(url=user.avatar_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		#await ctx.send("**{}** was __kicked__ from **defying ღ thots**.\n>> Kicked by: **{}**\n>> Reason: **{}**".format(user.mention, ctx.message.author.mention, reason))
		try:
			embed = discord.Embed(title="You were kicked from [**defying ღ thots**](https://discord.gg/GJ5UDth).", description="You were kicked by **{}**. \nThe reason for your kick is **none, not provided**. \n\n [ - The defying ღ thots staff team.](https://discord.gg/GJ5UDth)".format(ctx.message.author), color=0x000000)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			await user.send(embed=embed)
			#await user.send("You've been kicked from **defying ღ thots**. You were kicked by **{}**, and you were kicked for **none (no reason was found)**.\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
		except:
			embed = discord.Embed(description="I tried to DM the user, but I'm not allowed to because their DMs weren't enabled.", color=ebf533)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			#await ctx.send("I failed to DM {}, so I didn't inform them for their kick. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
		logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Used command ``!kick`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
		log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=user.avatar_url)
		await logch.send(embed=log)
	await user.kick()
 
@kick.error    
async def kick_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Try giving me a correct user.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} look now, do i look like a magician? just mention a user and i'll kick them \n example: ``!kick @dy ez noob``".format(ctx.message.author.mention))
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="I couldn't kick.. no one? Try giving me a correct user.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to kick? \n example: ``!kick @dy ez noob``".format(ctx.message.author.mention))
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} r u dumb or hella dumb? this command is for admins and mods only, nice try tho, i must give u that.".format(ctx.message.author.mention))
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Chat Moderator", "Co Owner", "Owner", "Admin ･˚｡")
async def mute(ctx, user: discord.Member, *, reason: str):
	mutedrole = discord.utils.get(ctx.message.author.guild.roles, name="Muted")
	if mutedrole in user.roles:
		embed = discord.Embed(description="This user is already muted.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
	else:
		if len(reason) == 0:
			embed = discord.Embed(title="Successfully muted {}.".format(user), description="**{}** was __muted__. \nThe reason of their mute is **none, not provided**.".format(user.mention), color=0x000000)
			embed.set_thumbnail(url=user.avatar_url)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			#await ctx.send("**{}** was __muted__.\n>> Muted by: **{}**\n>> Reason: **i guess the dummy that used the command forgot to enter a reason, so i'd say they got slapped justcuz** \n**This mute won't be removed automatically. Someone has to manually remove it.**".format(user.mention, ctx.message.author.mention))
			try:
				embed = discord.Embed(title="You were muted in [**defying ღ thots**](https://discord.gg/GJ5UDth).", description="You were muted by **{}**. \nThe reason for your mute is **none, not provided**. \n\n [ - The defying ღ thots staff team.](https://discord.gg/GJ5UDth)".format(ctx.message.author), color=0x000000)
				embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
				await user.send(embed=embed)
				#await user.send("You've been muted in **defying ღ thots**. You were muted by **{}**, and you were muted for **none (no reason was found)**.\n**This mute won't be removed automatically. Someone has to manually remove it.**\nIf you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author))
			except:
				embed = discord.Embed(description="I tried to DM the user, but I'm not allowed to because their DMs weren't enabled.", color=ebf533)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				await ctx.send(embed=embed)
				#await ctx.send("I failed to DM {}, so I didn't inform them for their mute. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
			logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
			timestamp=datetime.datetime.now()
			corfor = timestamp.strftime("%d %b, %Y at %H:%M")
			log = discord.Embed(description="Used command ``!mute`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
			log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			log.set_footer(text="{}".format(corfor))
			log.set_thumbnail(url=user.avatar_url)
			await logch.send(embed=log)
		else:
			embed = discord.Embed(title="Successfully muted {}.".format(user), description="**{}** was __muted__. \nThe reason of their mute is **{}**.".format(user.mention, reason), color=0x000000)
			embed.set_thumbnail(url=user.avatar_url)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			#await ctx.send("**{}** was __muted__.\n>> Muted by: **{}**\n>> Reason: **{}**\n**This mute won't be removed automatically. Someone has to manually remove it.**".format(user.mention, ctx.message.author.mention, reason))
			try:
				embed = discord.Embed(title="You were muted in [**defying ღ thots**](https://discord.gg/GJ5UDth).", description="You were muted by **{}**. \nThe reason for your mute is **{}**. \n\n [ - The defying ღ thots staff team.](https://discord.gg/GJ5UDth)".format(ctx.message.author, reason), color=0x000000)
				embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
				await user.send(embed=embed)
				#await user.send("You've been muted in **defying ღ thots**. You were muted by **{}**, and you were muted for **{}**. \n**This mute won't be removed automatically. Someone has to manually remove it.**\n If you feel like this punishment isn't correct, feel free to contact dy#0777 or ¢คຖt Şนpprē$͓̽$͓̽ | PM#7802, and they'll look into it.".format(ctx.message.author, reason))
			except:
				embed = discord.Embed(description="I tried to DM the user, but I'm not allowed to because their DMs weren't enabled.", color=ebf533)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				await ctx.send(embed=embed)
				#await ctx.send("I failed to DM {}, so I didn't inform them for their mute. \n Obvious reason: the user had their DMs disabled.".format(user.mention))
			logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
			timestamp=datetime.datetime.now()
			corfor = timestamp.strftime("%d %b, %Y at %H:%M")
			log = discord.Embed(description="Used command ``!mute`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
			log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			log.set_footer(text="{}".format(corfor))
			log.set_thumbnail(url=user.avatar_url)
			await logch.send(embed=log)
		await user.add_roles(mutedrole)
 
@mute.error    
async def mute_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Try giving me a correct user.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	#await ctx.send("{} look now, do i look like a magician? just mention a user and i'll kick them \n example: ``!kick @dy ez noob``".format(ctx.message.author.mention))
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="I couldn't mute.. no one? Try giving me a correct user.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	#await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to kick? \n example: ``!kick @dy ez noob``".format(ctx.message.author.mention))
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	#await ctx.send("{} r u dumb or hella dumb? this command is for admins and mods only, nice try tho, i must give u that.".format(ctx.message.author.mention))
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Chat Moderator", "Co Owner", "Owner", "Admin ･˚｡")
async def unmute(ctx, user: discord.Member, *, reason: str = ""):
	mutedrole = discord.utils.get(ctx.message.author.guild.roles, name="Muted")
	if mutedrole in user.roles:
		if len(reason) == 0:
			embed = discord.Embed(title="Successfully unmuted {}.".format(user), description="**{}** was __unmuted__. \nThe reason of their unmute is **none, not provided**.".format(user.mention), color=0x000000)
			embed.set_thumbnail(url=user.avatar_url)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
			timestamp=datetime.datetime.now()
			corfor = timestamp.strftime("%d %b, %Y at %H:%M")
			log = discord.Embed(description="Used command ``!unmute`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
			log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			log.set_footer(text="{}".format(corfor))
			log.set_thumbnail(url=user.avatar_url)
			await logch.send(embed=log)
		#await ctx.send("**{}** was __unmuted__. \n>> Unmuted by: **{}**\n>> Reason: **who even puts reasons on unmute lol**".format(user.mention, ctx.message.author.mention))
		else:
			embed = discord.Embed(title="Successfully unmuted {}.".format(user), description="**{}** was __unmuted__. \nThe reason of their unmute is **{}**.".format(user.mention, reason), color=0x000000)
			embed.set_thumbnail(url=user.avatar_url)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
			timestamp=datetime.datetime.now()
			corfor = timestamp.strftime("%d %b, %Y at %H:%M")
			log = discord.Embed(description="Used command ``!unmute`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
			log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			log.set_footer(text="{}".format(corfor))
			log.set_thumbnail(url=user.avatar_url)
			await logch.send(embed=log)
		#await ctx.send("**{}** was __unmuted__. \n>> Unmuted by: **{}**\n>> Reason: **{}**".format(user.mention, ctx.message.author.mention, reason))
		await user.remove_roles(mutedrole)
	else:
		embed = discord.Embed(description="This user is not muted.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return

@unmute.error    
async def unmute_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user. Try giving me a correct user.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
 		#await ctx.send("{} look now, do i look like a magician? just mention a user and i'll unmute them \n example: ``!unmute @dy lol begged for unmute``".format(ctx.message.author.mention))
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="I couldn't unmute.. no one? Try giving me a correct user.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to unmute? \n example: ``!unmute @dy lol begged for unmute``".format(ctx.message.author.mention))
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} r u dumb or hella dumb? this command is for admins and mods only, nice try tho, i must give u that.".format(ctx.message.author.mention))
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

# - Userinfo Command:
def sort_by_joined_at(member:discord.Member):
	return member.joined_at
	
@bot.command()
async def userinfo(ctx, user: discord.Member):
	time = user.joined_at
	
	corfor1 = time.strftime("%d %b, %Y at %H:%M")
	
	time2 = user.created_at
	
	corfor2 = time2.strftime("%d %b, %Y at %H:%M")
	
	memberslist = ctx.guild.members
	memberslist.sort(key=sort_by_joined_at)
	joinpos = memberslist.index(user)
	
	boosting = " "
	if user.premium_since == None:
		boosting = "Nope"
	else:
		time3 = user.premium_since
		corfor3 = time3.strftime("%d %b, %Y at %H:%M")
		boosting = "Yes"
		
	fro = " "
	if user.is_on_mobile():
		fro = "Mobile"
	else:
		fro = "PC"
	
	embed = discord.Embed(description="Nickname: {}".format(user.nick), color=0x000000)
	embed.set_author(name="Info of {}".format(user), icon_url=user.avatar_url)
	embed.set_footer(text="Requested by {}".format(ctx.message.author))
	embed.add_field(name="Joined on", value="{}".format(corfor1))
	embed.add_field(name="Join position", value="{}".format(str(joinpos + 1)))
	embed.add_field(name="Registered on", value="{}".format(corfor2))
	embed.add_field(name="Boosting this guild", value="{}".format(boosting))
	embed.add_field(name="Current status", value="{}".format(str(user.status)))
	embed.add_field(name="Mobile or PC", value="{}".format(fro))
	embed.set_thumbnail(url=user.avatar_url)
	await ctx.send(embed=embed)
	
@userinfo.error    
async def userinfo_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="Member not found, check the member you gave me and try again.", color=0xFF3639)
		#embed.set_image(url=ctx.message.author.guild.icon_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		time = ctx.message.author.joined_at
	
		corfor1 = time.strftime("%d %b, %Y at %H:%M")
	
		time2 = ctx.message.author.created_at
	
		corfor2 = time2.strftime("%d %b, %Y at %H:%M")
	
		memberslist = ctx.guild.members
		memberslist.sort(key=sort_by_joined_at)
		joinpos = memberslist.index(ctx.message.author)
	
		boosting = " "
		if ctx.message.author.premium_since == None:
			boosting = "Nope"
		else:
			time3 = ctx.message.author.premium_since
			corfor3 = time3.strftime("%d %b, %Y at %H:%M")
			boosting = "Yes"
		
		fro = " "
		if ctx.message.author.is_on_mobile():
			fro = "Mobile"
		else:
			fro = "PC"
	
		embed = discord.Embed(description="Nickname: {}".format(ctx.message.author.nick), color=0x000000)
		embed.set_author(name="Info of {}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Requested by {}".format(ctx.message.author))
		embed.add_field(name="Joined on", value="{}".format(corfor1))
		embed.add_field(name="Join position", value="{}".format(str(joinpos + 1)))
		embed.add_field(name="Registered on", value="{}".format(corfor2))
		embed.add_field(name="Boosting this guild", value="{}".format(boosting))
		embed.add_field(name="Current status", value="{}".format(str(ctx.message.author.status)))
		embed.add_field(name="Mobile or PC", value="{}".format(fro))
		embed.set_thumbnail(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def uf(ctx, user: discord.Member):
	time = user.joined_at
	
	corfor1 = time.strftime("%d %b, %Y at %H:%M")
	
	time2 = user.created_at
	
	corfor2 = time2.strftime("%d %b, %Y at %H:%M")
	
	memberslist = ctx.guild.members
	memberslist.sort(key=sort_by_joined_at)
	joinpos = memberslist.index(user)
	
	boosting = " "
	if user.premium_since == None:
		boosting = "Nope"
	else:
		time3 = user.premium_since
		corfor3 = time3.strftime("%d %b, %Y at %H:%M")
		boosting = "Yes"
		
	fro = " "
	if user.is_on_mobile():
		fro = "Mobile"
	else:
		fro = "PC"
	
	embed = discord.Embed(description="Nickname: {}".format(user.nick), color=0x000000)
	embed.set_author(name="Info of {}".format(user), icon_url=user.avatar_url)
	embed.set_footer(text="Requested by {}".format(ctx.message.author))
	embed.add_field(name="Joined on", value="{}".format(corfor1))
	embed.add_field(name="Join position", value="{}".format(str(joinpos + 1)))
	embed.add_field(name="Registered on", value="{}".format(corfor2))
	embed.add_field(name="Boosting this guild", value="{}".format(boosting))
	embed.add_field(name="Current status", value="{}".format(str(user.status)))
	embed.add_field(name="Mobile or PC", value="{}".format(fro))
	embed.set_thumbnail(url=user.avatar_url)
	await ctx.send(embed=embed)
	
@uf.error
async def uf_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="Member not found, check the member you gave me and try again.", color=0xFF3639)
		#embed.set_image(url=ctx.message.author.guild.icon_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		time = ctx.message.author.joined_at
	
		corfor1 = time.strftime("%d %b, %Y at %H:%M")
	
		time2 = ctx.message.author.created_at
	
		corfor2 = time2.strftime("%d %b, %Y at %H:%M")
	
		memberslist = ctx.guild.members
		memberslist.sort(key=sort_by_joined_at)
		joinpos = memberslist.index(ctx.message.author)
	
		boosting = " "
		if ctx.message.author.premium_since == None:
			boosting = "Nope"
		else:
			time3 = ctx.message.author.premium_since
			corfor3 = time3.strftime("%d %b, %Y at %H:%M")
			boosting = "Yes"
		
		fro = " "
		if ctx.message.author.is_on_mobile():
			fro = "Mobile"
		else:
			fro = "PC"
	
		embed = discord.Embed(description="Nickname: {}".format(ctx.message.author.nick), color=0x000000)
		embed.set_author(name="Info of {}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Requested by {}".format(ctx.message.author))
		embed.add_field(name="Joined on", value="{}".format(corfor1))
		embed.add_field(name="Join position", value="{}".format(str(joinpos + 1)))
		embed.add_field(name="Registered on", value="{}".format(corfor2))
		embed.add_field(name="Boosting this guild", value="{}".format(boosting))
		embed.add_field(name="Current status", value="{}".format(str(ctx.message.author.status)))
		embed.add_field(name="Mobile or PC", value="{}".format(fro))
		embed.set_thumbnail(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def whois(ctx, user: discord.Member):
	time = user.joined_at
	
	corfor1 = time.strftime("%d %b, %Y at %H:%M")
	
	time2 = user.created_at
	
	corfor2 = time2.strftime("%d %b, %Y at %H:%M")
	
	memberslist = ctx.guild.members
	memberslist.sort(key=sort_by_joined_at)
	joinpos = memberslist.index(user)
	
	boosting = " "
	if user.premium_since == None:
		boosting = "Nope"
	else:
		time3 = user.premium_since
		corfor3 = time3.strftime("%d %b, %Y at %H:%M")
		boosting = "Yes"
		
	fro = " "
	if user.is_on_mobile():
		fro = "Mobile"
	else:
		fro = "PC"
	
	embed = discord.Embed(description="Nickname: {}".format(user.nick), color=0x000000)
	embed.set_author(name="Info of {}".format(user), icon_url=user.avatar_url)
	embed.set_footer(text="Requested by {}".format(ctx.message.author))
	embed.add_field(name="Joined on", value="{}".format(corfor1))
	embed.add_field(name="Join position", value="{}".format(str(joinpos + 1)))
	embed.add_field(name="Registered on", value="{}".format(corfor2))
	embed.add_field(name="Boosting this guild", value="{}".format(boosting))
	embed.add_field(name="Current status", value="{}".format(str(user.status)))
	embed.add_field(name="Mobile or PC", value="{}".format(fro))
	embed.set_thumbnail(url=user.avatar_url)
	await ctx.send(embed=embed)
	
@whois.error
async def whois_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="Member not found, check the member you gave me and try again.", color=0xFF3639)
		#embed.set_image(url=ctx.message.author.guild.icon_url)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		time = ctx.message.author.joined_at
	
		corfor1 = time.strftime("%d %b, %Y at %H:%M")
	
		time2 = ctx.message.author.created_at
	
		corfor2 = time2.strftime("%d %b, %Y at %H:%M")
	
		memberslist = ctx.guild.members
		memberslist.sort(key=sort_by_joined_at)
		joinpos = memberslist.index(ctx.message.author)
	
		boosting = " "
		if ctx.message.author.premium_since == None:
			boosting = "Nope"
		else:
			time3 = ctx.message.author.premium_since
			corfor3 = time3.strftime("%d %b, %Y at %H:%M")
			boosting = "Yes"
		
		fro = " "
		if ctx.message.author.is_on_mobile():
			fro = "Mobile"
		else:
			fro = "PC"
	
		embed = discord.Embed(description="Nickname: {}".format(ctx.message.author.nick), color=0x000000)
		embed.set_author(name="Info of {}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Requested by {}".format(ctx.message.author))
		embed.add_field(name="Joined on", value="{}".format(corfor1))
		embed.add_field(name="Join position", value="{}".format(str(joinpos + 1)))
		embed.add_field(name="Registered on", value="{}".format(corfor2))
		embed.add_field(name="Boosting this guild", value="{}".format(boosting))
		embed.add_field(name="Current status", value="{}".format(str(ctx.message.author.status)))
		embed.add_field(name="Mobile or PC", value="{}".format(fro))
		embed.set_thumbnail(url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)
		
@bot.command()
async def status(ctx, a, b, *, status: str=" "):
	if(ctx.message.author.id == 514392208254959618 or ctx.message.author.id == 393839495859929089):
		if len(a) != 0:
			#embed = discord.Embed(description="Status changed. \n".format(status), color=0x000000)
			if ((a == "o" or a =="online") and (b == "p" or b == "playing")):
				embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.playing))
			elif ((a == "o" or a == "online") and (b == "w" or b == "watching")):
				embed = discord.Embed(description="Status changed. \n**Online**\n**Watching {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.watching))
			elif ((a == "o" or a =="online") and (b == "l" or b == "listening")):
				embed = discord.Embed(description="Status changed. \n**Online**\n**Listening to {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.listening))
			elif ((a == "i" or a =="idle") and (b == "p" or b == "playing")):
				embed = discord.Embed(description="Status changed. \n**Idle**\n**Playing {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.playing))
			elif ((a == "i" or a == "idle") and (b == "w" or b == "watching")):
				embed = discord.Embed(description="Status changed. \n**Idle**\n**Watching {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.watching))
			elif ((a == "i" or a =="idle") and (b == "l" or b == "listening")):
				embed = discord.Embed(description="Status changed. \n**Idle**\n**Listening to {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.listening))
			elif ((a == "d" or a =="dnd") and (b == "p" or b == "playing")):
				embed = discord.Embed(description="Status changed. \n**Do Not Disturb**\n**Playing {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.playing))
			elif ((a == "d" or a == "dnd") and (b == "w" or b == "watching")):
				embed = discord.Embed(description="Status changed. \n**Do Not Disturb**\n**Watching {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.watching))
			elif ((a == "d" or a =="dnd") and (b == "l" or b == "listening")):
				embed = discord.Embed(description="Status changed. \n**Do Not Disturb**\n**Listening to {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.listening))
			elif (a == "o" or a =="online"):
				if len(a) == 1:
					statuss = ctx.message.content[9:]
				elif len(a) == 6:
					statuss = ctx.message.content[14:]
				embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(statuss), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(statuss), type=discord.ActivityType.playing))
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_msg**, I chose the default one: **Playing**.", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
			elif (a == "i" or a == "idle"):
				if len(a) == 1:
					statuss = ctx.message.content[9:]
				elif len(a) == 4:
					statuss = ctx.message.content[12:]
				embed = discord.Embed(description="Status changed. \n**Idle**\n**Playing {}**".format(statuss), color=0x000000)
				await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(name='{}'.format(statuss), type=discord.ActivityType.playing))
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_msg**, I chose the default one: **Playing**.", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
			elif (a == "d" or a =="dnd"):
				if len(a) == 1:
					statuss = ctx.message.content[9:]
				elif len(a) == 3:
					statuss = ctx.message.content[11:]
				embed = discord.Embed(description="Status changed. \n**Do Not Disturb**\n**Playing {}**".format(statuss), color=0x000000)
				await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name='{}'.format(statuss), type=discord.ActivityType.playing))
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_msg**, I chose the default one: **Playing**.", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
			elif (a == "playing" or a == "p"):
				if len(a) == 1:
					statuss = ctx.message.content[9:]
				elif len(a) == 7:
					statuss = ctx.message.content[15:]
				embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(statuss), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(statuss), type=discord.ActivityType.playing))
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_ttpe**, I chose the default one: **Online**.", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
			elif (a == "w" or a == "watching"):
				if len(a) == 1:
					statuss = ctx.message.content[9:]
				elif len(a) == 8:
					statuss = ctx.message.content[16:]
				embed = discord.Embed(description="Status changed. \n**Online**\n**Watching {}**".format(statuss), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(statuss), type=discord.ActivityType.watching))
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_type**, I chose the default one: **Online**.", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
			elif (a == "l" or a == "listening"):
				if len(a) == 1:
					statuss = ctx.message.content[9:]
				elif len(a) == 9:
					statuss = ctx.message.content[17:]
				embed = discord.Embed(description="Status changed. \n**Online**\n**Listening to {}**".format(statuss), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(statuss), type=discord.ActivityType.listening))
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_type**, I chose the default one: **Online**.", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
			else:
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_type** and/or **status_msg** combination, I chose the default ones: **Online** and **Playing**.", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
				embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.playing))

			
			
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
			await ctx.send(embed=embed)
			#await bot.change_presence(activity=discord.Game(name='{}'.format(status)))
		else:
			embed = discord.Embed(description="You didn't provide a status.", color=0xFF3639)
			embed.set_image(url=ctx.message.author.guild.icon_url)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
	else:
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		return
		
@status.error
async def status_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		if(ctx.message.author.id == 495680416422821888 or ctx.message.author.id == 393839495859929089):
			if len(ctx.message.content) > 8:
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_type** and/or **status_msg**, I think that the status is empty. I'll get the status by your message. (COULD **NOT BE WORKING PROPERLY**!)", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
				status = ctx.message.content[7:]
				embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.playing))
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
				await ctx.send(embed=embed)
			else:
				embed = discord.Embed(description="You didn't provide a status.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
		else:
			embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
	if isinstance(error, commands.MissingRequiredArgument):
		#embed = discord.Embed(description="You didn't provide a status.", color=0xFF3639)
		#embed.set_image(url=ctx.message.author.guild.icon_url)
		#embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		#embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		#await ctx.send(embed=embed)
		if(ctx.message.author.id == 495680416422821888 or ctx.message.author.id == 393839495859929089):
			if len(ctx.message.content) > 8:
				embed2 = discord.Embed(description="Since you didn't provide a valid **status_type** and/or **status_msg**, I think that the status is empty. I'll get the status by your message. (COULD **NOT BE WORKING PROPERLY**!)", color=0xf2f542)
				embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed2)
				status = ctx.message.content[7:]
				embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(status), color=0x000000)
				await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name='{}'.format(status), type=discord.ActivityType.playing))
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
				await ctx.send(embed=embed)
			else:
				embed = discord.Embed(description="You didn't provide a status.", color=0xFF3639)
				embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
				embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
				await ctx.send(embed=embed)
				return
		else:
			embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

# - Role Command:

async def parse_roles(ctx, role:str):
	try:
		id: int = int(role)
		role = ctx.guild.get_role(id)
		if role is not None:
			return role
	except ValueError:
		pass
	for guild_role in ctx.guild.roles:
		if role.lower() == guild_role.name.lower():
			return guild_role
	for guild_role in ctx.guild.roles:
		if role.lower() in guild_role.name.lower():
			return guild_role
	return None

@bot.command()
@commands.has_any_role("Role Perms", "$ dy")
async def role(ctx, user: discord.Member, *, rolee: str):
    role = await parse_roles(ctx, rolee)
    role1 = discord.utils.get(ctx.message.author.guild.roles, name="$ dy")
    role2 = discord.utils.get(ctx.message.author.guild.roles, name="scopes")
    role3 = discord.utils.get(ctx.message.author.guild.roles, name="Custom Bot")
    role4 = discord.utils.get(ctx.message.author.guild.roles, name="Bot Coder")
    role5 = discord.utils.get(ctx.message.author.guild.roles, name="YAGPDB.xyz")
    role6 = discord.utils.get(ctx.message.author.guild.roles, name="MEE6")
    role7 = discord.utils.get(ctx.message.author.guild.roles, name="Sx4")
    role8 = discord.utils.get(ctx.message.author.guild.roles, name=">.<")
    role9 = discord.utils.get(ctx.message.author.guild.roles, name="InviteManager")
    role10 = discord.utils.get(ctx.message.author.guild.roles, name="Owner")
    role11 = discord.utils.get(ctx.message.author.guild.roles, name="BOTs")
    role12 = discord.utils.get(ctx.message.author.guild.roles, name="« X »")
    role13 = discord.utils.get(ctx.message.author.guild.roles, name="Co Owner ‧₊˚ ༄")
    role14 = discord.utils.get(ctx.message.author.guild.roles, name="⫛ I E N D")
    role15 = discord.utils.get(ctx.message.author.guild.roles, name="Djimi")
    role16 = discord.utils.get(ctx.message.author.guild.roles, name="Blitzzy")
    role17 = discord.utils.get(ctx.message.author.guild.roles, name="BLURY")
    role18 = discord.utils.get(ctx.message.author.guild.roles, name="GiveawayBot")
    role19 = discord.utils.get(ctx.message.author.guild.roles, name="Dank Memer")
    role20 = discord.utils.get(ctx.message.author.guild.roles, name="Groovy")
    role21 = discord.utils.get(ctx.message.author.guild.roles, name="Community Manager")
    role22 = discord.utils.get(ctx.message.author.guild.roles, name="appbot")
    role23 = discord.utils.get(ctx.message.author.guild.roles, name="Head Admin ✧˚*:･")
    role24 = discord.utils.get(ctx.message.author.guild.roles, name="Admin ˚｡☆")
    role25 = discord.utils.get(ctx.message.author.guild.roles, name="Mod ˚｡⋆")
    role26 = discord.utils.get(ctx.message.author.guild.roles, name="logs access")
    role27 = discord.utils.get(ctx.message.author.guild.roles, name="Bot Coder")
    role28 = discord.utils.get(ctx.message.author.guild.roles, name="Trial Mod")
    role29 = discord.utils.get(ctx.message.author.guild.roles, name="Chat Moderator")
    role30 = discord.utils.get(ctx.message.author.guild.roles, name="Vc Moderator")
    role31 = discord.utils.get(ctx.message.author.guild.roles, name="Staff")
    role32 = discord.utils.get(ctx.message.author.guild.roles, name="Server Helper")
    role33 = discord.utils.get(ctx.message.author.guild.roles, name="Partnerships Team")
    role34 = discord.utils.get(ctx.message.author.guild.roles, name="Event Manager")
    role35 = discord.utils.get(ctx.message.author.guild.roles, name="RolePerms")
    roless = [role1, role2, role3, role4, role5, role6, role7, role8, role9, role10, role11, role12, role13, role14, role15, role16, role17, role18, role19, role20, role21, role22, role23, role24, role25, role26, role27, role28, role29, role30, role31, role32, role33, role34, role35]
    if role in roless and ctx.message.author.id != 495680416422821888:
        embed = discord.Embed(description="This role is locked. It can't be assigned.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
        return
    if role in user.roles:
        embed = discord.Embed(
            description="Successfully removed the **{}** role from **{}**.".format(str(role), user.mention),
            color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)
        await user.remove_roles(role)
        logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
        timestamp = datetime.now()
        corfor = timestamp.strftime("%d %b, %Y at %H:%M")
        log = discord.Embed(description="Used command ``!role`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(
            ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0x000000)
        log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        log.set_footer(text="{}".format(corfor))
        log.set_thumbnail(url=user.avatar_url)
        await logch.send(embed=log)
        return
    else:
        embed = discord.Embed(
            description="Successfully added the **{}** role to **{}**.".format(str(role), user.mention),
            color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)
        await user.add_roles(role)
        logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
        timestamp = datetime.now()
        corfor = timestamp.strftime("%d %b, %Y at %H:%M")
        log = discord.Embed(description="Used command ``!role`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(
            ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0x000000)
        log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        log.set_footer(text="{}".format(corfor))
        log.set_thumbnail(url=user.avatar_url)
        await logch.send(embed=log)
        return
	
@role.error    
async def role_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="You didn't give me a correct user and/or a role.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} look now, do i look like a magician? just mention a user and i'll ban them \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
	elif isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(description="You didn't give me a user and/or a role.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
		#await ctx.send("{} okay so, i can't read your mind, sorry, could you try giving me at least a member to ban? \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
	elif isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

# - Purge Command:
@bot.command()
@commands.has_any_role("Chat Moderator", "Mod ˚｡⋆", "Admin ˚｡☆", "Owner")
async def clean(ctx):
	def check(m):
		return m.author.bot
	#rr = todeln + 1
	ctx.message.delete()
	deleted = await ctx.message.channel.purge(limit=100, check=check)
	embed = discord.Embed(description="Cleaned bots' messages.", color=0x000000)
	embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
	msg = await ctx.send(embed=embed)
	await asyncio.sleep(5)
	await msg.delete()
	
@clean.error
async def clean_error(ctx, error):
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_any_role("Chat Moderator", "Mod ˚｡⋆", "Admin ˚｡☆", "Owner", "Co Owner")
async def purge(ctx, amount, *, user: discord.Member):
	try:
		todeln = int(amount)
	except:
		ctx.message.delete()
		embed = discord.Embed(description="You didn't enter a number between 2 and 200.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		msg = await ctx.send(embed=embed)
		await asyncio.sleep(10)
		await msg.delete()
		return
	if(todeln > 0):
		def check(m):
			return m.author == user
		#rr = todeln + 1
		await ctx.message.delete()
		deleted = await ctx.message.channel.purge(limit=todeln, check=check)
		embed = discord.Embed(description="Successfully purged **{}** messages by **{}**.".format(todeln, user.mention), color=0x000000)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_thumbnail(url=user.avatar_url)
		msg = await ctx.send(embed=embed)
		await asyncio.sleep(5)
		await msg.delete()
		logch = discord.utils.get(ctx.message.author.guild.channels, name="logs")
		timestamp=datetime.datetime.now()
		corfor = timestamp.strftime("%d %b, %Y at %H:%M")
		log = discord.Embed(description="Used command ``!purge`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF)
		log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		log.set_footer(text="{}".format(corfor))
		log.set_thumbnail(url=user.avatar_url)
		await logch.send(embed=log)
		
@purge.error
async def purge_error(ctx, error):
	if isinstance(error, commands.BadArgument):
		embed = discord.Embed(description="I couldn't find this user.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	if isinstance(error, commands.MissingRequiredArgument):
		todeln = int(ctx.message.content[7:])
		if(todeln < 200 and todeln > 2):
			deleted = await ctx.message.channel.purge(limit=(todeln + 1))
			embed = discord.Embed(description="Successfully purged **{}** messages.".format(todeln), color=0x000000)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			await ctx.send(embed=embed)
			logch = discord.utils.get(ctx.message.author.guild.channels, name="enightclub-logs")
			timestamp=datetime.datetime.now()
			corfor = timestamp.strftime("%d %b, %Y at %H:%M")
			log = discord.Embed(description="Used command ``!purge`` in {}:\n{}\n\nMod ID: {}".format(ctx.message.channel.mention, ctx.message.content, ctx.message.author.id), color=0xFFFFFF)
			log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			log.set_footer(text="{}".format(corfor))
			#log.set_thumbnail(url=user.avatar_url)
			await logch.send(embed=log)
			return
		else:
			embed = discord.Embed(description="There's a limit of 200 messages per purge. You entered a higher number than that.", color=0xFF3639)
			embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
			embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
			await ctx.send(embed=embed)
			return
	if isinstance(error, commands.CheckFailure):
		embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
		embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
		embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
		await ctx.send(embed=embed)
	else:
		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, None, file=sys.stderr)

			      
# CONFUESS CMD 
@bot.command()
async def confess(ctx, *, msg: str):
    await ctx.message.delete()
    chan = discord.utils.get(ctx.message.author.guild.channels, name="☆│confessions")
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

# dm
@bot.command()
@commands.has_any_role("$ dy", "Bot Coder")
async def dm(ctx, user: discord.Member, *, msg: str=""):
    await ctx.message.delete()
    await user.send(f"{msg}")

@dm.error
async def dm_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(title="User not found.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="You didn't give me a correct user/message.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CheckFailure):
        embed = discord.Embed(title="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

# Under tests:

@bot.command()
async def restart(ctx):
	await ctx.send("**Closing connection to Heroku...**")
	await bot.logout(os.environ.get("token"))
	await ctx.send("**Re-connecting to Discord...**")
	await bot.start()

@bot.command()
async def r(ctx):
	await ctx.send("```HEROKU\nRestarting```")
	await ctx.send("```State changed from up to starting```")
	await ctx.send("```Starting process with command python main.py```")
	await bot.start(os.environ.get("token"))
	await bot.logout()
	await ctx.send("```State changed from starting to up```")
	await ctx.send("```Process exited with status 0```")
	await ctx.send("**Restarted.**")

# - BOT LOGIN


bot.run(os.environ.get("token"))
