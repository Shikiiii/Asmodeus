import discord
from discord.ext import commands

import random
import sys
import traceback
import asyncio
import datetime
import json

from common_vars import *

# Commands in this file:
# setmuted, setconfess, starboard, prefix, lockdown, role, massban,
# masskick, massmute, bots

@bot.command()
async def setmuted(ctx, *, rolee: str):
    role = await parse_roles(ctx, rolee)
    serverMuted[str(ctx.guild.id)] = str(role.id)
    storage = bot.get_guild(646432280365236235)
    storageM = storage.get_channel(648898928221093908)
    for key, value in serverMuted.items():
        if int(key) == ctx.guild.id:
            msgID = int(value)
            msg = await storageM.fetch_message(msgID)
            await msg.edit(content="{}|{}".format(str(ctx.guild.id), str(role.id)))
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :no_entry: Muted role changed to {}.".format(role.mention), color=0x000000)
            await ctx.send(embed=embed)
            return
    message = await storageM.send("{}|{}".format(str(ctx.guild.id), str(role.id)))
    serverMutedToDelete[ctx.guild.id] = message.id
    embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :no_entry: Muted role set to {}.".format(role.mention), color=0x000000)
    await ctx.send(embed=embed)

@setmuted.error
async def setmuted_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        role = None
        for key, value in serverMuted.items():
            if int(key) == ctx.guild.id:
                role = await parse_roles(ctx, role)
            else:

        prefix = "!"
        for key, value in serverPrefixes.items():
            if int(key) == message.guild.id:
                prefix = str(value)
        
        if role is None:
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :no_entry: Mute is currently disabled because you do not have a chosen role to use. Please choose a role with {}setmuted [role].".format(prefix), color=0x000000)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :no_entry: Muted role is currently {}.".format(role.mention), color=0x000000)
            await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        role = None
        for key, value in serverMuted.items():
            if int(key) == ctx.guild.id:
                role = bot.get_channel(int(value))
            else:
                role = None
        #if len(chan) <= 1:
        #    chan = 0

        prefix = "!"
        for key, value in serverPrefixes.items():
            if int(key) == message.guild.id:
                prefix = str(value)
        
        if role is None:
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :no_entry: Mute is currently disabled because you do not have a chosen role to use. Please choose a role with {}setmuted [role].".format(prefix), color=0x000000)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :no_entry: Muted role is currently {}.".format(role.mention), color=0x000000)
            await ctx.send(embed=embed)
    elif isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    
@bot.command()
@commands.has_permissions(manage_guild=True)
async def setconfess(ctx, *, chan: discord.TextChannel):
    confessChannels[str(ctx.guild.id)] = str(chan.id)
    storage = bot.get_guild(646432280365236235)
    storageCF = storage.get_channel(647444887184080906)
    for key, value in confessChannelsToDelete.items():
        if int(key) == ctx.guild.id:
            msgID = int(value)
            msg = await storageCF.fetch_message(msgID)
            await msg.edit(content="{}|{}".format(str(ctx.guild.id), str(chan.id)))
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :shushing_face: Confess channel changed to {}.".format(chan.mention), color=0x000000)
            await ctx.send(embed=embed)
            return
    message = await storageCF.send("{}|{}".format(str(ctx.guild.id), str(chan.id)))
    confessChannelsToDelete[ctx.guild.id] = message.id
    embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :shushing_face: Confess is enabled! Channel set to {}.".format(chan.mention), color=0x000000)
    await ctx.send(embed=embed)

@setconfess.error
async def setconfess_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        chan = None
        for key, value in confessChannels.items():
            if int(key) == ctx.guild.id:
                chan = bot.get_channel(int(value))
            else:
                chan = None
        #if len(chan) <= 1:
        #    chan = 0
        prefix = "!"
        for key, value in serverPrefixes.items():
            if int(key) == message.guild.id:
                prefix = str(value)
        
        if chan is None:
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :shushing_face: Confess isn't enabled for this server. Try setting a channel for it using {}confess [channel].".format(prefix), color=0x000000)
            await ctx.send(embed=embed)
        else:
            chan
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :shushing_face: Confess is currently set for {}.".format(chan.mention), color=0x000000)
            await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        if ctx.message.content[12:] == "disable":
            del confessChannels[str(ctx.guild.id)]
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :shushing_face: Confess has been disabled. Thanks for using this feature!", color=0x000000)
            await ctx.send(embed=embed)
            return
        chan = None
        for key, value in confessChannels.items():
            if int(key) == ctx.guild.id:
                chan = bot.get_channel(int(value))
            else:
                chan = None
        #if len(chan) <= 1:
        #    chan = 0

        prefix = "!"
        for key, value in serverPrefixes.items():
            if int(key) == ctx.guild.id:
                prefix = str(value)
        
        if chan is None:
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :shushing_face: Confess isn't enabled for this server. Try setting a channel for it using {}confess [channel].".format(prefix), color=0x000000)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :shushing_face: Confess is currently set for {}.".format(chan.mention), color=0x000000)
            await ctx.send(embed=embed)
    elif isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

@bot.command()
@commands.has_permissions(manage_guild=True)
async def starboard(ctx, *, chan: discord.TextChannel):
    starboardChannels[str(ctx.guild.id)] = str(chan.id)
    storage = bot.get_guild(646432280365236235)
    storageSB = storage.get_channel(647616003164864514)
    for key, value in starboardChannelsToDelete.items():
        if int(key) == ctx.guild.id:
            msgID = int(value)
            msg = await storageSB.fetch_message(msgID)
            await msg.edit(content="{}|{}".format(str(ctx.guild.id), str(chan.id)))
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :star: Starboard channel changed to {}.".format(chan.mention), color=0x000000)
            await ctx.send(embed=embed)
            return
    message = await storageSB.send("{}|{}".format(str(ctx.guild.id), str(chan.id)))
    starboardChannelsToDelete[ctx.guild.id] = message.id
    embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :star: Starboard is enabled! Channel set to {}.".format(chan.mention), color=0x000000)
    await ctx.send(embed=embed)

@starboard.error
async def starboard_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        chan = None
        for key, value in starboardChannels.items():
            if int(key) == ctx.guild.id:
                chan = bot.get_channel(int(value))
            else:
                chan = None
        #if len(chan) <= 1:
        #    chan = 0

        prefix = "!"
        for key, value in serverPrefixes.items():
            if int(key) == message.guild.id:
                prefix = str(value)
        
        if chan is None:
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :star: Starboard isn't enabled for this server. Try setting a channel for it using {}starboard [channel].".format(prefix), color=0x000000)
            await ctx.send(embed=embed)
        else:
            chan
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :star: Starboard is currently set for {}.".format(chan.mention), color=0x000000)
            await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        if ctx.message.content[11:] == "disable":
            del starboardChannels[str(ctx.guild.id)]
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :star: Starboard has been disabled. Thanks for using this feature!", color=0x000000)
            await ctx.send(embed=embed)
            return
        chan = None
        for key, value in starboardChannels.items():
            if int(key) == ctx.guild.id:
                chan = bot.get_channel(int(value))
            else:
                chan = None
        #if len(chan) <= 1:
        #    chan = 0

        prefix = "!"
        for key, value in serverPrefixes.items():
            if int(key) == message.guild.id:
                prefix = str(value)
        
        if chan is None:
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :star: Starboard isn't enabled for this server. Try setting a channel for it using {}starboard [channel].".format(prefix), color=0x000000)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :star: Starboard is currently set for {}.".format(chan.mention), color=0x000000)
            await ctx.send(embed=embed)
    elif isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

@bot.command()
@commands.has_permissions(manage_guild=True)
async def prefix(ctx, *, prefix: str):
    if len(prefix) <= 100:
        serverPrefixes[str(ctx.guild.id)] = prefix
        print(serverPrefixes)
        storage = bot.get_guild(646432280365236235)
        storagePrefix = storage.get_channel(646432846961049601)
        for key, value in serverPrefixesToDelete.items():
            if int(key) == ctx.guild.id:
                msgID = int(value)
                msg = await storagePrefix.fetch_message(msgID)
                await msg.edit(content="{}|{}".format(str(ctx.guild.id), str(prefix)))
                embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Prefix for **{}** changed to ``{}``.".format(ctx.guild.name, prefix), color=0x000000)
                await ctx.send(embed=embed)
                return
        message = await storagePrefix.send("{}|{}".format(str(ctx.guild.id), str(prefix)))
        serverPrefixesToDelete[ctx.guild.id] = message.id
        embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Prefix for **{}** changed to ``{}``.".format(ctx.guild.name, prefix), color=0x000000)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="We've limited the prefixes to 100 characters. It appears you typed a prefix longer than that.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    
@prefix.error
async def prefix_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="{}".format(ctx.message.author.name), description="To change the prefix, try giving me a prefix.", color=0x000000)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

@bot.command()
@commands.has_permissions(administrator=True)
async def lockdown(ctx):
    lockdownRole = discord.utils.get(ctx.message.guild.roles, name="@everyone")
    check = ctx.message.channel.overwrites_for(lockdownRole)
    if check.send_messages == False:
        lockdownMsg = discord.Embed(description="**Lockdown mode** : :red_circle: OFF | {}".format(ctx.message.author.mention), color=0xFFF308)
        lockdownMsg.set_footer(text="Note: Lockdown only affects the channel where the command was ran.")
        await ctx.send(embed=lockdownMsg)
        await ctx.message.channel.set_permissions(lockdownRole, send_messages=True)
    elif check.send_messages == True:
        lockdownMsg = discord.Embed(description="**Lockdown mode** : :green_circle: ON | {}".format(ctx.message.author.mention), color=0xFFF308)
        lockdownMsg.set_footer(text="Note: Lockdown only affects the channel where the command was ran.")
        await ctx.send(embed=lockdownMsg)
        await ctx.message.channel.set_permissions(lockdownRole, send_messages=False)
    else:
        lockdownMsg = discord.Embed(description="**Lockdown mode** : :green_circle: ON | {}".format(ctx.message.author.mention), color=0xFFF308)
        lockdownMsg.set_footer(text="Note: Lockdown only affects the channel where the command was ran.")
        await ctx.send(embed=lockdownMsg)
        await ctx.message.channel.set_permissions(lockdownRole, send_messages=False)
        
@lockdown.error
async def lockdown_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            description="You don't have the permissions to use this command.".format(ctx.message.author.mention),
            color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
        
@bot.command()
@commands.has_permissions(manage_roles=True, administrator=True)
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
    roless = [role1, role2, role3, role4, role5, role6, role7, role8, role9, role10, role11, role12, role13, role14,
              role15, role16, role17, role18, role19, role20, role21, role22, role23, role24, role25, role26, role27,
              role28, role29, role30, role31, role32, role33, role34, role35]
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
    # await ctx.send("{} look now, do i look like a magician? just mention a user and i'll ban them \n example: ``!ban @dy ez noob``".format(ctx.message.author.mention))
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="You didn't give me a user and/or a role.", color=0xFF3639)
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
        
@bot.command()
@commands.has_permissions(administrator=True)
async def massban(ctx, *, users: str):
    desc = "Mass ban started. May take a while. \n\n"
    embed = discord.Embed(description=desc, color=0x000000)
    embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    msg = await ctx.send(embed=embed)
    mentions = ctx.message.mentions
    for user in mentions:
        try:
            await user.ban()
        except:
            await ctx.send(f"Couldn't ban {user.mention} because of missing permissions.")
            
@massban.error
async def massban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="No @mentioned users were found with the information you gave.",
                              color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="No @mentioned users were found with the information you gave.",
                              color=0xFF3639)
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
@commands.has_permissions(administrator=True)
async def massmute(ctx, *, users: str):
    desc = "Mass mute started. May take a while. \n\n"
    role = discord.utils.get(ctx.message.author.guild.roles, name="Muted")
    embed = discord.Embed(description=desc, color=0x000000)
    embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    msg = await ctx.send(embed=embed)
    mentions = ctx.message.mentions
    for user in mentions:
        try:
            await user.add_roles(role)
        except:
            await ctx.send(f"Couldn't kick {user.mention} because of missing permissions.")

@massmute.error
async def massmute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="No @mentioned users were found with the information you gave.",
                              color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="No @mentioned users were found with the information you gave.",
                              color=0xFF3639)
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
@commands.has_permissions(administrator=True)
async def masskick(ctx, *, users: str):
    desc = "Mass kick started. May take a while. \n\n"
    embed = discord.Embed(description=desc, color=0x000000)
    embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    msg = await ctx.send(embed=embed)
    mentions = ctx.message.mentions
    for user in mentions:
        try:
            await user.kick()
        except:
            await ctx.send(f"Couldn't kick {user.mention} because of missing permissions.")

@masskick.error
async def masskick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="No @mentioned users were found with the information you gave.",
                              color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(description="No @mentioned users were found with the information you gave.",
                              color=0xFF3639)
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
@commands.has_permissions(administrator=True)
async def bots(ctx):
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
        embed = discord.Embed(description="Too many bots, can't send the message.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)

@bots.error
async def bots_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        embed = discord.Embed(description="You don't have the permissions to use this command.", color=0xFF3639)
        embed.set_author(name="{}".format(ctx.message.author), icon_url=ctx.message.author.avatar_url)
        embed.set_footer(text="Error raised on: {}".format(ctx.message.content))
        await ctx.send(embed=embed)
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, None, file=sys.stderr)

