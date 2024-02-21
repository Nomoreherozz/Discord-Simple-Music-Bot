import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='/', intents = discord.Intents.all())


for i in range(len(cogs)):
    cogs[i].setup(client)

client.run("OTI5ODI4MDE5MzExMzUzODY2.Yds_0w.tUDQKW00cIcks145Ba8F5DzYxgI")