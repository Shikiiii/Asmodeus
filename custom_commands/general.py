import discord
from discord.ext import commands

import random
import sys
import traceback
import asyncio
from datetime import datetime
import json

# ~MatKrulli: lazy import because I'm lazy
from common_vars import *

# Commands in this file:
# confess, nick, reply, afk, define, ping, snipe, editsnipe, reminder, remindercancel,
# reminderdm, reminderdmcancel, avatar, avatarid, userinfo, membercount,
# serverinfo, members

@bot.command()
async def confess(ctx, *, msg: str):
    await ctx.message.delete()
    chan = None
    for key, value in confessChannels.items():
        if int(key) == ctx.guild.id:
            chan = bot.get_channel(int(value))
            
    if chan is None:
        embed = discord.Embed(title="{}".format(ctx.message.author.name), description="Confessions aren't enabled for this server. Please contact an administrator to enable them.", color=0xe9f542)
        await ctx.send(embed=embed)
        return
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

@bot.command()
async def nick(ctx, user: discord.Member, *, msg: str):
    if ctx.message.author.id == user.id:
        try:
            await ctx.message.author.edit(nick="{}".format(msg))
        except:
            embed = discord.Embed(description="Their role is higher or equal to mines, can't change their nickname.",
                                  color=0xFF3639)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(description="Changed your nickname to **{}**.".format(user.mention, msg), color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="You can only change your own nickname with your current permissions.",
                              color=0xFF3639)
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
            embed = discord.Embed(description="Their role is higher or equal to mines, can't change their nickname.",
                                  color=0xFF3639)
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
            embed = discord.Embed(description="Their role is higher or equal to mines, can't change their nickname.",
                                  color=0xFF3639)
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

@bot.command(aliases=["r"])
async def reply(ctx, id: int, *, content: str):
    msg = await ctx.message.channel.fetch_message(id)
    embed = discord.Embed(description="> {}\n\n{}".format(msg.content, content))
    msg3 = await ctx.send(f"**{ctx.message.author.name}** replied to **{msg.author.name}**:", embed=embed)
    msg2 = discord.Embed(description="Ay, **{}** replied to your message in **{}**. \n[Jump to the reply.](https://discordapp.com/channels/{}/{}/{})".format(ctx.message.author.name, ctx.message.author.guild.name, ctx.message.author.guild.id, ctx.message.channel.id, msg3.id))
    await msg.author.send(embed=msg2)
    await ctx.message.delete()
    
@reply.error
async def reply_error(ctx, error):
    embed = discord.Embed(title="{}".format(ctx.message.author.name), description="Something went wrong, want to read the help page?", color=0xff0000)
    msg = await ctx.message.channel.send(embed=embed)
    await msg.add_reaction("❌")
    await msg.add_reaction("✔")
    def check(reaction, user):
        return user == ctx.message.author and reaction.message.channel.id == ctx.message.channel.id and reaction.message.id == msg.id
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
        await msg.remove_reaction("❌")
        await msg.remove_reaction("✔")
        return
    else:
        if str(reaction.emoji) == '❌':
            await msg.delete()
            await ctx.message.delete()
            return
        elif str(reaction.emoji) == '✔':
            await msg.delete()
            await ctx.message.delete()
            embed2 = discord.Embed(title="!reply [message.id] [content]", 
                                  description="**Note: The message __must be__ in the same channel where the command is ran. If you don't know how to get a message ID, check [this](https://support.discordapp.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-).**\nReplies to the given message with [content].\nAlias: ``!r``\n\nExample: ``!reply 640474593605189642 not much, hbu?``", 
                                  color=0x000000)
            await ctx.send(embed=embed2)
            return
        else:
            return

@bot.command()
async def afk(ctx, *, reason: str):
    # global afklist
    #user = ctx.message.author
    #oldnick = str(user.display_name)
    #try:
    #    await user.edit(nick="[AFK] {}".format(oldnick))
    #except:
    #    embed = discord.Embed(description="Your role is higher or equal to mines, no [AFK] to your nickname.",
    #                          color=0xebf533)
    #    embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    #    await ctx.send(embed=embed)
    #if str(ctx.message.author.id) not in afklist.keys():
    #    if len(reason) == 0:
    #        reason = random.choice(["Fapping to pornhub.com", "Fuckin yo mom", "Doin something",
    #                                "Im too lazy to type what I'm afk for", "Hi"])
    #    afklist[user.id] = reason
    #    await ctx.send("{}, I set your AFK: **{}**.".format(ctx.message.author.mention, reason))
    embed = discord.Embed(title="{}".format(ctx.message.author.name), description="This command has been disabled because of a bot-breaking bug. It'll be back soon, really soon!", color=0xffff00)
    await ctx.send(embed=embed)


@afk.error
async def afk_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        #user = ctx.message.author
        #oldnick = str(user.display_name)
        #try:
        #    await user.edit(nick="[AFK] {}".format(oldnick))
        #except:
        #    embed = discord.Embed(description="Your role is higher or equal to mines, no [AFK] to your nickname.",
        #                          color=0xebf533)
        #    embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        #    await ctx.send(embed=embed)
        #if str(ctx.message.author.id) not in afklist.keys():
        #    choice_list = ["Fapping to pornhub.com", "Fuckin yo mom", "Doin something",
        #                   "Im too lazy to type what I'm afk for", "Hi"]
        #    reason = random.choice(choice_list)
        #    afklist[user.id] = reason
        #    await ctx.send("{}, I set your AFK: **{}**.".format(ctx.message.author.mention, reason))
        embed = discord.Embed(title="{}".format(ctx.message.author.name), description="This command has been disabled because of a bot-breaking bug. It'll be back soon, really soon!", color=0xffff00)
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command(aliases=["urban"])
async def define(ctx, *, term: str):
    if term == "perfection":
        await ctx.send("i didn't need to search urban for this definition, cause i can describe perfection in 1 word and that's <@571776582147112991> 🥺")
    headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "41e03ab49dmsh4d6a1ebe8db51dep1009b5jsnc4d2da773e2f"
    }
    x = term.split(' ')
    xx = "+".join(x)
    conn.request("GET", f"/define?term={xx}", headers=headers)
    try:
        res = conn.getresponse()
    except:
        embed = discord.Embed(description="No definition found.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
        return

    my_list = res.read()
    my_json = json.loads(my_list)

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

    embed = discord.Embed(title=f"Definition of {entry['word']}",
                          description=f"``Top Definition``\n{entry['definition']}\n\n ``Example``\n{entry['example']}\n\n :thumbsup: {entry['thumbs_up']} | :thumbsdown: {entry['thumbs_down']}",
                          color=0x000000)
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
async def ping(ctx):
    # print("Testing ping!")
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
        await ctx.message.channel.send(embed=embed)
        return
    else:
        embed = discord.Embed(title=f"Pong! :ping_pong:",
                              description=":heartbeat: **{}ms**".format(delta_ping),
                              color=0xff0000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        await ctx.message.channel.send(embed=embed)

@bot.command()
async def snipe(ctx):
    for key in tosnipe:
        if key == ctx.message.channel.id:
            msg = tosnipe[key]
            author = tosnipeauthors[key]
            time = tosnipetime[key]
            embed = discord.Embed(description="{}".format(str(msg)), color=0x000000, timestamp=time)
            embed.set_author(name="{}".format(author), icon_url=author.avatar_url)
            await ctx.send(embed=embed)

@bot.command()
async def editsnipe(ctx):
    for key in toeditsnipe:
        if key == ctx.message.channel.id:
            msg = toeditsnipe[key]
            author = toeditsnipeauthors[key]
            time = toeditsnipetime[key]
            embed = discord.Embed(description="{}".format(str(msg)), color=0x000000, timestamp=time)
            embed.set_author(name="{}".format(author), icon_url=author.avatar_url)
            await ctx.send(embed=embed)

@bot.command()
async def reminder(ctx, intime, *, remindmsg: str = ""):
    if ctx.message.author.id in remindersserver:
        embed = discord.Embed(
            description="You already have an ongoing reminder! If you want to make a new one, you have to remove the old one using ``!remindercancel``.",
            color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
        return
    if len(remindmsg) == 0:
        embed = discord.Embed(
            description="Fatal error. Check the ``message`` parameter and try again. Please note that __you need to give me a message to remind you with__.",
            color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
        return
    else:
        n = intime[:-1]
        time_type = intime[-1]

        try:
            number = int(n)
        except:
            embed = discord.Embed(
                description="Fatal error. Check the ``time`` parameter and try again. Please note that **this is a correct format**: 3s (3 seconds), 5m (5 minutes), 7h (7 hours), 1d (1 day). There is also a limit of 7 days.",
                color=0xFF3639)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed)
            return
        if time_type == "s":
            if number > 604800:
                embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.",
                                      color=0xFF3639)
                embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
                await ctx.send(embed=embed)
                return
            embed = discord.Embed(
                description="Alright, I'll remind you in **{}** second(s). I'll only notify you in here. To have a DMs reminder, use !remiderdm. Your reminder message is ``{}``.".format(
                    str(number), remindmsg), color=0x03fc03)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
            # embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder too.")
            remindersserver.append(ctx.message.author.id)
            await ctx.send(embed=embed)
            # await ctx.send(embed=embed2)

            await asyncio.sleep(float(number))

            if ctx.message.author.id in remindersserver:
                embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
                await ctx.send("{},".format(ctx.message.author.mention))
                await ctx.send(embed=embed)
                # try:
                #   await ctx.message.author.send(embed=embed)
                # except discord.HTTPException as exception:
                #
                remindersserver.remove(ctx.message.author.id)
                return
            else:
                return
        if time_type == "m":
            if number > 10080:
                embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.",
                                      color=0xFF3639)
                embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
                await ctx.send(embed=embed)
                return
            embed = discord.Embed(
                description="Alright, I'll remind you in **{}** minute(s). I'll only notify you in here. To have a DMs reminder, use !remiderdm. Your reminder message is ``{}``.".format(
                    str(number), remindmsg), color=0x03fc03)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
            # embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder too.")
            remindersserver.append(ctx.message.author.id)
            await ctx.send(embed=embed)
            # await ctx.send(embed=embed2)

            await asyncio.sleep(float(number) * 60)

            if ctx.message.author.id in remindersserver:
                embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
                await ctx.send("{},".format(ctx.message.author.mention))
                await ctx.send(embed=embed)
                # try:
                #   await ctx.message.author.send(embed=embed)
                # except discord.HTTPException as exception:
                #
                remindersserver.remove(ctx.message.author.id)
                return
            else:
                return
        if time_type == "h":
            if number > 168:
                embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.",
                                      color=0xFF3639)
                embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
                await ctx.send(embed=embed)
                return
            embed = discord.Embed(
                description="Alright, I'll remind you in **{}** hour(s). I'll only notify you in here. To have a DMs reminder, use !remiderdm. Your reminder message is ``{}``.".format(
                    str(number), remindmsg), color=0x03fc03)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
            # embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder too.")
            remindersserver.append(ctx.message.author.id)
            await ctx.send(embed=embed)
            # await ctx.send(embed=embed2)

            await asyncio.sleep(float(number) * 60 * 60)

            if ctx.message.author.id in remindersserver:
                embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
                await ctx.send("{},".format(ctx.message.author.mention))
                await ctx.send(embed=embed)
                # try:
                #   await ctx.message.author.send(embed=embed)
                # except discord.HTTPException as exception:
                #
                remindersserver.remove(ctx.message.author.id)
                return
            else:
                return
        if time_type == "d":
            if number > 7:
                embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.",
                                      color=0xFF3639)
                embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
                await ctx.send(embed=embed)
                return
            embed = discord.Embed(
                description="Alright, I'll remind you in **{}** day(s). I'll only notify you in here. To have a DMs reminder, use !remiderdm. Your reminder message is ``{}``.".format(
                    str(number), remindmsg), color=0x03fc03)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
            # embed2 = discord.Embed(description="Note: Enable your DMs in this server so I can DM you with the reminder too.")
            remindersserver.append(ctx.message.author.id)
            await ctx.send(embed=embed)
            # await ctx.send(embed=embed2)

            await asyncio.sleep(float(number) * 60 * 60 * 24)

            if ctx.message.author.id in remindersserver:
                embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
                await ctx.send("{},".format(ctx.message.author.mention))
                await ctx.send(embed=embed)
                # try:
                #   await ctx.message.author.send(embed=embed)
                # except discord.HTTPException as exception:
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
        embed = discord.Embed(
            description="You're missing required arguments. Here's an example of how to use this command: \n``!reminder 3h going to appreciate this godly command``",
            color=0xFF3639)
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
        embed = discord.Embed(description="You don't have a reminder to cancel. Set one by using ``!reminder``.",
                              color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)


@bot.command()
async def reminderdm(ctx, intime, *, remindmsg: str = ""):
    if ctx.message.author.id in remindersdm:
        embed = discord.Embed(
            description="You already have an ongoing reminder! If you want to make a new one, you have to remove the old one using ``!remindercancel``.",
            color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
        return
    if len(remindmsg) == 0:
        embed = discord.Embed(
            description="Fatal error. Check the ``message`` parameter and try again. Please note that __you need to give me a message to remind you with__.",
            color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
        return
    else:
        n = intime[:-1]
        time_type = intime[-1]

        try:
            number = int(n)
        except:
            embed = discord.Embed(
                description="Fatal error. Check the ``time`` parameter and try again. Please note that **this is a correct format**: 3s (3 seconds), 5m (5 minutes), 7h (7 hours), 1d (1 day). There is also a limit of 7 days.",
                color=0xFF3639)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed)
            return
        if time_type == "s":
            if number > 604800:
                embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.",
                                      color=0xFF3639)
                embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
                await ctx.send(embed=embed)
                return
            embed = discord.Embed(
                description="Alright, I'll remind you in **{}** second(s). I'll notify you in DMs. Your reminder message is ``{}``.".format(
                    str(number), remindmsg), color=0x03fc03)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
            embed2 = discord.Embed(
                description="Note: Enable your DMs in this server so I can DM you with the reminder.")
            remindersdm.append(ctx.message.author.id)
            await ctx.send(embed=embed)
            await ctx.send(embed=embed2)

            await asyncio.sleep(float(number))

            if ctx.message.author.id in remindersdm:
                embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
                # await ctx.send("{},".format(ctx.message.author.mention))
                await ctx.message.author.send(embed=embed)
                try:
                    await ctx.message.author.send(embed=embed)
                except discord.HTTPException:
                    await ctx.send("{}, I couldn't DM you with your reminder, so I'll post it here.".format(
                        ctx.message.author.mention))
                    await ctx.send(embed=embed)
                remindersdm.remove(ctx.message.author.id)
                return
            else:
                return
        if time_type == "m":
            if number > 10080:
                embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.",
                                      color=0xFF3639)
                embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
                await ctx.send(embed=embed)
                return
            embed = discord.Embed(
                description="Alright, I'll remind you in **{}** minute(s). I'll notify you in DMs. Your reminder message is ``{}``.".format(
                    str(number), remindmsg), color=0x03fc03)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
            embed2 = discord.Embed(
                description="Note: Enable your DMs in this server so I can DM you with the reminder.")
            remindersdm.append(ctx.message.author.id)
            await ctx.send(embed=embed)
            await ctx.send(embed=embed2)

            await asyncio.sleep(float(number) * 60)

            if ctx.message.author.id in remindersdm:
                embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
                # await ctx.send("{},".format(ctx.message.author.mention))
                await ctx.message.author.send(embed=embed)
                try:
                    await ctx.message.author.send(embed=embed)
                except discord.HTTPException:
                    await ctx.send("{}, I couldn't DM you with your reminder, so I'll post it here.".format(
                        ctx.message.author.mention))
                    await ctx.send(embed=embed)
                remindersdm.remove(ctx.message.author.id)
                return
            else:
                return
        if time_type == "h":
            if number > 168:
                embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.",
                                      color=0xFF3639)
                embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
                await ctx.send(embed=embed)
                return
            embed = discord.Embed(
                description="Alright, I'll remind you in **{}** hour(s). I'll notify you in DMs. Your reminder message is ``{}``.".format(
                    str(number), remindmsg), color=0x03fc03)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
            embed2 = discord.Embed(
                description="Note: Enable your DMs in this server so I can DM you with the reminder.")
            remindersdm.append(ctx.message.author.id)
            await ctx.send(embed=embed)
            await ctx.send(embed=embed2)

            await asyncio.sleep(float(number) * 60 * 60)

            if ctx.message.author.id in remindersdm:
                embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
                # await ctx.send("{},".format(ctx.message.author.mention))
                await ctx.message.author.send(embed=embed)
                try:
                    await ctx.message.author.send(embed=embed)
                except discord.HTTPException:
                    await ctx.send("{}, I couldn't DM you with your reminder, so I'll post it here.".format(
                        ctx.message.author.mention))
                    await ctx.send(embed=embed)
                remindersdm.remove(ctx.message.author.id)
                return
            else:
                return
        if time_type == "d":
            if number > 7:
                embed = discord.Embed(description="Whoa there buddy! We have a limit of 7 days per reminder.",
                                      color=0xFF3639)
                embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
                embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
                await ctx.send(embed=embed)
                return
            embed = discord.Embed(
                description="Alright, I'll remind you in **{}** day(s). I'll notify you in DMs. Your reminder message is ``{}``.".format(
                    str(number), remindmsg), color=0x03fc03)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
            embed2 = discord.Embed(
                description="Note: Enable your DMs in this server so I can DM you with the reminder.")
            remindersdm.append(ctx.message.author.id)
            await ctx.send(embed=embed)
            await ctx.send(embed=embed2)

            await asyncio.sleep(float(number) * 60 * 60 * 24)

            if ctx.message.author.id in remindersdm:
                embed = discord.Embed(description="**REMINDER:**\n\n{}".format(remindmsg), color=0xffffff)
                # await ctx.send("{},".format(ctx.message.author.mention))
                await ctx.message.author.send(embed=embed)
                try:
                    await ctx.message.author.send(embed=embed)
                except discord.HTTPException:
                    await ctx.send("{}, I couldn't DM you with your reminder, so I'll post it here.".format(
                        ctx.message.author.mention))
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
        embed = discord.Embed(
            description="You're missing required arguments. Here's an example of how to use this command: \n``!reminder 3h going to appreciate this godly command``",
            color=0xFF3639)
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
        embed = discord.Embed(description="You don't have a DM reminder to cancel. Set one by using ``!reminderdm``.",
                              color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)


# - Avatar commands:
@bot.command(aliases=['av'])
async def avatar(ctx, user: discord.Member):
    embed = discord.Embed(title="Avatar of {}".format(user), color=0x000000)
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)


@avatar.error
async def avatar_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(title="Member not found, ping a user to get their avatar.", color=0xFF3639)
        # embed.set_image(url=bot.user.avatar_url)
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


@bot.command(aliases=['avid'])
async def avatarid(ctx, user_id: int):
    try:
        user = await bot.fetch_user(user_id)
    except discord.HTTPException:
        embed = discord.Embed(description="I dunno man, it doesn't look like there's a member like this.",
                              color=0xFF3639)
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
        embed = discord.Embed(
            description="I couldn't get the avatar of.. no one? Try giving me an ID so I can get an avatar..",
            color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)


# - Userinfo Command:
@bot.command(aliases=["uf", "whois"])
async def userinfo(ctx, user: discord.Member):
    time = user.joined_at

    corfor1 = time.strftime("%d %b, %Y at %H:%M")

    time2 = user.created_at

    corfor2 = time2.strftime("%d %b, %Y at %H:%M")

    def sort_by_joined_at(member: discord.Member):
        return member.joined_at

    memberslist = ctx.guild.members
    memberslist.sort(key=sort_by_joined_at)
    joinpos = memberslist.index(user)

    if user.premium_since is None:
        boosting = "Nope"
    else:
        boosting = "Yes"

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
        embed = discord.Embed(description="Member not found, check the member you gave me and try again.",
                              color=0xFF3639)
        # embed.set_image(url=ctx.message.author.guild.icon_url)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingRequiredArgument):
        time = ctx.message.author.joined_at

        corfor1 = time.strftime("%d %b, %Y at %H:%M")

        time2 = ctx.message.author.created_at

        corfor2 = time2.strftime("%d %b, %Y at %H:%M")

        def sort_by_joined_at(member: discord.Member):
            return member.joined_at

        memberslist = ctx.guild.members
        memberslist.sort(key=sort_by_joined_at)
        joinpos = memberslist.index(ctx.message.author)

        if ctx.message.author.premium_since is None:
            boosting = "Nope"
        else:
            boosting = "Yes"

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

@bot.command()
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
    # fa = " "
    if ctx.message.author.guild.mfa_level == 0:
        fa = "No"
    if ctx.message.author.guild.mfa_level == 1:
        fa = "Yes"
    # ver = " "

    embed = discord.Embed(title="Info of {}".format(ctx.message.author.guild.name),
                          description="Owned by {}".format(ctx.message.author.guild.owner), color=0x000000)
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
    # embed2 = discord.Embed(color=0x000000)
    embed.add_field(name="Requires 2FA", value="{}".format(fa), inline=True)
    embed.add_field(name="Boosters", value="{}".format(ctx.message.author.guild.premium_subscription_count),
                    inline=True)
    embed.add_field(name="Boost level", value="{}".format(ctx.message.author.guild.premium_tier), inline=True)
    if str(ctx.message.author.guild.verification_level) == "none":
        ver = "None"
        embed.add_field(name="Verification level", value="{}".format(ver))
    # print(ver)
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
    
@bot.command()
async def members(ctx, *, rolee: str):
    role = await parse_roles(ctx, rolee)
    members = []
    for member in ctx.message.author.guild.members:
        if role in member.roles:
            members.append(member.mention)
    embed = discord.Embed(title="All members that have the {} role:".format(str(role)), description="\n".join(members),
                          color=0x000000)
    embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url=bot.user.avatar_url)
    if role is None:
        embed = discord.Embed(description="I couldn't find this role.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
        return
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
