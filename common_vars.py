from discord.ext.commands import Bot
import http.client

bot = Bot(command_prefix='!')

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
