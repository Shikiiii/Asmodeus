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
# setmuted, setconfess, starboard, prefix, lockdown, role, massban,
# masskick, massmute, bots

@bot.command()
async def logs(ctx, type, chan: discord.TextChannel):
    if type == "delete":
        deleteLogs[ctx.guild.id] = chan.id
        storage = bot.get_guild(646432280365236235)
        storageD = storage.get_channel(648951518602592277)
        for key, value in deleteLogsToDelete.items():
            if key == ctx.guild.id:
                msgID = int(value)
                msg = await storageD.fetch_message(msgID)
                await msg.edit(content="{}|{}".format(str(ctx.guild.id), str(chan.id)))
                embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :green_circle: Deleted logs changed to {}.".format(chan.mention), color=0x000000)
                await ctx.send(embed=embed)
                return
        message = await storageD.send("{}|{}".format(str(ctx.guild.id), str(chan.id)))
        deleteLogsToDelete[ctx.guild.id] = str(message.id)
        embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :green_circle: Deleted logs enabled! Channel set to {}.".format(chan.mention), color=0x000000)
        await ctx.send(embed=embed)
    elif type == "edit":
        print("Type is edit!")
        editLogs[ctx.guild.id] = chan.id
        print("ok, i got the storage channels")
        storage = bot.get_guild(646432280365236235)
        storageE = storage.get_channel(648951532905037834)
        print("ok, entering the for loop, hope i get out alive")
        print(editLogsToDelete)
        for key, value in editLogsToDelete.items():
            print("ok, report 1, im in, nothing strange")
            if key == ctx.guild.id:
                print("ok, some key is equal to guild.id")
                msgID = int(value)
                print("ok, lets fetch a message")
                msg = await storageE.fetch_message(msgID)
                print("now im editing a message")
                await msg.edit(content="{}|{}".format(str(ctx.guild.id), str(chan.id)))
                print("now lets tell whats going on")
                embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :green_circle: Edit logs changed to {}.".format(chan.mention), color=0x000000)
                print("sending the report")
                await ctx.send(embed=embed)
                return
        print("ok, no loops for me, editing the message")
        message = await storageE.send("{}|{}".format(str(ctx.guild.id), str(chan.id)))
        print("updating the dict")
        editLogsToDelete[ctx.guild.id] = message.id
        print("and, making a message")
        embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :green_circle: Edit logs enabled! Channel set to {}.".format(chan.mention), color=0x000000)
        print("sending!")
        await ctx.send(embed=embed)
    elif type == "member":
        memberLogs[ctx.guild.id] = chan.id
        storage = bot.get_guild(646432280365236235)
        storageMM = storage.get_channel(648951574319726592)
        for key, value in memberLogsToDelete.items():
            if key == ctx.guild.id:
                msgID = int(value)
                msg = await storageMM.fetch_message(msgID)
                await msg.edit(content="{}|{}".format(str(ctx.guild.id), str(chan.id)))
                embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :green_circle: Member join/leave logs changed to {}.".format(chan.mention), color=0x000000)
                await ctx.send(embed=embed)
                return
        message = await storageMM.send("{}|{}".format(str(ctx.guild.id), str(chan.id)))
        memberLogsToDelete[ctx.guild.id] = message.id
        embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :green_circle: Member join/leave enabled! Channel set to {}.".format(chan.mention), color=0x000000)
        await ctx.send(embed=embed)
    elif type == "punish":
        punishLogs[ctx.guild.id] = chan.id
        storage = bot.get_guild(646432280365236235)
        storageP= storage.get_channel(648951548809838628)
        for key, value in punishLogsToDelete.items():
            if key == ctx.guild.id:
                msgID = int(value)
                msg = await storageP.fetch_message(msgID)
                await msg.edit(content="{}|{}".format(str(ctx.guild.id), str(chan.id)))
                embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :no_entry: Punishment logs changed to {}.".format(chan.mention), color=0x000000)
                await ctx.send(embed=embed)
                return
        message = await storageP.send("{}|{}".format(str(ctx.guild.id), str(chan.id)))
        punishLogsToDelete[ctx.guild.id] = message.id
        embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ :no_entry: Punishment logs enabled! Channel set to {}.".format(chan.mention), color=0x000000)
        await ctx.send(embed=embed)
    else:
        prefix = "!"
        for key, value in serverPrefixes.items():
            if int(key) == ctx.guild.id:
                prefix = str(value)
        embed = discord.Embed(title="{}".format(ctx.message.author.name), description="Type of logs not found. The current types are: \n``delete`` : Logs from deleted messages\n``edit`` : Logs from edited messages\n``member`` : Logs from join/leave of members\n``punish`` : Logs from all staff commands\n\nTo setup these logs, do {}logs [type] [channel/disable]".format(prefix), color=0xF21B1B)
        await ctx.send(embed=embed)
        
@logs.error
async def logs_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        prefix = "!"
        for key, value in serverPrefixes.items():
            if int(key) == ctx.guild.id:
                prefix = str(value)
        type = ctx.message.content[6:]
        if type == "delete":
            for key, value in deleteLogs.items():
                if int(key) == ctx.guild.id:
                    chan = bot.get_channel(int(value))
                    embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Deleted logs are enabled for this server in {}.".format(chan.mention), color=0x000000)
                    await ctx.send(embed=embed)
                    return
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Deleted logs aren't enabled for this server.", color=0x000000)
            await ctx.send(embed=embed)
            return
        elif type == "edit":
            for key, value in editLogs.items():
                if int(key) == ctx.guild.id:
                    chan = bot.get_channel(int(value))
                    embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Edit logs are enabled for this server in {}.".format(chan.mention), color=0x000000)
                    await ctx.send(embed=embed)
                    return
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Edit logs aren't enabled for this server.", color=0x000000)
            await ctx.send(embed=embed)
            return
        elif type == "member":
            for key, value in memberLogs.items():
                if int(key) == ctx.guild.id:
                    chan = bot.get_channel(int(value))
                    embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Member join/leave logs are enabled for this server in {}.".format(chan.mention), color=0x000000)
                    await ctx.send(embed=embed)
                    return
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Member join/leave logs aren't enabled for this server.", color=0x000000)
            await ctx.send(embed=embed)
            return
        elif type == "punish":
            for key, value in deleteLogs.items():
                if int(key) == ctx.guild.id:
                    chan = bot.get_channel(int(value))
                    embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Punishment logs are enabled for this server in {}.".format(chan.mention), color=0x000000)
                    await ctx.send(embed=embed)
                    return
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Punishment logs aren't enabled for this server.", color=0x000000)
            await ctx.send(embed=embed)
            return
        else:
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉  Type of logs not found. The current types are: \n``delete`` : Logs from deleted messages\n``edit`` : Logs from edited messages\n``member`` : Logs from join/leave of members\n``punish`` : Logs from all staff commands\n\nTo setup these logs, do {}logs [type] [channel/disable]".format(prefix), color=0x000000)
            await ctx.send(embed=embed)
            return
    elif isinstance(error, commands.BadArgument):
        prefix = "!"
        for key, value in serverPrefixes.items():
            if int(key) == ctx.guild.id:
                prefix = str(value)
        typee = ctx.message.content[6:]
        type = typee.split(" ")
        if type[1] != "disable":
            if type[0] == "delete":
                for key, value in deleteLogs.items():
                    if int(key) == ctx.guild.id:
                        chan = bot.get_channel(int(value))
                        embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Deleted logs are enabled for this server in {}.".format(chan.mention), color=0x000000)
                        await ctx.send(embed=embed)
                        return
                embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Deleted logs aren't enabled for this server.", color=0x000000)
                await ctx.send(embed=embed)
                return
            elif type[0] == "edit":
                for key, value in editLogs.items():
                    if int(key) == ctx.guild.id:
                        chan = bot.get_channel(int(value))
                        embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Edit logs are enabled for this server in {}.".format(chan.mention), color=0x000000)
                        await ctx.send(embed=embed)
                        return
                embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Edit logs aren't enabled for this server.", color=0x000000)
                await ctx.send(embed=embed)
                return
            elif type[0] == "member":
                for key, value in memberLogs.items():
                    if int(key) == ctx.guild.id:
                        chan = bot.get_channel(int(value))
                        embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Member join/leave logs are enabled for this server in {}.".format(chan.mention), color=0x000000)
                        await ctx.send(embed=embed)
                        return
                embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Member join/leave logs aren't enabled for this server.", color=0x000000)
                await ctx.send(embed=embed)
                return
            elif type[0] == "punish":
                for key, value in deleteLogs.items():
                    if int(key) == ctx.guild.id:
                        chan = bot.get_channel(int(value))
                        embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Punishment logs are enabled for this server in {}.".format(chan.mention), color=0x000000)
                        await ctx.send(embed=embed)
                        return
                embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Punishment logs aren't enabled for this server.", color=0x000000)
                await ctx.send(embed=embed)
                return
            else:
                embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉  Type of logs not found. The current types are: \n``delete`` : Logs from deleted messages\n``edit`` : Logs from edited messages\n``member`` : Logs from join/leave of members\n``punish`` : Logs from all staff commands\n\nTo setup these logs, do {}logs [type] [channel/disable]".format(prefix), color=0x000000)
                await ctx.send(embed=embed)
                return
        elif type[1] == "disable":
            if type[0] == "delete":
                storage = bot.get_guild(646432280365236235)
                storageD = storage.get_channel(648951518602592277)
                chan = None
                check = False
                for key, value in deleteLogs.items():
                    if key == ctx.guild.id:
                        check = True
                        chan = bot.get_channel(int(value))
                if check == True:
                    del deleteLogs[ctx.guild.id]
                    for key, value in deleteLogsToDelete.items():
                        if int(key) == ctx.guild.id:
                            msg = await storageD.fetch_message(int(value))
                            await msg.delete()
                    del deleteLogsToDelete[ctx.guild.id]
                    embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Delete logs have been disabled for this server.", color=0x000000)
                    await ctx.send(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Uh-oh! Delete logs aren't enabled for this server, so you can't disable them.", color=0x000000)
                    await ctx.send(embed=embed)
                    return
            elif type[0] == "edit":
                storage = bot.get_guild(646432280365236235)
                storageE = storage.get_channel(648951532905037834)
                chan = None
                check = False
                for key, value in editLogs.items():
                    if key == ctx.guild.id:
                        check = True
                        chan = bot.get_channel(int(value))
                if check == True:
                    del editLogs[ctx.guild.id]
                    for key, value in editLogsToDelete.items():
                        if int(key) == ctx.guild.id:
                            msg = await storageE.fetch_message(int(value))
                            await msg.delete()
                    del editLogsToDelete[ctx.guild.id]
                    embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Edit logs have been disabled for this server.", color=0x000000)
                    await ctx.send(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Uh-oh! Edit logs aren't enabled for this server, so you can't disable them.", color=0x000000)
                    await ctx.send(embed=embed)
                    return
            elif type[0] == "member":
                storage = bot.get_guild(646432280365236235)
                storageMM = storage.get_channel(648951574319726592)
                chan = None
                check = False
                for key, value in memberLogs.items():
                    if key == ctx.guild.id:
                        check = True
                        chan = bot.get_channel(int(value))
                if check == True:
                    del memberLogs[ctx.guild.id]
                    for key, value in memberLogsToDelete.items():
                        if int(key) == ctx.guild.id:
                            msg = await storageMM.fetch_message(int(value))
                            await msg.delete()
                    del memberLogsToDelete[ctx.guild.id]
                    embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Member join/leave logs have been disabled for this server.", color=0x000000)
                    await ctx.send(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Uh-oh! Member join/leave logs aren't enabled for this server, so you can't disable them.", color=0x000000)
                    await ctx.send(embed=embed)
                    return
            elif type[0] == "punish":
                storage = bot.get_guild(646432280365236235)
                storageP= storage.get_channel(648951548809838628)
                chan = None
                check = False
                for key, value in punishLogs.items():
                    if key == ctx.guild.id:
                        check = True
                        chan = bot.get_channel(int(value))
                if check == True:
                    del punishLogs[ctx.guild.id]
                    for key, value in punishLogsToDelete.items():
                        if int(key) == ctx.guild.id:
                            msg = await storageP.fetch_message(int(value))
                            await msg.delete()
                    del punishLogsToDelete[ctx.guild.id]
                    embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Punishment logs have been disabled for this server.", color=0x000000)
                    await ctx.send(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉ Uh-oh! Punishment logs aren't enabled for this server, so you can't disable them.", color=0x000000)
                    await ctx.send(embed=embed)
                    return
            else:
                embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉  Type of logs not found. The current types are: \n``delete`` : Logs from deleted messages\n``edit`` : Logs from edited messages\n``member`` : Logs from join/leave of members\n``punish`` : Logs from all staff commands\n\nTo setup these logs, do {}logs [type] [channel/disable]".format(prefix), color=0x000000)
                await ctx.send(embed=embed)
                return
        else:
            embed = discord.Embed(title="{}".format(ctx.message.author.name), description=".҉  Type of logs not found. The current types are: \n``delete`` : Logs from deleted messages\n``edit`` : Logs from edited messages\n``member`` : Logs from join/leave of members\n``punish`` : Logs from all staff commands\n\nTo setup these logs, do {}logs [type] [channel/disable]".format(prefix), color=0x000000)
            await ctx.send(embed=embed)
            return
            
@bot.command()
async def setmuted(ctx, *, rolee: str):
    role = None
    if len(ctx.message.role_mentions) > 0:
        role = ctx.guild.get_role(ctx.message.role_mentions[0].id)
    if role is None:
        role = await parse_roles(ctx, rolee)
    if role is None:
        embed = discord.Embed(title="{}".format(ctx.message.author.name), description="Role not found. :(", color=0x000000)
        await ctx.send(embed=embed)
        return
    serverMuted[str(ctx.guild.id)] = str(role.id)
    storage = bot.get_guild(646432280365236235)
    storageM = storage.get_channel(648898928221093908)
    for key, value in serverMutedToDelete.items():
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

