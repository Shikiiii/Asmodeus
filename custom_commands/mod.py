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

from discord.ext.commands.cooldowns import BucketType

# Commands in this file:
# ban, unban, banid, kick, mute, unmute,
# purge, clear

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason: str):
    if len(reason) == 0:
        punishMsg = discord.Embed(description="{} was banned.\n``Reason:`` N/A\n``Duration:`` -".format(user.mention), color=0x000000)
        punishMsg.set_author(name="{}".format(ctx.message.author.name))
        punishMsg.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=punishMsg)
        try:
            await user.send("You've been banned from {}.".format(ctx.server.name))
        except:
            embed = discord.Embed(
                description="I tried to DM the user, but I'm not allowed to because their DMs aren't open.",
                color=0xebf533)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
        await user.ban(reason="N/A")
        logch = None
        for key, value in punishLogs.items():
            if int(key) == message.author.guild.id:
                logch = bot.get_channel(int(value))
        if logch is None:
            return
        log = discord.Embed(description="Used command ``!ban`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(
            ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF, timestamp=datetime.utcnow())
        log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        log.set_footer(text="{}".format(corfor))
        log.set_thumbnail(url=user.avatar_url)
        await logch.send(embed=log)
    else:
        punishMsg = discord.Embed(description="{} was banned.\n``Reason:`` {}\n``Duration:`` -".format(user.mention, reason), color=0x000000)
        punishMsg.set_author(name="{}".format(ctx.message.author.name))
        punishMsg.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=punishMsg)
        try:
            await user.send("You've been banned from {}.".format(ctx.server.name))
        except:
            embed = discord.Embed(
                description="I tried to DM the user, but I'm not allowed to because their DMs aren't open.",
                color=0xebf533)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
        await user.ban(reason=reason)
        logch = None
        for key, value in punishLogs.items():
            if int(key) == message.author.guild.id:
                logch = bot.get_channel(int(value))
        if logch is None:
            return
        log = discord.Embed(description="Used command ``!ban`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(
            ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF, timestamp=datetime.utcnow())
        log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        log.set_thumbnail(url=user.avatar_url)
        await logch.send(embed=log)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this user.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            description="Give me a user to ban. \n``TIP:`` If you want to ban a user that's not in the server, try using !banid.",
            color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, id: int, *, reason: str = ""):
    user = await bot.fetch_user(id)
    if user is None:
        embed = discord.Embed(description="User doesn't exist.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        return
    banEntry = await ctx.message.guild.fetch_ban(user)
    if banEntry is None:
        embed = discord.Embed(description="This user is not banned.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
        return
    else:
        if banEntry.reason is None:
            punishMsg = discord.Embed(description="{} was unbanned.".format(user.mention), color=0x000000)
            punishMsg.set_author(name="{}".format(ctx.message.author.name))
            punishMsg.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=punishMsg)
            logch = None
            for key, value in punishLogs.items():
                if int(key) == message.author.guild.id:
                    logch = bot.get_channel(int(value))
            if logch is None:
                return
            log = discord.Embed(description="Used command ``!unban`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(
                ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF, timestamp=datetime.utcnow())
            log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            log.set_thumbnail(url=user.avatar_url)
            await logch.send(embed=log)
        else:
            punishMsg = discord.Embed(description="{} was unbanned.".format(banEntry.user.mention), color=0x000000)
            punishMsg.set_author(name="{}".format(ctx.message.author.name))
            punishMsg.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=punishMsg)
            logch = None
            for key, value in punishLogs.items():
                if int(key) == message.author.guild.id:
                    logch = bot.get_channel(int(value))
            if logch is None:
                return
            log = discord.Embed(description="Used command ``!unban`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(
                ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF, timestamp=datetime.utcnow())
            log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            log.set_thumbnail(url=user.avatar_url)
            await logch.send(embed=log)
        await ctx.message.guild.unban(banEntry.user, reason="Unbanned by mod.")
        
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this user. Is the ID correct?", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="I couldn't  unban.. no one? Try giving me the ID of an user.",
                              color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
@bot.command()
@commands.has_permissions(ban_members=True)
async def banid(ctx, id: int, *, reason: str):
    user = await bot.fetch_user(id)
    if user is None:
        embed = discord.Embed(description="User doesn't exist, duh.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        return
    if len(reason) == 0:
        punishMsg = discord.Embed(description="{} was banned.\n``Reason:`` N/A\n``Duration:`` -".format(user.mention), color=0x000000)
        punishMsg.set_author(name="{}".format(ctx.message.author.name))
        punishMsg.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=punishMsg)
        logch = None
        for key, value in punishLogs.items():
            if int(key) == message.author.guild.id:
                logch = bot.get_channel(int(value))
        if logch is None:
            return
        log = discord.Embed(description="Used command ``!banid`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(
            ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF, timestamp=datetime.utcnow())
        log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        log.set_thumbnail(url=user.avatar_url)
        await logch.send(embed=log)
        await ctx.message.guild.ban(discord.Object(id=id), reason="N/A")
    else:
        punishMsg = discord.Embed(description="{} was banned.\n``Reason:`` {}\n``Duration:`` -".format(user.mention, reason), color=0x000000)
        punishMsg.set_author(name="{}".format(ctx.message.author.name))
        punishMsg.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=punishMsg)
        await ctx.message.guild.ban(discord.Object(id=id), reason=reason)
        logch = None
        for key, value in punishLogs.items():
            if int(key) == message.author.guild.id:
                logch = bot.get_channel(int(value))
        if logch is None:
            return
        log = discord.Embed(description="Used command ``!banid`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(
            ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF, timestamp=datetime.utcnow())
        log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        log.set_thumbnail(url=user.avatar_url)
        await logch.send(embed=log)
        
@banid.error
async def banid_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this user. Is the ID correct?", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="Give me ID of an user to ban.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason: str):
    if len(reason) == 0:
        punishMsg = discord.Embed(description="{} was kicked.\n``Reason:`` N/A\n``Duration:``-".format(user.mention), color=0x000000)
        punishMsg.set_author(name="{}".format(ctx.message.author.name))
        punishMsg.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=punishMsg)
        try:
            await ctx.send("You've been kicked from {}.".format(ctx.server.name))
        except:
            embed = discord.Embed(
                description="I tried to DM the user, but I'm not allowed to because their DMs aren't open.",
                color=0xebf533)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
        await user.kick(reason="N/A")
        logch = None
        for key, value in punishLogs.items():
            if int(key) == message.author.guild.id:
                logch = bot.get_channel(int(value))
        if logch is None:
            return
        log = discord.Embed(description="Used command ``!kick`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(
            ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF, timestamp=datetime.utcnow())
        log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        log.set_thumbnail(url=user.avatar_url)
        await logch.send(embed=log)
    else:
        punishMsg = discord.Embed(description="{} was kicked.\n``Reason:`` N/A\n``Duration:``-".format(user.mention), color=0x000000)
        punishMsg.set_author(name="{}".format(ctx.message.author.name))
        punishMsg.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=punishMsg)
        try:
            await ctx.send("You've been kicked from {}.".format(ctx.server.name))
        except:
            embed = discord.Embed(
                description="I tried to DM the user, but I'm not allowed to because their DMs aren't open.",
                color=0xebf533)
            embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
        await user.kick(reason=reason)
        logch = None
        for key, value in punishLogs.items():
            if int(key) == message.author.guild.id:
                logch = bot.get_channel(int(value))
        if logch is None:
            return
        log = discord.Embed(description="Used command ``!kick`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(
            ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF, timestamp=datetime.utcnow())
        log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        log.set_thumbnail(url=user.avatar_url)
        await logch.send(embed=log)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this user. Try giving me a correct user.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="I couldn't kick.. no one? Try giving me a correct user.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
@bot.command()
@commands.has_permissions(manage_messages=True)
#@commands.cooldown(3, 86400, BucketType.user)
async def mute(ctx, user: discord.Member, *, reason: str):
    mutedrole = None
    for key, value in serverMuted.items():
        if int(key) == ctx.guild.id:
            mutedrole = await parse_roles(ctx, str(value))
    prefix = "!"
    for key, value in serverPrefixes.items():
        if int(key) == ctx.guild.id:
            prefix = str(value)
    if mutedrole is None:
        embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :no_entry: Mute is currently disabled because you do not have a chosen role to use. Please tell an administrator to choose a role with {}setmuted [role].".format(prefix), color=0x000000)
        await ctx.send(embed=embed)
        return
    if mutedrole in user.roles:
        embed = discord.Embed(description="This user is already muted.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
        return
    else:
        if len(reason) == 0:
            punishMsg = discord.Embed(description="{} was muted.\n``Reason:`` N/A\n``Duration:`` -".format(user.mention), color=0x000000)
            punishMsg.set_author(name="{}".format(ctx.message.author.name))
            punishMsg.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=punishMsg)
            await user.add_roles(mutedrole, reason="N/A")
            await user.edit(mute=True)
            logch = None
            for key, value in punishLogs.items():
                if int(key) == message.author.guild.id:
                    logch = bot.get_channel(int(value))
            if logch is None:
                return
            log = discord.Embed(description="Used command ``!mute`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(
                ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF, timestamp=datetime.utcnow())
            log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            log.set_thumbnail(url=user.avatar_url)
            await logch.send(embed=log)
            
        else:
            punishMsg = discord.Embed(description="{} was muted.\n``Reason:`` {}\n``Duration:`` -".format(user.mention, reason), color=0x000000)
            punishMsg.set_author(name="{}".format(ctx.message.author.name))
            punishMsg.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=punishMsg)
            await user.add_roles(mutedrole, reason=reason)
            await user.edit(mute=True)
            logch = None
            for key, value in punishLogs.items():
                if int(key) == message.author.guild.id:
                    logch = bot.get_channel(int(value))
            if logch is None:
                return
            log = discord.Embed(description="Used command ``!mute`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(
                ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF, timestamp=datetime.utcnow())
            log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            log.set_thumbnail(url=user.avatar_url)
            await logch.send(embed=log)
        
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="I couldn't find this user. Try giving me a correct user.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="I couldn't mute.. no one? Try giving me a correct user.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, user: discord.Member):
    mutedrole = None
    for key, value in serverMuted.items():
        if int(key) == ctx.guild.id:
            mutedrole = await parse_roles(ctx, str(value))
    prefix = "!"
    for key, value in serverPrefixes.items():
        if int(key) == ctx.guild.id:
            prefix = str(value)
    if mutedrole is None:
        embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :no_entry: Mute is currently disabled because you do not have a chosen role to use. Please tell an administrator to choose a role with {}setmuted [role].".format(prefix), color=0x000000)
        await ctx.send(embed=embed)
        return
    if mutedrole in user.roles:
            punishMsg = discord.Embed(description="{} was unmuted.".format(user.mention), color=0x000000)
            punishMsg.set_author(name="{}".format(ctx.message.author.name))
            punishMsg.set_thumbnail(url=user.avatar_url)
            await ctx.send(embed=punishMsg)
            await user.remove_roles(mutedrole)
            await user.edit(mute=False)
            logch = None
            for key, value in punishLogs.items():
                if int(key) == message.author.guild.id:
                    logch = bot.get_channel(int(value))
            if logch is None:
                return
            log = discord.Embed(description="Used command ``!unmute`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(
                ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF, timestamp=datetime.utcnow())
            log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
            log.set_thumbnail(url=user.avatar_url)
            await logch.send(embed=log)
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
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="I couldn't unmute.. no one? Try giving me a correct user.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clean(ctx):
    def check(m):
        return m.author.bot

    # rr = todeln + 1
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
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount, *, user: discord.Member):
    try:
        todeln = int(amount)
    except:
        ctx.message.delete()
        embed = discord.Embed(description="You didn't enter a number of messages to delete. Try again!", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(10)
        await msg.delete()
        return
    if todeln > 0:
        def check(m):
            return m.author == user

        # rr = todeln + 1
        await ctx.message.delete()
        deleted = await ctx.message.channel.purge(limit=todeln, check=check)
        embed = discord.Embed(description="Successfully purged **{}** messages by **{}**.".format(todeln, user.mention),
                              color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()
        logch = None
        for key, value in punishLogs.items():
            if int(key) == message.author.guild.id:
                logch = bot.get_channel(int(value))
        if logch is None:
            return
        log = discord.Embed(description="Used command ``!purge`` in {}:\n{}\n\nMod ID: {}\nUser ID: {}".format(
            ctx.message.channel.mention, ctx.message.content, ctx.message.author.id, user.id), color=0xFFFFFF, timestamp=datetime.utcnow())
        log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
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
        deleted = await ctx.message.channel.purge(limit=(todeln + 1))
        embed = discord.Embed(description="Successfully purged **{}** messages.".format(todeln), color=0x000000)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        msgg = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        msgg.delete()
        logch = None
        for key, value in punishLogs.items():
            if int(key) == message.author.guild.id:
                logch = bot.get_channel(int(value))
        if logch is None:
            return
        log = discord.Embed(
            description="Used command ``!purge`` in {}:\n{}\n\nMod ID: {}".format(ctx.message.channel.mention,
                                                                                  ctx.message.content,
                                                                                  ctx.message.author.id),
                                                                                  color=0xFFFFFF,
                                                                                  timestamp=datetime.utcnow())
        log.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        log.set_footer(text="{}".format(corfor))
        # log.set_thumbnail(url=user.avatar_url)
        await logch.send(embed=log)
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)
        
        
