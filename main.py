import time

import discord
import feedparser
from discord.ext import commands
from discord.ext import tasks
import  asyncio

intens = discord.Intents.all()
client = commands.Bot(command_prefix="?", intents=intens)
clientd = discord.Client(intents=intens)


@client.event
async def on_ready():

  MyChannel = client.get_channel(998911817571123290)
  espi = feedparser.parse("https://biznes.pap.pl/pl/rss/6614")
  for post in espi.entries:
   if 'LONGTERM' in post.title:
         embed = discord.Embed(title=post.title, url=post.link, description="", color=discord.Color.red())
         await MyChannel.send(embed=embed)





client.run('OTM0NTc0NTU3NDEzNjcwOTYy.GhExPD.zLZTLfeb0KjEuY4RtIkm6gMaKXwiKR5spa4coo')








