
import discord
from discord.ext import commands
import discord.client 

import requests
from bs4 import BeautifulSoup

from scripts.methods_ import move_images

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    await client.change_presence(
        activity= discord.Activity(
            name = "HAS STARTED UP!"
        )
    )
    self = await client.fetch_user(221336351478513664)
    await self.send("Hello Andy!")
    print('Bot is ready')

image_types = ["png", "jpeg", "gif", "jpg"]

school_bin = 'C:/Users/andys/Desktop/DISCORD IMPORT/school_photos'

@client.event
async def on_message(message):
    embedVar = discord.Embed(title="Processed", color=0x00ff00)
    for attachment in message.attachments:
        if any(attachment.filename.lower().endswith(image) for image in image_types):
            await attachment.save(attachment.filename)
            move_images(image_types)
            await message.channel.send(embed= embedVar)
    await client.process_commands(message)

@client.command()
async def test(ctx):
    await ctx.send('test')

@client.command()
async def news(ctx):
    print('triggered')
    headers = {'User-Agent': 'Mozilla/5.0'}

    link = 'https://old.reddit.com/r/worldnews/'

    res = requests.get(link, headers=headers)
    html_page = res.content

    soup = BeautifulSoup(html_page, 'html.parser')

    reddit_post = soup.find_all('div', class_ = 'top-matter', limit=5)

    for post in reddit_post[:]:
        if len(post.p.a.attrs['href']) > 500:
            reddit_post.remove(post)
        else:
            continue

    embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
    for post in reddit_post:
        title = post.p.a.text
        link = post.p.a.attrs['href']
        embedVar.add_field(name=title, value=link, inline=False)
    await ctx.author.send(embed=embedVar)
    
client.run('OTEzMzE2NDk1MzczNzk1MzQ5.YZ8uRQ.Rl5EPXl84GMWJIFTBfrEnW_E-mU')



