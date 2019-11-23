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
import custom_commands.events

guild: Optional[Guild] = None

shiki: Optional[Member] = None

bot.remove_command('help')

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
                        value="``prefix``, ``lockdown``, ``role``, ``masskick``, ``massmute``, ``massban``, ``bots``")
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
    elif cmd == "prefix":
        embed = discord.Embed(title="!prefix [prefix]",
                              description="Changes the server-wide prefix to the given prefix. \n\nExample: ``!prefix $``",
                              color=0x000000)
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
        embed = discord.Embed(title="!avatarid [id]",
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
        embed = discord.Embed(title="!unmute [user]",
                              description="Unmutes the user you gave.\n\nExample: ``!unmute @Shiki``",
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
