from discord.ext.commands import Bot
from discord.ext import commands
import discord
import http.client
import requests
import json

async def get_prefix(bot, message):
    for key, value in serverPrefixes.items():
        if int(key) == message.guild.id:
            return value
    return "!"

bot = commands.Bot(command_prefix=get_prefix)

afklist = {}

remindersdm = []
remindersserver = []

conn = http.client.HTTPSConnection("mashape-community-urban-dictionary.p.rapidapi.com")

tosnipe = {}
tosnipeauthors = {}
tosnipetime = {}

toeditsnipe = {}
toeditsnipeauthors = {}
toeditsnipetime = {}

msgsCounterr = 0
msgsCounterrr = 0
allTimeMessages = 0

#storage = 0
#storagePrefix = 0
serverPrefixes = {}
serverPrefixesToDelete = {}

starboardChannels = {}

async def convert_color_menu(role_number: str):
    if role_number == "1":
        return "Light Red"
    elif role_number == "2":
        return "Light Orange"
    elif role_number == "3":
        return "Light Purple"
    elif role_number == "4":
        return "Light Yellow"
    elif role_number == "5":
        return "Light Cyan"
    elif role_number == "6":
        return "Light Blue"
    elif role_number == "7":
        return "Light Green"
    elif role_number == "8":
        return "Light Pink"
    elif role_number == "9":
        return "Dark Red"
    elif role_number == "10":
        return "Dark Blue"
    elif role_number == "11":
        return "Dark Purple"
    elif role_number == "12":
        return "Dark Pink"
    elif role_number == "13":
        return "Crimson"
    elif role_number == "14":
        return "Black"
    elif role_number == "15":
        return "Gray"
    elif role_number == "16":
        return "Indigo"
    elif role_number == "17":
        return "Lavender"
    elif role_number == "18":
        return "Violet"
    elif role_number == "19":
        return "White"
    elif role_number == "20":
        return "Magenta"
    elif role_number == "21":
        return "Cream"
    else:
        return "none"

async def guildConvert(arg):
    try:
        guild = bot.get_guild(int(arg))
        if guild is None:
            return None
        else:
            return guild
    except ValueError:
        guild = discord.utils.get(bot.guilds, name="{}".format(arg))
        if guild is None:
            return None
        else:
            return guild

tenorkey = "6JKJQX4V4OHD"
limit = 50
media_filter = "basic"
kiss = "animekiss"
hug = "animehug"
slap = "animeslap"
cuddle = "animecuddle"
blush = "animeblush"
pat = "animepat"
facepalm = "animefacepalm"
poke = "animepoke"

kissgifs = requests.get(
    "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (kiss, tenorkey, limit, media_filter))
huggifs = requests.get(
    "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (hug, tenorkey, limit, media_filter))
slapgifs = requests.get(
    "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (slap, tenorkey, limit, media_filter))
cuddlegifs = requests.get(
    "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (cuddle, tenorkey, limit, media_filter))
blushgifs = requests.get(
    "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (blush, tenorkey, limit, media_filter))
patgifs = requests.get(
    "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (pat, tenorkey, limit, media_filter))
facepalmgifs = requests.get(
    "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (facepalm, tenorkey, limit, media_filter))
pokegifs = requests.get(
    "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&media_filter=%s" % (poke, tenorkey, limit, media_filter))


kiss_gifs = json.loads(kissgifs.content)
hug_gifs = json.loads(huggifs.content)
slap_gifs = json.loads(slapgifs.content)
cuddle_gifs = json.loads(cuddlegifs.content)
blush_gifs = json.loads(blushgifs.content)
pat_gifs = json.loads(patgifs.content)
facepalm_gifs = json.loads(facepalmgifs.content)
poke_gifs = json.loads(pokegifs.content) 

async def parse_roles(ctx, role: str):
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
