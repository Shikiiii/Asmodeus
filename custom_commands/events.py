import discord
from discord import Message, Guild, Member
from discord.ext import commands
import random
import sys
import traceback
import asyncio
import datetime
import json
from datetime import datetime

from common_vars import *

@bot.event
async def on_ready():
    global guild
    guild = bot.get_guild(618048944840245248)
    thischannell = bot.get_channel(632904178100076565)

    await bot.change_presence(activity=discord.Game(name='!help'))
    print('started.')

    await bot.wait_until_ready()
    storage = bot.get_guild(646432280365236235)
    storagePrefix = storage.get_channel(646432846961049601)
    storageSB = storage.get_channel(647616003164864514)
    # Here, we get the prefixes, so we don't have to scan the channel everytime a command is ran. - Shiki
    async for message in storagePrefix.history():
        x = message.content.split("|")
        id = x[0]
        prefix = x[1]
        serverPrefixes[str(id)] = str(prefix)
        serverPrefixesToDelete[id] = message.id
    async for message in storageSB.history():
        x = message.content.split("|")
        guildID = x[0]
        chan = x[1]
        starboardChannels[str(guildID)] = str(chan)
        starboardChannelsToDelete[guildID] = message.id
        

    #vc = bot.get_channel(642482823445479424)
    #await vc.connect()

    while True:
        global msgsCounterrr
        msgsCounterrr = 0
        await asyncio.sleep(3600)

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "⭐":
        if reaction.count >= 5:
            for key, value in starboardChannels.items():
                if int(key) == reaction.message.author.guild.id:
                    chan = bot.get_channel(int(value))
                    for key, value in starboardMessages.items():
                        if int(key) == reaction.message.channel.id:
                            if int(value) == reaction.message.id:
                                return
                    embed = discord.Embed(description="{}\n\n[JUMP TO MESSAGE](https://discordapp.com/channels/{}/{}/{})".format(reaction.message.content, reaction.message.guild.id, reaction.message.channel.id, reaction.message.id), color=0xffff00, timestamp=datetime.utcnow())
                    embed.set_author(name="{}".format(reaction.message.author.name), icon_url=reaction.message.author.avatar_url)
                    if len(reaction.message.attachments) > 0:
                        if reaction.message.attachments[0].height is not None:
                            embed.set_image(url=reaction.message.attachments[0].url)
                    await chan.send(embed=embed)
                    embed2 = discord.Embed(description=":crown: {}'s message has been added to the starboard!".format(reaction.message.author.name), color=0xffff00)
                    await reaction.message.channel.send(embed=embed2)
                    starboardMessages[reaction.message.channel.id] = reaction.message.id
        
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
        loggg = discord.utils.get(member.guild.channels, name="join-leave-logs")
        await loggg.send(f"{member} ({member.mention}, {member.id}) joined.")
        await asyncio.sleep(60)
        await msg.delete()

@bot.event
async def on_member_remove(member):
    if member.guild.id == 642429293330300971:
        mbrcnt = bot.get_channel(642482823445479424)
        await mbrcnt.edit(name="{} SNOWIES ❄️".format(member.guild.member_count))
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
                      "Crimson", "Black", "Gray", "Indigo", "Lavender", "Violet", "White", "Magenta", "Cream"}
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
        logch = discord.utils.get(before.author.guild.channels, name="logs")
        timestamp = datetime.datetime.now()
        corfor = timestamp.strftime("%d %b, %Y at %H:%M")
        log = discord.Embed(description="Edited a message in {}: \n``Old:``\n{}\n``New:``\n{}\n\nUsers ID: {}".format(
            before.channel.mention, before.content, after.content, before.author.id), color=0xFFFFFF)
        log.set_author(name="{}".format(before.author), icon_url=before.author.avatar_url)
        log.set_footer(text="{}".format(corfor))
        log.set_thumbnail(url=before.author.avatar_url)
        if before.content == after.content:
            return
        await logch.send(embed=log)

        toeditsnipe[before.channel.id] = before.content
        toeditsnipeauthors[before.channel.id] = before.author
        timestamp2 = datetime.datetime.now()
        corfor = timestamp2.strftime("%d %b, %Y at %H:%M")
        toeditsnipetime[before.channel.id] = timestamp2
