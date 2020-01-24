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

from datetime import datetime

@bot.command()
async def quicktestpaid(ctx):
    embed = discord.Embed(title="25$ Paid Promotion", description="**Welcome to Bearded Vultures!**\n\nWe’re a __**new**__ company that does numerous things to support our customers to the best of our ability. From gaming communities to discord servers, our company can create a __**professional**__ build that will be more than satisfactory to you! Read more about our company below; \n\n**:snowflake: ARK: Survival Evolved (TAMES) :snowflake: \n:snowflake: Discord Servers :snowflake: \n:snowflake: Minecraft Builds :snowflake: \n\n:scream: Reaction Roles \n:scream: Self Advertising \n:scream: Events / Giveaways \n\n:trophy: Creator Contests \n:trophy: Builder Contests \n\n:gift: The first 3 services are __FREE__ to our customers, per customer. :gift: **\n\n*:boom:Lᴏᴏᴋɪɴɢ ғᴏʀ **ʙᴜɪʟᴅᴇʀs** ᴀɴᴅ **ᴅɪsᴄᴏʀᴅ ᴄʀᴇᴀᴛᴏʀs***\n:moneybag: __**Earn honest cash with us!**__ :moneybag: \n**OUR employees get 90-95% of all profits from their builds and creations!** \n\n:paperclip: https://discord.gg/6Rj8muS\n:paperclip: https://discord.gg/JqubD94", color=0x33F6FF, timestamp=datetime.utcnow())
    embed.set_author(name="Ａｓｍｏｄｅｕｓ❄🎄 Paid Promotion", url="https://discord.gg/h945y6T")
    await ctx.send("Hey! Welcome to **{}**.\nCheck out our cheap promotions! https://discord.gg/vrjvX5u".format(ctx.guild.name), embed=embed)

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
    storageCF = storage.get_channel(647444887184080906)
    storageM = storage.get_channel(648898928221093908)
    storageD = storage.get_channel(648951518602592277)
    storageE = storage.get_channel(648951532905037834)
    storageMM = storage.get_channel(648951574319726592)
    storageP= storage.get_channel(648951548809838628)
    storageUP = storage.get_channel(646432281287852057)
    storageMC = storage.get_channel(651763336425373707)
    
    # Here, we get the prefixes, so we don't have to scan the channel everytime a command is ran. - Shiki
    async for message in storageMC.history():
        x = message.content.split("|")
        userID = x[0]
        ign = x[1]
        mcIGNs[int(userID)] = ign
        mcIGNsToDelete[int(userID)] = message.id
    async for message in storageUP.history():
        x = message.content.split("|")
        userID = x[0]
        marriedTo = x[1]
        balance = x[2]
        balances[int(userID)] = int(balance)
        balancesToDelete[int(userID)] = message.id
        married[int(userID)] = int(marriedTo)
        marriedToDelete[int(userID)] = message.id
    async for message in storageP.history():
        x = message.content.split("|")
        guildID = x[0]
        chan = x[1]
        punishLogs[guildID] = chan
        punishLogsToDelete[guildID] = message.id
    async for message in storageMM.history():
        x = message.content.split("|")
        guildID = x[0]
        chan = x[1]
        memberLogs[guildID] = chan
        memberLogsToDelete[guildID] = message.id
    async for message in storageE.history():
        x = message.content.split("|")
        guildID = x[0]
        chan = x[1]
        editLogs[guildID] = chan
        editLogsToDelete[guildID] = message.id
    async for message in storageD.history():
        x = message.content.split("|")
        guildID = x[0]
        chan = x[1]
        deleteLogs[guildID] = chan
        deleteLogsToDelete[guildID] = message.id
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
    async for message in storageCF.history():
        x = message.content.split("|")
        guildID = x[0]
        chan = x[1]
        confessChannels[str(guildID)] = str(chan)
        confessChannelsToDelete[guildID] = message.id
    async for message in storageM.history():
        x = message.content.split("|")
        guildID = x[0]
        role = x[1]
        serverMuted[str(guildID)] = str(role)
        serverMutedToDelete[guildID] = message.id
        
    #c = bot.get_channel(642482823445479424)
    #await vc.connect()
    #faith = bot.get_user(571776582147112991)
    #shiki = bot.get_user(237938976999079948)
    #stimessages = 0
    #while True:
        #global msgsCounterrr
        #msgsCounterrr = 0
        #await asyncio.sleep(3600)
        #await faith.send("ilym 💕💖💞💖💕💖💞💕💖💞💕💖💖💕💕💖💞💞💞💕")
        #await shiki.send("sent a dm to faith {}".format(stimessages))
        #stimessages += 1
        

@bot.event
async def on_member_update(before, after):
    if before.guild.id == 660616924643721248:
        role = discord.utils.get(after.guild.roles, name="Snowstorms ❄️")
        if role not in before.roles and role in after.roles:
            embed = discord.Embed(description="just boosted the server! <a:Hearts:653291632535404545>\n\nCheck out your cool perks with ``!tag boosting``. Ily", color=0xF224E5, timestamp=datetime.utcnow())
            embed.set_author(name=after.name, icon_url=after.avatar_url)
            embed.set_thumbnail(url=after.guild.icon_url)
            chan = bot.get_channel(642482771511476234)
            await chan.send("{}".format(after.mention), embed=embed)

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
                    print("Checking message..")
                    if len(reaction.message.attachments) > 0:
                        print("Detected attachment(s). Checking if it's an image..")
                        if reaction.message.attachments[0].height is not None:
                            print("It's an image! Let's put the first one with set_image..")
                            embed.set_image(url=reaction.message.attachments[0].url)
                            print("Success! Ready to go!")
                    await chan.send(embed=embed)
                    embed2 = discord.Embed(description=":crown: {}'s message has been added to the starboard!".format(reaction.message.author.name), color=0xffff00)
                    await reaction.message.channel.send(embed=embed2)
                    starboardMessages[reaction.message.channel.id] = reaction.message.id
        
@bot.event
async def on_member_join(member):
    if member.guild.id == 660616924643721248:
        rol = discord.utils.get(member.guild.roles, name="Members 💖")
        await member.add_roles(rol)
        mbrcnt = bot.get_channel(660637774495481856)
        channel = bot.get_channel(660616924643721254)
        await mbrcnt.edit(name="🍓 {} +1".format(member.guild.member_count))
        embed = discord.Embed(
            description="Welcome to **[Ａｓｍｏｄｅｕｓ](https://discord.gg/Qqzy2ds)**! You're the **{}th** member. \n\n Make sure to read: <#660634194854150144>".format(
                member.guild.member_count), color=0x000000, timestamp=datetime.utcnow())
        welcomer = member.guild.get_role(665509280140754954)
        #await welcomer.edit(mentionable=True)
        embed.set_author(name="{}".format(member,), icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.guild.icon_url)
        await channel.send("{} | {} <a:Cheers:660932691075530763>".format(member.mention, welcomer.mention), embed=embed)
        #await welcomer.edit(mentionable=False)
        loggg = discord.utils.get(member.guild.channels, name="join-leave-logs")
        await loggg.send(f"{member} ({member.mention}, {member.id}) joined.")
        #anouncements = bot.get_channel(660635938925576203)
        #msg = await anouncements.send("Hey {}, check out our **10$ Nitro Giveaway**!".format(member.mention))
        #await asyncio.sleep(5)
        #await msg.delete()
        #try:
        #    embed = discord.Embed(description="Our server recently got deleted at 1K, help us get back at 1K by inviting 3 people and joining the **Nitro Giveaway**: <#660635938925576203>")
            #await member.send("Hey! Welcome to **Ａｓｍｏｄｅｕｓ❄🎄**. Feel free to chat with us in <#660616924643721254>.", embed=embed)
        #except:
         #   return
    else:
        #embed = discord.Embed(title="25$ Paid Promotion", description="**Welcome to Bearded Vultures!**\n\nWe’re a __**new**__ company that does numerous things to support our customers to the best of our ability. From gaming communities to discord servers, our company can create a __**professional**__ build that will be more than satisfactory to you! Read more about our company below; \n\n**:snowflake: ARK: Survival Evolved (TAMES) :snowflake: \n:snowflake: Discord Servers :snowflake: \n:snowflake: Minecraft Builds :snowflake: \n\n:scream: Reaction Roles \n:scream: Self Advertising \n:scream: Events / Giveaways \n\n:trophy: Creator Contests \n:trophy: Builder Contests \n\n:gift: The first 3 services are __FREE__ to our customers, per customer. :gift: **\n\n*:boom:Lᴏᴏᴋɪɴɢ ғᴏʀ **ʙᴜɪʟᴅᴇʀs** ᴀɴᴅ **ᴅɪsᴄᴏʀᴅ ᴄʀᴇᴀᴛᴏʀs***\n:moneybag: __**Earn honest cash with us!**__ :moneybag: \n**OUR employees get 90-95% of all profits from their builds and creations!** \n\n:paperclip: https://discord.gg/6Rj8muS\n:paperclip: https://discord.gg/JqubD94", color=0x33F6FF, timestamp=datetime.utcnow())
        #embed.set_author(name="Ａｓｍｏｄｅｕｓ❄🎄 Paid Promotion", url="https://discord.gg/h945y6T")
        await member.send("Hey! Welcome to **{}**.\Our server recently got deleted at 1K, help us get back at 1K by inviting 3 people and joining the **Nitro Giveaway**! https://discord.gg/Qqzy2ds".format(member.guild.name), embed=embed)

    chan = None
    for key, value in memberLogs.items():
        if int(key) == member.guild.id:
            chan = bot.get_channel(int(value))
            embed = discord.Embed(description="joined the server.", timestamp=datetime.utcnow(), color=0x05ff44)
            embed.set_author(name="{}".format(member), icon_url=member.avatar_url)
            await chan.send(embed=embed)
    

@bot.event
async def on_member_remove(member):
    if member.guild.id == 660616924643721248:
        mbrcnt = bot.get_channel(660637774495481856)
        await mbrcnt.edit(name="🍓 {} -1".format(member.guild.member_count))
        loggg = discord.utils.get(member.guild.channels, name="join-leave-logs")
        await loggg.send(f"{member} ({member.mention}, {member.id}) left.")
    chan = None
    for key, value in memberLogs.items():
        if int(key) == member.guild.id:
            chan = bot.get_channel(int(value))
            embed = discord.Embed(description="left the server.", timestamp=datetime.utcnow(), color=0xff1e05)
            embed.set_author(name="{}".format(member), icon_url=member.avatar_url)
            await chan.send(embed=embed)

@bot.event
async def on_message(message: Message):
    if message.channel.id == 660637460622999582:
        if message.author.bot == True:
            return
        await message.channel.set_permissions(message.author, send_messages=False)
        intros = message.channel
        chan = bot.get_channel(670392877800620033)
        print(chan)
        msg = None
        async for message in chan.history(limit=1):
            msg = await intros.fetch_message(int(message.content))
        await msg.delete()
        embed = discord.Embed(title="__Reminder:__", description="Before you post your introduction, keep in mind:\n - You are only allowed to post **1 message** in this channel. Make sure it covers your whole introduction. After you post a message, the channel will become read-only for you.\n - Deleting your introduction **will not let you type again**. Please contact <@660658512052879401> if you want to edit your introduction.\n - Useless messages in this channel will be deleted.", color=0x000000, timestamp=datetime.utcnow()) 
        msg2 = await intros.send(embed=embed)
        await chan.send("{}".format(msg2.id))
    elif message.channel.id == 662797497143656509 and message.author.bot == False:
        await message.channel.send("{} just posted their ad because they are boosting our server. Please boost our server too! For all the stuff you get in return, do ``!tag boosting``. Ly".format(message.author.mention))
    elif bot.user.mentioned_in(message):
        if "ping" in message.content:
            await message.channel.send("{} pong".format(message.author.mention))
        elif "pong" in message.content:
            await message.channel.send("{} ping".format(message.author.mention))
        else:
            splitted = message.content.split(" ")
            if len(splitted) > 1:
                return
            prefix = None
            for key, value in serverPrefixes.items():
                if int(key) == message.guild.id:
                    prefix = str(value)
            if prefix is None:
                prefix = "! (Default)"
            sb = None
            for key, value in starboardChannels.items():
                if int(key) == message.guild.id:
                    sbb = bot.get_channel(int(value))
                    sb = sbb.mention
            if sb is None:
                sb = "Not enabled, use the ``scoreboard`` command to enable it."
            confess = None
            for key, value in confessChannels.items():
                if int(key) == message.guild.id:
                    confesss = bot.get_channel(int(value))
                    confess = confesss.mention
            if confess is None:
                confess = "Not enabled, use the ``setconfess`` command to enable it."
            muted = None
            for key, value in serverMuted.items():
                if int(key) == message.guild.id:
                    mutedd = message.guild.get_role(int(value))
                    muted = mutedd.mention
            if muted is None:
                muted = "Not set, use the ``setmuted`` command to set it. Otherwise ``mute`` wouldn't work."
            editLogsS = None
            deleteLogsS = None
            memberLogsS = None
            punishLogsS = None
            for key, value in deleteLogs.items():
                if int(key) == message.guild.id:
                    deleteLogss = bot.get_channel(int(value))
                    deleteLogsS = deleteLogss.mention
            if deleteLogs is None:
                deleteLogsS = ":x:"
            for key, value in editLogs.items():
                if int(key) == message.guild.id:
                    editLogss = bot.get_channel(int(value))
                    editLogsS = editLogss.mention
            if editLogs is None:
                editLogsS = ":x:"
            for key, value in memberLogs.items():
                if int(key) == message.guild.id:
                    memberLogss = bot.get_channel(int(value))
                    memberLogsS = memberLogss.mention
            if memberLogs is None:
                memberLogsS = ":x:"
            for key, value in punishLogs.items():
                if int(key) == message.guild.id:
                    punishLogss = bot.get_channel(int(value))
                    punishLogsS = punishLogss.mention
            if punishLogs is None:
                punishLogsS = ":x:"
            embed=discord.Embed(description="Haay! Here to help you.\n**Server prefix:** ``{}``\n**Starboard channel:** {}\n**Confess channel:** {}\n**Muted role:** {}\n\n**Logs:**\n``Delete:`` {}\n``Edit:`` {}\n``Member:`` {}\n``Punish:`` {}".format(str(prefix), sb, confess, muted, deleteLogsS, editLogsS, memberLogsS, punishLogsS), color=0x000000, timestamp=datetime.utcnow()) 
            embed.set_author(name="{}".format(bot.user.name), icon_url=bot.user.avatar_url)
            embed.set_thumbnail(url=message.guild.icon_url)
            await message.channel.send(embed=embed)
    #if ((message.channel.id == 642482771511476234) or (message.channel.id == 629056727186407445)) and message.author.bot and message.author.id != 640827656660582400:
    #    await message.delete()
    #    return
    if message.channel.id == 642482779111555072 or message.channel.id == 642482779925250067 or message.channel.id == 642482780797665290 or message.channel.id == 642482781812686866:
        if len(message.attachments) == 0:   
            if message.author.id != 237938976999079948:
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
    if message.channel.id == 660636770777694243:
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
                               description="We're so glad to have you here! By staying in this server, you agree to our __rules__. We have over 100 bots, channels and roles to play around with! Make sure to stick around for more cool stuff. We are a friendly community, we accept everyone regardless of your gender, age, race or etc.",
                               color=0xC5FCFC)
        embed2 = discord.Embed(color=0xC5FCFC)
        embed2.set_image(url="https://cdn.discordapp.com/attachments/635581513228091462/637970310095831061/Untitled-1.png")
        await message.channel.send(embed=embed2)
        await message.channel.send(embed=embed1)
    elif (message.content == "!rules" and (
            message.author.id == 237938976999079948 or message.author.id == 495680416422821888)):
        embed1 = discord.Embed(title="**༚ ✧˳⁺ __Server rules__ ⁺˳✧ ༚**",
                               description="``1`` - **Make sure to follow the [Discord TOS](https://discordapp.com/terms) and the [Community Guidelines](https://discordapp.com/guidelines)**. \n\n``2`` - This is a **friendly community**. Any toxicity, hate or racism is banned.\n\n``3`` - Hard 'R' is banned unless you're black.\n\n``4`` - Playing a mf hacker is a really, really dumb move. Linking someone's personal information (doxing them) would get you instantly banned.\n\n``5`` - Advertising is completely banned (including DM/PM advertising). If someone's DMing you ads of any sort, let staff know, they'll handle it.\n\n``6`` - Respect all members and staff, their decision(s) and wishes.\n\nOther than that, please **use common sense** while you are typing in any of the text channels. This means no spamming, raiding, insulting, etc.\n\nFor any problems: <@237938976999079948> | If you've found any loopholes in the rules, DM <@237938976999079948>.",
                               timestamp=datetime.utcnow(),
                               color=0xC5FCFC)
        embed1.set_footer(text="Last update:")
        #embed2 = discord.Embed(color=0xC5FCFC)
        #embed2.set_image(url="https://media.giphy.com/media/kD0G3PwfsUhUzQu3QQ/giphy.gif")
        #embed3 = discord.Embed(title="**༚ ✧˳⁺ __Voice Chat rules__ ⁺˳✧ ༚**",
        #                       description="__``1``__ • Don't ear rape other people with music or with your mic. \r\n\r\n __``2``__ • Do not spam music, let other people play their song. \r\n\r\n __``3``__ • Do not stop the music if there are still others in the voice channel. \r\n\r\n __``4``__ • Do not mic spam, yell or disturb others. \r\n\r\n __``5``__ • Do NOT be toxic or be racist.",
         #                      color=0xC5FCFC)
        #await message.channel.send(embed=embed2)
        #await message.channel.send(embed=embed3)
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
    #elif "uwu" in message.content or "UwU" in message.content or "uWu" in message.content or "Uwu" in message.content or "uwU" in message.content:
     #   await message.delete()
    elif message.content == "shiki":
        await message.channel.send("dm <@237938976999079948> with thigh pics for free admin aha x")
    elif message.content == "no u" and message.author.bot == False:
        await message.channel.send("no u")
    elif message.content == "alex":
        await message.channel.send("biggest retard")
    elif message.content == "kam" or message.content == "kamera":
        await message.channel.send("dm <@567799351368482826> for a Daddy :wink:")
    elif message.content == "madz":
        await message.channel.send("shrek is love, shrek is life")
    elif message.content == "meg":
        await message.channel.send("wooden hoe *with loyalty 1")
    elif message.content == "david":
        await message.channel.send("looking at maps")
    elif message.content == "sora":
        await message.channel.send("gift me money")

    await bot.process_commands(message)

@bot.event
async def on_message_delete(message: Message):
    if message.author.bot == False:
        logch = None
        for key, value in deleteLogs.items():
            if int(key) == message.author.guild.id:
                logch = bot.get_channel(int(value))
        if logch is None:
            return
        log = discord.Embed(
            description="Deleted a message in {}: \n{}\n\nUsers ID: {}".format(message.channel.mention, message.content,
                                                                               message.author.id), color=0xFFFFFF, timestamp=datetime.utcnow())
        log.set_author(name="{}".format(message.author), icon_url=message.author.avatar_url)
        log.set_thumbnail(url=message.author.avatar_url)
        if message.author.id != 237938976999079948:
            await logch.send(embed=log)

    if message.author.bot == False:
        if message.content.startswith("!confess"):
            print("Confess was ignored from !snipe.")
        elif "uwu" in message.content or "UwU" in message.content or "uWu" in message.content or "Uwu" in message.content or "uwU" in message.content:
            return
        else:
            tosnipe[message.channel.id] = message.content
            tosnipeauthors[message.channel.id] = message.author
            timestamp=datetime.utcnow()
            tosnipetime[message.channel.id] = timestamp


@bot.event
async def on_message_edit(before, after):
    if before.author.bot == False:
        logch = None
        for key, value in editLogs.items():
            if int(key) == before.author.guild.id:
                logch = bot.get_channel(int(value))
        if logch is None:
            return
        log = discord.Embed(description="Edited a message in {}: \n``Old:``\n{}\n``New:``\n{}\n\nUsers ID: {}".format(
            before.channel.mention, before.content, after.content, before.author.id), color=0xFFFFFF, timestamp=datetime.utcnow())
        log.set_author(name="{}".format(before.author), icon_url=before.author.avatar_url)
        log.set_thumbnail(url=before.author.avatar_url)
        if before.content == after.content:
            return
        await logch.send(embed=log)

        toeditsnipe[before.channel.id] = before.content
        toeditsnipeauthors[before.channel.id] = before.author
        timestamp=datetime.utcnow()
        toeditsnipetime[before.channel.id] = timestamp
