import discord
from discord import Message, Guild, Member
from typing import Optional
from discord.ext import commands

import os
import sys
import traceback
import asyncio
from datetime import datetime
import datetime
import random
import json
import requests

# ~MatKrulli: lazy import because I'm lazy
from common_vars import *

# ~MatKrulli: this will ensure the commands from custom_commands.general are properly added to the bot
import custom_commands.general
import custom_commands.fun
import custom_commands.mod
import custom_commands.admin
import custom_commands.beta
import custom_commands.botOwner

bot.remove_command('help')

@bot.event
async def on_ready():
    global guild
    guild = bot.get_guild(618048944840245248)
    # testguild = bot.get_guild(617866004978073620)
    thischannell = bot.get_channel(632904178100076565)
    # msggg = await thischannell.fetch_message(633576140409405440)

    # allTimeMessages = int(msggg.content)

    # global shiki
    # shiki = server.get_member(237938976999079948)

    await bot.change_presence(activity=discord.Game(name='!help'))
    print('started.')

    await bot.wait_until_ready()
    # guildd = bot.get_guild(618048944840245248)
    # print("+++++++++++++++ \n" + str(guildd) + "+++++++++++++++++++")
    # while True:
    # chann = bot.get_channel(633785042606489655)
    # await chann.send("<@237938976999079948>")
    # await asyncio.sleep(2)

    while True:
        global msgsCounterrr
        msgsCounterrr = 0
        await asyncio.sleep(3600)


# welcome message

@bot.event
async def on_member_join(member):
    if member.guild.id == 642429293330300971:
        rol = discord.utils.get(member.guild.roles, name="Members 💖")
        await member.add_roles(rol)
        mbrcnt = bot.get_channel(642482823445479424)
        await mbrcnt.edit(name="{} SNOWIES ❄️".format(member.guild.member_count))
        channel = bot.get_channel(642482771511476234)
        channel2 = bot.get_channel(642482763295096857)
        channel3 = bot.get_channel(642482769049681930)
        channel4 = bot.get_channel(642482769833885736)
        embed = discord.Embed(
            description="Welcome to **[Ａｓｍｏｄｅｕｓ](https://discord.gg/h945y6T)**! You're the **{}th** member. \n\n Make sure to read: {}  \n\nRoles: {} \nColors: {}.".format(
                member.guild.member_count, channel2.mention, channel3.mention, channel4.mention), color=0x000000)
        embed.set_author(name="{}".format(member), icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.guild.icon_url)
        await channel.send("{}".format(member.mention), embed=embed)
        # channel4 = discord.utils.get(member.guild.channels, name="♥‿♥welcome-goodbye♥‿♥")
        # await channel4.send("Welcome to **defying ღ thots**, **{}** ({}) has joined the server. We now have **{}** members.".format(member, member.mention, member.guild.member_count))
        loggg = discord.utils.get(member.guild.channels, name="join-leave-logs")
        await loggg.send(f"{member} ({member.mention}, {member.id}) joined.")

        # await channel.send("Welcome {} to **e nightclub!** You’re the **{}** member. \n\n Make sure to read: {}  |  Roles: {}  |  For help:  {}.".format(member.mention, member.guild.member_count, channel2.mention, channel3.mention, channel4.mention))
        chan = bot.get_channel(642482769049681930)
        msg = await chan.send(f"Ay {member.mention}, feel free to check out our roles and grab some. :)")
        await asyncio.sleep(60)
        await msg.delete()


# leave message & join message.

@bot.event
async def on_member_remove(member):
    if member.guild.id == 642429293330300971:
        mbrcnt = bot.get_channel(642482823445479424)
        await mbrcnt.edit(name="{} SNOWIES ❄️".format(member.guild.member_count))
        # channel = discord.utils.get(member.guild.channels, name="♥‿♥welcome-goodbye♥‿♥")
        # await channel.send("**{}** ({}) has left the server. We now have **{}** members.".format(member, member.mention, member.guild.member_count))
        loggg = discord.utils.get(member.guild.channels, name="join-leave-logs")
        await loggg.send(f"{member} ({member.mention}, {member.id}) left.")

@bot.event
async def on_message(message: Message):
    #if ((message.channel.id == 642482771511476234) or (message.channel.id == 629056727186407445)) and message.author.bot and message.author.id != 640827656660582400:
    #    await message.delete()
    #    return
    if message.channel.id == 642482779111555072 or message.channel.id == 642482779925250067 or message.channel.id == 642482780797665290 or message.channel.id == 642482781812686866:
        if len(message.attachments) == 0:
            await message.delete()
            await message.author.send(
                "> :red_circle: You're only allowed to post images in {}.".format(message.channel.mention))
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
        embed = discord.Embed(
            description="You can invite me from [here](https://discordapp.com/oauth2/authorize?client_id=640827656660582400&scope=bot&permissions=2097151191)!")
        await message.channel.send(embed=embed)
    if message.content == "/get repo":
        embed = discord.Embed(description="[My insides~](https://www.github.com/Shikiiii/Asmodeus)")
        await message.channel.send(embed=embed)
    if message.channel.id == 642482769833885736:
        role_names = {"Light Red", "Light Orange", "Light Purple", "Light Yellow", "Light Cyan", "Light Blue",
                      "Light Green", "Light Pink", "Dark Red", "Dark Blue", "Dark Purple", "Dark Pink",
                      "Crimson", "Black", "Gray", "Indigo", "Lavender", "Violet", "White", "Magenta"}
        await message.delete()
        if message.content == "none":
            toremove = []
            for user_role in message.author.roles:
                if user_role.name in role_names:
                    toremove.append(user_role)
            for user_role in toremove:
                await message.author.remove_roles(user_role)
            return
        rolee = await convert_color_menu(message.content)
        if rolee == "none":
            new_role = discord.utils.get(message.author.guild.roles, name=message.content)
            if hasattr(new_role, "id"):
                toremove = []
                for user_role in message.author.roles:
                    if user_role.name in role_names:
                        toremove.append(user_role)
                for user_role in toremove:
                    await message.author.remove_roles(user_role)
                await message.author.add_roles(new_role)
        else:
            new_role = discord.utils.get(message.author.guild.roles, name=rolee)
            toremove = []
            for user_role in message.author.roles:
                if user_role.name in role_names:
                    toremove.append(user_role)
            for user_role in toremove:
                await message.author.remove_roles(user_role)
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
    if (message.content == "!welcome" and (
            message.author.id == 237938976999079948 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**༚ ✧˳⁺ __Welcome to Ａｓｍｏｄｅｕｓ!__  ⁺˳✧ ༚**",
                               description="- We are so glad to have you join our server! By joining this server you agreed to our rules. \r\n\r\n - We have over 100+ roles, channels and some bots to play different games and much more! \r\n\r\n - Our channels are not aggressively moderated so feel free to join any conversation you like.",
                               color=0xC5FCFC)
        embed2 = discord.Embed(color=0xC5FCFC)
        embed2.set_image(url="https://cdn.discordapp.com/attachments/635581513228091462/637970310095831061/Untitled-1.png")
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed1)
    elif (message.content == "!rules" and (
            message.author.id == 237938976999079948 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**༚ ✧˳⁺ __Server rules__ ⁺˳✧ ༚**",
                               description="__``1``__ • Make sure to follow the [Discord TOS](https://discordapp.com/terms) and the [Community Guidelines](https://discordapp.com/guidelines). \r\n\r\n __``2``__ • Keep content in the appropriate channels. This includes only posting NSFW content in NSFW marked channels. \r\n\r\n __``3``__ • No Doxing / Do not leak someone's IP address / Do not share personal information of anyone. \r\n\r\n __``4``__ • Any type of serious harassment will result in a ban. If you're not sure about whether something you've done is harassment, check out the [guidelines](https://discordapp.com/guidelines). \r\n\r\n __``5``__ • No advertising (Including PM advertisement). \r\n\r\n __``6``__ • Do NOT tell people to kill themselves (even if it's a joke). \r\n\r\n __``7``__ • Do not impersonate other users. Impersonating our staff team or discord staff will result in a permanent ban. \r\n\r\n __``8``__ • Remember that this server is English only! Try to avoid using any other languages so everyone can understand each other and have fun. \r\n\r\n __``9``__ • Respect all staff and follow their instruction(s). \r\n\r\n __``10``__ • Do NOT set people up against each other. \r\n\r\n __``11``__ • Respect people's wishes considering revealing their age, face reveal etc. \r\n\r\n __``12``__ • Asking for nudes or for other information is ABSOLUTELY not accepted here and will result in a ban. \r\n\r\n **- Please contact <@237938976999079948> if you have any issues with our staff team and/or the rules posted above.** \r\n\r\n **- Thank you for joining Ａｓｍｏｄｅｕｓ! We hope you have a great stay here!**",
                               color=0xC5FCFC)
        embed2 = discord.Embed(color=0xC5FCFC)
        embed2.set_image(url="https://media.giphy.com/media/kD0G3PwfsUhUzQu3QQ/giphy.gif")
        embed3 = discord.Embed(title="**༚ ✧˳⁺ __Voice Chat rules__ ⁺˳✧ ༚**",
                               description="__``1``__ • Don't ear rape other people with music or with your mic. \r\n\r\n __``2``__ • Do not spam music, let other people play their song. \r\n\r\n __``3``__ • Do not stop the music if there are still others in the voice channel. \r\n\r\n __``4``__ • Do not mic spam, yell or disturb others. \r\n\r\n __``5``__ • Do NOT be toxic or be racist.",
                               color=0xC5FCFC)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed3)
        await message.channel.send(embed=embed1)
    elif (message.content == "!faq" and (
            message.author.id == 237938976999079948 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="*__**FAQ**:__*",
                               description="__**How can I level up?**__ \r\n\r\n To level up you have to be active in any channel in the server, avoid spamming. Spamming won't level you up. \r\n\r\n __**Is there a way to get picture perms/embed links?**__ \r\n\r\n Yes there is a way to get these perms, when you reach **level 10+** you'll be able to post pictures or links.. \r\n\r\n __**Someone is advertising in my DMS what do I do?**__ \r\n\r\n Dm a staff member and they'll ban them as soon as possible. \r\n\r\n __**Staff is abusing his perms, what do I do?**__ \r\n\r\n DM <@237938976999079948>. \r\n\r\n __**Do you guys do giveaways and events?**__ \r\n\r\n Yes we do events and giveaways sometimes. \r\n\r\n __**I want to apply for a Partner Manager, how can I do that?**__ \r\n\r\n DM <@237938976999079948>.",
                               color=0xC5FCFC)
        embed2 = discord.Embed(color=0xC5FCFC)
        embed2.set_image(url="https://media.giphy.com/media/WtISnEdn9w4jjSZNtC/giphy.gif")
        embed3 = discord.Embed(title="",
                               description="__**Can we be partners?**__ \r\n\r\n Sure! You can be partner with us by messaging one of the PMs.\r\n\r\n __**I got banned for no reason, what do I do?**__ \r\n\r\n Simply DM the owner <@237938976999079948> and I'll unban you as soon as possible! \r\n\r\n __**Can I get a color?**__ \r\n\r\n Yes, you can pick a color form our [colors menu](https://discordapp.com/channels/627928375989764138/629061888646316032/629220377637421067). \r\n\r\n __**Someone leaked my pictures, IP, phone number. What do I do?**__ \r\n\r\n DM one of the staff members and they'll ban them. \r\n\r\n __**When was this server created?**__ \r\n\r\n created on 29/9/2019, but was released public on 14/10/2019. \r\n\r\n __**Is this a dating server?**__ \r\n\r\n Nope, this is a chill server to talk to new people and make friends. However, we won't stop you if you're dating **__AND__** you're 18 or above.",
                               color=0xC5FCFC)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed1)
        await message.channel.send(embed=embed3)
    elif (message.content == "!staff" and (
            message.author.id == 237938976999079948 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**__Staff Members:__**",
                               description="☆ - Owners: glow <@514392208254959618> | Shiki <@237938976999079948>. \r\n\r\n ☆ - Co Owners: zyzz <@543885407071371340>\r\n\r\n☆ - Admins: zip <@267631540811464704> \r\n\r\n ☆ - Mods: Alex <@444751983786852362> | System <@316988095562252290>",
                               color=0xFF93F0)
        embed2 = discord.Embed(color=0xFF93F0)
        embed2.set_image(url="https://media.giphy.com/media/Xy1debdAWrNLK3cnHk/giphy.gif")
        embed3 = discord.Embed(title="**__Perm invite links:__**",
                               description="🔗 Perm invite link: https://discord.gg/GJ5UDth", color=0xFF93F0)
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed1)
        await message.channel.send(embed=embed3)
    elif (message.content == "!verification" and (
            message.author.id == 237938976999079948 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**༚ ✧˳⁺ Verification ⁺˳✧ ༚**",
                               description="✧ - Post selfie in <#627942893448986713> with \"Shiki\" written on a piece of paper. \r\n\r\n ✧ - Verified role gives you access to <#627942990186283039> or <#627943195069775912> depends on your gender. \r\n\r\n If you're feeling uncomfortable with posting your selfie, you can DM the selfie to the owner.",
                               color=0xC5FCFC)
        # embed2 = discord.Embed(color=0xFF93F0)
        await message.channel.send(embed=embed1)
    elif message.content == "info":
        await message.channel.send(
            "Hi! I'm currently in **{}** guilds, seeing a total of **{}** users.\n**{}** messages were sent in the past hour, and **{}** messages were sent since last restart.\n**{}** messages were sent in global (LAST RESET: 13/10/19 @ 2:55PM GTM+3)".format(
                len(bot.guilds), len(bot.users), msgsCounterrr, msgsCounterr, allTimeMessages))
    elif message.content == "invite":
        online = 0
        for member in message.guild.members:
            if member.status != discord.Status.offline:
                online += 1
        embed = discord.Embed(
            description="\n[Ａｓｍｏｄｅｕｓ](https://discord.gg/ANQSkTq) \n\n- e-girls, fun, socializing, chilling and more! \n\n⬤ {} Online ⭘ {} Members".format(
                online, message.guild.member_count), color=0x000000)
        embed.set_author(name="YOU'VE BEEN INVITED TO JOIN A SERVER\n", icon_url=message.author.avatar_url)
        embed.set_thumbnail(url=message.guild.icon_url)
        await message.channel.send(embed=embed)
        msg = await message.channel.send("Get the direct link DMed to you by reacting here!")
        await msg.add_reaction("📧")

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '📧'

        try:
            await bot.wait_for('reaction_add', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await msg.delete()
        else:
            try:
                await message.author.send("Direct link: https://discord.gg/ANQSkTq", embed=embed)
            except:
                await message.channel.send("{}, your DMs are disabled, so I couldn't DM you the invite link!".format(
                    message.author.mention))
            await msg.delete()
    # dy  & shiki dms commands:

    #  if "xxx" in message.content:
    #   await message.author.send("Hi")
    # elif shiki in message.mentions:
    # await message.author.send(f"Hey there, {message.author.mention}! \nPlease don't abusively mention the Devs without a reason. If you want to just talk to them, it's okay, but don't don it oftenly without a real reason. But while you're here... \n\n Are you looking for **cheap** and sometimes **free** __bot developing and hosting__? Our **custom bot**, <@593090256560193549> was made by the user you just pinged, {shiki.mention}. \n\n If you're interesting in having a custom bot like this one, **DM {shiki.mention}** and we'll talk about it there. \n\n > This automatic action was fired because you pinged either the Bot Coder role or {shiki.mention}.")
    elif message.content == "shiki":
        await message.channel.send("dm <@237938976999079948> with thigh pics for free admin aha x")
    elif message.content == "!!apply":
        await message.channel.send("Thank you for applying! Please check your DMs to complete the application.")
    elif message.content == "no u" and message.author.bot == False:
        await message.channel.send("no u")
    elif message.content == "glow":
        await message.channel.send("O_O")
    elif message.content == "alex":
        await message.channel.send("biggest retard")
    elif message.content == "kam" or message.content == "kamera":
        await message.channel.send("dm <@567799351368482826> for a Daddy :wink:")
    elif message.content == "madz":
        await message.channel.send("shrek is love, shrek is life")
    elif message.content == "meg":
        await message.channel.send("wooden hoe *with loyalty 1")

    await bot.process_commands(message)

@bot.event
async def on_message_delete(message: Message):
    if message.author.bot == False:
        logch = discord.utils.get(message.author.guild.channels, name="logs")
        timestamp = datetime.datetime.now()
        corfor = timestamp.strftime("%d %b, %Y at %H:%M")
        log = discord.Embed(
            description="Deleted a message in {}: \n{}\n\nUsers ID: {}".format(message.channel.mention, message.content,
                                                                               message.author.id), color=0xFFFFFF)
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


@bot.event
async def on_message_edit(before, after):
    if before.author.bot == False:
        # print(before)
        # print(after)
        logch = discord.utils.get(before.author.guild.channels, name="logs")
        timestamp = datetime.datetime.now()
        corfor = timestamp.strftime("%d %b, %Y at %H:%M")
        log = discord.Embed(description="Edited a message in {}: \n``Old:``\n{}\n``New:``\n{}\n\nUsers ID: {}".format(
            before.channel.mention, before.content, after.content, before.author.id), color=0xFFFFFF)
        log.set_author(name="{}".format(before.author), icon_url=before.author.avatar_url)
        log.set_footer(text="{}".format(corfor))
        log.set_thumbnail(url=before.author.avatar_url)
        await logch.send(embed=log)

        toeditsnipe[before.channel.id] = before.content
        toeditsnipeauthors[before.channel.id] = before.author
        timestamp2 = datetime.datetime.now()
        corfor = timestamp2.strftime("%d %b, %Y at %H:%M")
        toeditsnipetime[before.channel.id] = timestamp2


# BETA COMMANDS

@bot.command()
async def help(ctx, *, mdl: str):
    selfbotasmember = ctx.guild.get_member(594131533745356804)
    print(selfbotasmember)
    if mdl == "general":
        embed = discord.Embed(title="Module: General",
                              description="To view more info about a command, use ``!cmdhelp command``.",
                              color=0x000000)
        embed.add_field(name="Commands:",
                        value="``nick``, ``reply``, ``afk``, ``define``, ``ping``, ``snipe``, ``editsnipe``, ``reminder``, ``remindercancel``, ``reminderdm``, ``reminderdmcancel``, ``avatar``, ``avatarid``, ``userinfo``, ``serverinfo``, ``membercount``")
        embed.set_author(name="{}".format(str(bot.user.name)), icon_url=str(bot.user.avatar_url))
        await ctx.send(embed=embed)
    elif mdl == "fun":
        embed = discord.Embed(title="Module: Fun",
                              description="To view more info about a command, use ``!cmdhelp command``.",
                              color=0x000000)
        embed.add_field(name="Commands:",
                        value="``facepalm``, ``poke``, ``blush``, ``pat``, ``kiss``, ``hug``, ``cuddle``, ``slap``, ``howgay``, ``howlesbian``, ``howhot``, ``thotrate``, ``8ball``, ``rate``, ``roast``, ``penis``, ``ship``, ``coinflip``")
        embed.set_author(name="{}".format(str(bot.user.name)), icon_url=str(bot.user.avatar_url))
        await ctx.send(embed=embed)
    elif mdl == "mod":
        embed = discord.Embed(title="Module: Moderation",
                              description="To view more info about a command, use ``!cmdhelp command``.",
                              color=0x000000)
        embed.add_field(name="Commands:",
                        value="``ban``, ``unban``, ``banid``, ``kick``, ``mute``, ``unmute``, ``purge``, ``clean``")
        embed.set_author(name="{}".format(str(bot.user.name)), icon_url=str(bot.user.avatar_url))
        await ctx.send(embed=embed)
    elif mdl == "admin":
        embed = discord.Embed(title="Module: Administrator",
                              description="To view more info about a command, use ``!cmdhelp command``.",
                              color=0x000000)
        embed.add_field(name="Commands:",
                        value="``lockdown``, ``role``, ``masskick``, ``massmute``, ``massban``, ``bots``")
        embed.set_author(name="{}".format(str(bot.user.name)), icon_url=str(bot.user.avatar_url))
        await ctx.send(embed=embed)
    elif mdl == "bot_owners":
        embed = discord.Embed(title="Module: Owners",
                              description="To view more info about a command, use ``!cmdhelp command``.",
                              color=0x000000)
        embed.add_field(name="Commands:", value="``say``, ``status``, ``verify``")
        embed.set_author(name="{}".format(str(bot.user.name)), icon_url=str(bot.user.avatar_url))
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Modules:",
                              description="``!help general`` | General Commands\n``!help fun`` | Fun Commands\n``!help mod`` | Moderation Commands\n``!help admin`` | Administration Commands\n``!help bot_owners`` | Bot Owners Commands",
                              color=0x000000)
        embed.set_author(name="{}".format(str(bot.user.name)), icon_url=str(bot.user.avatar_url))
        await ctx.send(embed=embed)


@help.error
async def help_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Modules:",
                              description="``!help general`` | General Commands\n``!help fun`` | Fun Commands\n``!help mod`` | Moderation Commands\n``!help admin`` | Administration Commands\n``!help bot_owners`` | Bot Owners Commands",
                              color=0x000000)
        embed.set_author(name="{}".format(str(bot.user.name)), icon_url=str(bot.user.avatar_url))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)


@bot.command()
async def cmdhelp(ctx, *, cmd: str):
    if cmd == "help":
        embed = discord.Embed(title="!help [module]",
                              description="Gets the help menu with the modules / of a module. It includes all commands.\n\nExample: ``!help fun``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "massban":
        embed = discord.Embed(title="!massban @members",
                              description="Bans all the @mentioned members. \n\nExample: ``!ban @Shiki @Alex @Tess``",
                              color=0x000000)
        await ctx.send(embed=embed)
    elif cmd == "masskick":
        embed = discord.Embed(title="!masskick @members",
                              description="Kicks all the @mentioned members. \n\nExample: ``!kick @Shiki @Alex @Tess``",
                              color=0x000000)
        await ctx.send(embed=embed)
    elif cmd == "massmute":
        embed = discord.Embed(title="!massmute @members",
                              description="Mutes all the @mentioned members. \n\nExample: ``!mute @Shiki @Alex @Tess``",
                              color=0x000000)
        await ctx.send(embed=embed)
    elif cmd == "nick":
        embed = discord.Embed(title="!nick [member] [newNickname]",
                              description="Changes either yours or someone's nickname. \n\nExample: ``!nick @Alex boomer``",
                              color=0x000000)
        await ctx.send(embed=embed)
    elif cmd == "reply":
        embed = discord.Embed(title="!reply [message.id] [content]",
                              description="**Note: The message __must be__ in the same channel where the command is ran. If you don't know how to get a message ID, check [this](https://support.discordapp.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-).**\nReplies to the given message with [content].\nAlias: ``!r``\n\nExample: ``!reply 640474593605189642 not much, hbu?``",
                              color=0x000000)
        await ctx.send(embed=embed)
    elif cmd == "afk":
        embed = discord.Embed(title="!afk [message]",
                              description="Sets your AFK, the [message] will be displayed whenever someone @mentions you.\n\nExample: ``!afk eating``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "define":
        embed = discord.Embed(title="!define [term]",
                              description="Searches for a definition in UrbanDictionary.\nAlias: ``!urban``.\n\nExample: ``!define jkjk``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "ping":
        embed = discord.Embed(title="!ping", description="Gets the bot's ping.", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "snipe":
        embed = discord.Embed(title="!snipe", description="Gets the last deleted message in the channel.",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "editsnipe":
        embed = discord.Embed(title="!editsnipe",
                              description="Gets the last edited message in the channel, showing the message before the edit.",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "reminder":
        embed = discord.Embed(title="!reminder [time] [message]",
                              description="Sets a reminder that will be send in the channel you used the command in. Correct time uses are ``s`` for seconds, ``m`` for minutes, ``h`` for hours and ``d`` for days. Maximum is 7 days. You are allowed to 1 reminder at the same time. \n\nExample: ``!reminder 2h read that new book I got``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "remindercancel":
        embed = discord.Embed(title="!remindercancel", description="Cancels your current reminder.", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "reminderdm":
        embed = discord.Embed(title="!reminderdm [time] [message]",
                              description="Sets a reminder that will be send in your DMs. Correct time uses are ``s`` for seconds, ``m`` for minutes, ``h`` for hours and ``d`` for days. Maximum is 7 days. You are allowed to 1 reminder at the same time. \n\nExample: ``!reminderdm 2h fap idk``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "reminderdmcancel":
        embed = discord.Embed(title="!reminderdmcancel", description="Cancels your current DM reminder.",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "avatar":
        embed = discord.Embed(title="!avatar [user]",
                              description="Gets someone's avatar. Your avatar will be shown if ``user`` is None.\nAlias: ``!av``.\n\nExample: ``!avatar @Shiki``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "avatarid":
        embed = discord.Embed(title="!aavatarid [id]",
                              description="Gets someone's avatar. This command can get the avatar of a user that's not in the server. Works with IDs.\nAlias: ``!avid``.\n\nExample: ``!avatarid 237938976999079948``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "userinfo":
        embed = discord.Embed(title="!userinfo [user]",
                              description="Gets someone's account info.\nAlias: ``!uf``, ``!whois``.\n\nExample: ``!userinfo dy``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "facepalm":
        embed = discord.Embed(title="!facepalm",
                              description="Facepalms.",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "pokes":
        embed = discord.Embed(title="!poke [user]",
                              description="Pokes someone, showing a random gif from Tenor. If ``user`` is None, the command will still work.\n\nExample: ``!poke @Shiki``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "pat":
        embed = discord.Embed(title="!pat [user]",
                              description="Pats someone, showing a random gif from Tenor. If ``user`` is None, the command will still work.\n\nExample: ``!pat @Shiki``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "blush":
        embed = discord.Embed(title="!blush",
                              description="You. . blush. And that's hella cute.",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "kiss":
        embed = discord.Embed(title="!kiss [user]",
                              description="Kisses someone, showing a random gif from Tenor. If ``user`` is None, the command will still work.\n\nExample: ``!kiss @Shiki``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "hug":
        embed = discord.Embed(title="!hug [user]",
                              description="Hugs someone, showing a random gif from Tenor. If ``user`` is None, the command will still work.\n\nExample: ``!hug @dy``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "cuddle":
        embed = discord.Embed(title="!cuddle [user]",
                              description="Cuddles someone, showing a random gif from Tenor. If ``user`` is None, the command will still work.\n\nExample: ``!cuddle @idk``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "slap":
        embed = discord.Embed(title="!slap [user]",
                              description="Slaps someone, showing a random gif from Tenor. If ``user`` is None, the command will still work.\n\nExample: ``!slap @youmom``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "howgay":
        embed = discord.Embed(title="!howgay [user]",
                              description="Shows the gayness of the user you gave.\n\nExample: ``!howgay @dy``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "howlesbian":
        embed = discord.Embed(title="!howlesbian [user]",
                              description="Shows how lesbian someone is.\n\nExample: ``!howlesbian @idk``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "howhot":
        embed = discord.Embed(title="!howhot [user]",
                              description="Shows how hot someone is.\n\nExample: ``!howhot @idk``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "thotrate":
        embed = discord.Embed(title="!thotrate [user]",
                              description="Shows the thot rate of the user you gave.\n\nExample: ``!thotrate @Shiki(LOL NO PLEASE)``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "rate":
        embed = discord.Embed(title="!rate [dy/shiki] [user]",
                              description="Rates the user you gave with the rate you chose, either ``dy`` or ``shiki``.\n\nExample: ``!rate shiki @dy``",
                              color=0x000000)
        await ctx.send(embed=embed)
    elif cmd == "8ball":
        embed = discord.Embed(title="!8ball [question]",
                              description="Answers your question using magic.\n\nExample: ``!8ball am i cool?``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "roast":
        embed = discord.Embed(title="!roast [user]",
                              description="Roasts the user you gave. The roasts are fire.\n\nExample: ``!roast @someone``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "penis":
        embed = discord.Embed(title="!penis [user]",
                              description="Shows someone's pee pee size.\n\nExample: ``!penis @dy``", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "ship":
        embed = discord.Embed(title="!ship [user1] [user2]",
                              description="Matches 2 users. Lovely.\n\nExample: ``!match @shiki @idk``", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "coinflip":
        embed = discord.Embed(title="!coinflip",
                              description="Flips a coin. Lands either on heads or trails.\nAlias: ``!cf``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "kick":
        embed = discord.Embed(title="!kick [user] [reason]",
                              description="Kicks the user you gave.\n\nExample: ``!kick @dy idk``", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "mute":
        embed = discord.Embed(title="!mute [user] [reason]",
                              description="Mutes the user you gave for permanet.\n\nExample: ``!mute @Shiki idk``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "unmute":
        embed = discord.Embed(title="!unmute [user] [reason]",
                              description="Unmutes the user you gave.\n\nExample: ``!unmute @Shiki idk``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "purge":
        embed = discord.Embed(title="!purge [amount] [user]",
                              description="Purges ``amount`` messages. User is optional. Maximum is 200.\n\nExample: ``!purge 10 @Shiki``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "clean":
        embed = discord.Embed(title="!clean", description="Cleans up to 100 of the bot's messages in this channel.",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "serverinfo":
        embed = discord.Embed(title="!serverinfo", description="Shows the server info.", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "membercount":
        embed = discord.Embed(title="!membercount", description="Shows the member count of the server.", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "members":
        embed = discord.Embed(title="!members [role]",
                              description="Shows the members that have the given role.\n\nExample: ``!members owner``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "ban":
        embed = discord.Embed(title="!ban [user] [reason]",
                              description="Bans the given user.\n\nExample: ``!ban @dy idk``", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "banid":
        embed = discord.Embed(title="!banid [id]",
                              description="Bans a user that's not in the server using their ID.\n\nExample: ``!banid 395802215190888498``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "unban":
        embed = discord.Embed(title="!unban [id]",
                              description="Unbans the given user with their ID.\n\nExample: ``!unban 395802215190888498``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "status":
        embed = discord.Embed(title="!status [o/i/d] [p/w/l] [message]",
                              description="Changes the bot's status. Online, idle or do not disturb. Playing, watching or listening to.\n\nExample: ``!status o w you sleep.``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif(cmd == "verify"):
  	    embed = discord.Embed(title="!verify [user] [male/female]", description="Verifies the user to either male or female.\nAlias: ``!v``\n\nExample: ``!verify @dy m``", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "lockdown":
        embed = discord.Embed(title="!lockdown",
                              description="Locks the channel where the message was sent in. To unlock, type !lockdown again.",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "role":
        embed = discord.Embed(title="!role [user] [role]",
                              description="Gives/Removes the given role to/from the given user.\n\nExample: ``!role @Shiki retard``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "say":
        embed = discord.Embed(title="!say [channel] [message]",
                              description="The bot says whatever the [message] is. Channel is optional.\n\nExample: ``!say #asd asd``",
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    elif cmd == "bots":
        embed = discord.Embed(title="!bots", description="Lists all the bots in the server.", color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="This isn't a valid command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)              

bot.run(os.environ.get("token"))
