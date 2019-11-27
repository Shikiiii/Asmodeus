import discord
from discord.ext import commands

import random
import sys
import traceback
import asyncio
import datetime
import json

from datetime import datetime

from common_vars import *

# Commands in this file:
# MCM, servers, server, say, verify, status

#@bot.command()
#async def update(ctx):
#    embed = discord.Embed(title="0.7 has been pushed to the repository.", description="")

@bot.command(name="update0.7")
@commands.is_owner()
async def update(ctx):
    embed = discord.Embed(title="0.7 has been deployed to the repository.", description="**__New Stuff:__**\n\n> - Added 2 new reaction commands: ``poke`` and ``facepalm``.\n> - Added a nick command to change yours or another member's nickname, depending on your permissions.\n> - Probably the most requested feature now, added a way to change the prefix using the ``prefix`` command. Thanks for the patience OtakuStream and Liquid Rose!\n> - Added a starboard! To set the channel where the starboards go, use the ``starboard`` command. A message requires 5 :star: reactions to be added to the starboard. This will be changeable in the future.\n> - Added confessions! All secrets are anonymous, even to the bot developer. For you admins, set the confessions channel using ``setconfess``, and for you users, confess something by doing ``confess [message]``.\n> - Added a way to choose your own mute role! Now ``mute`` won't work unless you set a role first using ``setmuted``.\n> - Added logs! There are 4 type of logs right now: ``delete``, ``edit``, ``member`` and ``punish``. To set them up, use ``cmdhelp logs``.\n> - Now when you mention the bot, it'll give you your prefix, starboard channel, confess channel, muted role and logs' channels. Thank me later.\n> - And most importantly, finally splitted the bot into small files of groups so the bot can be updated faster. This will help new updates come out sooner!\n\n**__Fixes:__**\n> - Ship can also take 1 user as an argument now, the other user will be the message author. And fixed the empty strings bug.\n> - Before, typing 'no u' would make the bot spam it, till the end of the world, this has been fixed.\n> - Timestamps now work as normal timestamps.\n\n**__Removed:__**\n> - ``unban`` and ``unmute`` no longer take a [reason] argument. It was useless anyway.\n> - ``afk`` has been disabled because of a bot-breaking bug. It'll be back soon, but upgraded!\n\n[Invite Me To Your Server](https://discordapp.com/oauth2/authorize?client_id=640827656660582400&scope=bot&permissions=2097151191) | [Support Server](https://discord.gg/h945y6T) | Developer: ``$ ｈｉｋｉ#0081``", timestamp=datetime.utcnow(), color=0x000000)
    embed.set_author(name="{}".format(bot.user.name), icon_url=bot.user.avatar_url)
    embed.set_footer(text="Please report any bug found in the support server. Thanks! Updated at:")
    for guild in bot.guilds:
        if guild.id == 642429293330300971:
            chan1 = bot.get_channel(642482765396312074)
            chan2 = bot.get_channel(649328015687548938)
            await chan1.send(embed=embed)
            await chan2.send(embed=embed)
            print("Sent a message to {}!".format(guild.name))
        elif guild.id == 634860194207236117:
            chan = bot.get_channel(635206523793965062)
            await chan.send(embed=embed)
            print("Sent a message to {}!".format(guild.name))
        elif guild.id == 385378814584422413:
            chan = bot.get_channel(646007396828708864)
            chan = bot.get_channel(610621692615721005)
            await chan.send(embed=embed)
            await chan.send(embed=embed)
            print("Sent a message to {}!".format(guild.name))
        else:
            for TextChannel in guild.text_channels:
                try:
                    await TextChannel.send(embed=embed)
                    print("Sent a message to {}!".format(guild.name))
                    break
                except:
                    continue

@bot.command()
@commands.is_owner()
async def dmAllServer(ctx, servv: int, *, msg: str):
    serv = bot.get_guild(servv)
    dmed = 0
    embed = discord.Embed(description="DMs pending••• :yellow_heart: $ **{}**".format(dmed), color=0x000000)
    msgg = await ctx.send(embed=embed)
    for member in serv.members:
        try:
            await member.send("{}".format(msg))
            dmed += 1
            embedd = discord.Embed(description="DMs pending••• :yellow_heart: $ **{}**".format(dmed), color=0x000000)
            await msgg.edit(embed=embedd)
        except:
            continue
    await msgg.edit(content="Finished DMing all members.")

@bot.command()
@commands.is_owner()
async def mCM(ctx):
    if ctx.message.author.id == 237938976999079948:
        role_names = ["Light Red", "Light Orange", "Light Purple", "Light Yellow", "Light Cyan", "Light Blue",
                      "Light Green", "Light Pink", "Dark Red", "Dark Blue", "Dark Purple", "Dark Pink",
                      "Crimson", "Black", "Gray", "Indigo", "Lavender", "Violet", "White", "Magenta", "Cream"]
        for item in role_names:
            role = discord.utils.get(ctx.message.guild.roles, name=item)
            await role.edit(mentionable = not role.mentionable)

@bot.command()
@commands.is_owner()
async def servers(ctx):
    serverss = bot.guilds
    strings = []
    for guild in serverss:
        strings.append("{}".format(guild.name))
    readme = "/n".join(strings)
    await ctx.send("```{}```".format(readme))

@bot.command()
@commands.is_owner()
async def server(ctx, *, serverr: str):
    hi = True
    server = await guildConvert(serverr)
    try:
        if server is None:
            await ctx.send("not found")
        else:
            for channel in server.channels:
                while hi:
                    invite = await channel.create_invite()
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

@bot.command()
@commands.is_owner()
async def say(ctx, chan: discord.TextChannel, *, msg: str = ""):
    # channels = ctx.message.channel_mentions
    # if len(channels) > 0:
    # for channel in channels:
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

@bot.command(aliases=["v"])
@commands.is_owner()
async def verify(ctx, user: discord.Member, gender: str = " "):
    verm = discord.utils.get(ctx.message.author.guild.roles, name="Verified Male")
    verf = discord.utils.get(ctx.message.author.guild.roles, name="Verified Female")
    verchan = discord.utils.get(ctx.message.author.guild.channels, name="x【verification】x")

    failtover = discord.Embed(
        description="Try verifying this member again, but specify either **f** / **female** or **m** / **male**. \nExample: ``!verify @cooluser m``",
        color=0xFF3639)
    failtover.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    failtover.set_footer(text="Error raised on: {}".format(ctx.message.content))

    alrver = discord.Embed(description="This user is already verified.", color=0xFF3639)
    alrver.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    alrver.set_footer(text="Error raised on: {}".format(ctx.message.content))
    if verm in user.roles or verf in user.roles:
        await ctx.message.delete()
        msg = await ctx.send(embed=alrver)
        await asyncio.sleep(float(10))
        await msg.delete()
        return
    if gender == "m" or gender == "male":
        # verr = " ".join(m)
        ver = discord.Embed(description="༚ ✧˳⁺ {} has received the **Verified Male** role. ⁺˳✧ ༚ ".format(user.mention),
                            color=0xFF93F0)
        ver.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        ver.set_thumbnail(url=user.avatar_url)
        await user.add_roles(verm)
        await ctx.message.delete()
        await ctx.send(embed=ver)
        if ctx.message.channel != verchan:
            await verchan.send(embed=ver)
        return
    elif gender == "f" or gender == "female":
        # verr = " ".join(f)
        ver = discord.Embed(
            description="༚ ✧˳⁺ {} has rece9ved the **Verified Female** role. ⁺˳✧ ༚ ".format(user.mention),
            color=0xFF93F0)
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
        msg = await ctx.send(embed=embed)
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
@commands.is_owner()
async def status(ctx, a, b, *, status: str = " "):
    if len(a) != 0:
        if (a == "o" or a == "online") and (b == "p" or b == "playing"):
            embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.playing))
        elif (a == "o" or a == "online") and (b == "w" or b == "watching"):
            embed = discord.Embed(description="Status changed. \n**Online**\n**Watching {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.watching))
        elif (a == "o" or a == "online") and (b == "l" or b == "listening"):
            embed = discord.Embed(description="Status changed. \n**Online**\n**Listening to {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.listening))
        elif (a == "i" or a == "idle") and (b == "p" or b == "playing"):
            embed = discord.Embed(description="Status changed. \n**Idle**\n**Playing {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.idle,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.playing))
        elif (a == "i" or a == "idle") and (b == "w" or b == "watching"):
            embed = discord.Embed(description="Status changed. \n**Idle**\n**Watching {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.idle,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.watching))
        elif (a == "i" or a == "idle") and (b == "l" or b == "listening"):
            embed = discord.Embed(description="Status changed. \n**Idle**\n**Listening to {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.idle,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.listening))
        elif (a == "d" or a == "dnd") and (b == "p" or b == "playing"):
            embed = discord.Embed(description="Status changed. \n**Do Not Disturb**\n**Playing {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name='{}'.format(status),
                                                                                           type=discord.ActivityType.playing))
        elif (a == "d" or a == "dnd") and (b == "w" or b == "watching"):
            embed = discord.Embed(
                description="Status changed. \n**Do Not Disturb**\n**Watching {}**".format(status), color=0x000000)
            await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name='{}'.format(status),
                                                                                           type=discord.ActivityType.watching))
        elif (a == "d" or a == "dnd") and (b == "l" or b == "listening"):
            embed = discord.Embed(
                description="Status changed. \n**Do Not Disturb**\n**Listening to {}**".format(status),
                color=0x000000)
            await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name='{}'.format(status),
                                                                                           type=discord.ActivityType.listening))
        elif a == "o" or a == "online":
            if len(a) == 1:
                statuss = ctx.message.content[9:]
            elif len(a) == 6:
                statuss = ctx.message.content[14:]
            embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(statuss),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(statuss),
                                                                type=discord.ActivityType.playing))
            embed2 = discord.Embed(description="Since you didn't provide a valid **status_msg**, I chose the default one: **Playing**.", color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
        elif a == "i" or a == "idle":
            if len(a) == 1:
                statuss = ctx.message.content[9:]
            elif len(a) == 4:
                statuss = ctx.message.content[12:]
            embed = discord.Embed(description="Status changed. \n**Idle**\n**Playing {}**".format(statuss),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.idle,
                                      activity=discord.Activity(name='{}'.format(statuss),
                                                                type=discord.ActivityType.playing))
            embed2 = discord.Embed(
                description="Since you didn't provide a valid **status_msg**, I chose the default one: **Playing**.",
                color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
        elif a == "d" or a == "dnd":
            if len(a) == 1:
                statuss = ctx.message.content[9:]
            elif len(a) == 3:
                statuss = ctx.message.content[11:]
            embed = discord.Embed(
                description="Status changed. \n**Do Not Disturb**\n**Playing {}**".format(statuss), color=0x000000)
            await bot.change_presence(status=discord.Status.dnd,
                                      activity=discord.Activity(name='{}'.format(statuss),
                                                                type=discord.ActivityType.playing))
            embed2 = discord.Embed(
                description="Since you didn't provide a valid **status_msg**, I chose the default one: **Playing**.",
                color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
        elif a == "playing" or a == "p":
            if len(a) == 1:
                statuss = ctx.message.content[9:]
            elif len(a) == 7:
                statuss = ctx.message.content[15:]
            embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(statuss),
                                 color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(statuss),
                                                                type=discord.ActivityType.playing))
            embed2 = discord.Embed(
                description="Since you didn't provide a valid **status_ttpe**, I chose the default one: **Online**.",
                color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
        elif a == "w" or a == "watching":
            if len(a) == 1:
                statuss = ctx.message.content[9:]
            elif len(a) == 8:
                statuss = ctx.message.content[16:]
            embed = discord.Embed(description="Status changed. \n**Online**\n**Watching {}**".format(statuss),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(statuss),
                                                                type=discord.ActivityType.watching))
            embed2 = discord.Embed(
                description="Since you didn't provide a valid **status_type**, I chose the default one: **Online**.",
                color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
        elif a == "l" or a == "listening":
            if len(a) == 1:
                statuss = ctx.message.content[9:]
            elif len(a) == 9:
                statuss = ctx.message.content[17:]
            embed = discord.Embed(description="Status changed. \n**Online**\n**Listening to {}**".format(statuss),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(statuss),
                                                                type=discord.ActivityType.listening))
            embed2 = discord.Embed(
                description="Since you didn't provide a valid **status_type**, I chose the default one: **Online**.",
                color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
        else:
            embed2 = discord.Embed(
                description="Since you didn't provide a valid **status_type** and/or **status_msg** combination, I chose the default ones: **Online** and **Playing**.",
                color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
            embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.playing))

        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="You didn't provide a status.", color=0xFF3639)
        embed.set_image(url=ctx.message.author.guild.icon_url)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
        return

@status.error
async def status_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        if len(ctx.message.content) > 8:
            embed2 = discord.Embed(
                description="Since you didn't provide a valid **status_type** and/or **status_msg**, I think that the status is empty. I'll get the status by your message. (COULD **NOT BE WORKING PROPERLY**!)",
                color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
            status = ctx.message.content[7:]
            embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.playing))
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description="You didn't provide a status.", color=0xFF3639)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed)
            return
    if isinstance(error, commands.MissingRequiredArgument):
        if len(ctx.message.content) > 8:
            embed2 = discord.Embed(
                description="Since you didn't provide a valid **status_type** and/or **status_msg**, I think that the status is empty. I'll get the status by your message. (COULD **NOT BE WORKING PROPERLY**!)",
                color=0xf2f542)
            embed2.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed2.set_footer(text="Warning raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed2)
            status = ctx.message.content[7:]
            embed = discord.Embed(description="Status changed. \n**Online**\n**Playing {}**".format(status),
                                  color=0x000000)
            await bot.change_presence(status=discord.Status.online,
                                      activity=discord.Activity(name='{}'.format(status),
                                                                type=discord.ActivityType.playing))
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=ctx.message.author.guild.icon_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description="You didn't provide a status.", color=0xFF3639)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
            await ctx.send(embed=embed)
            return
    if isinstance(error, commands.CheckFailure):
        await ctx.send("{}, sorry. This command is available only to the bot developer(s).".format(ctx.message.author.mention))
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
