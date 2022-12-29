import discord
import requests
from bs4 import BeautifulSoup
from classExcel import gymTracker


bot = discord.Bot(command_prefix='$')
servers = [502251789731627028]
username = "Tubby#0124"

back = ['Pull Machine', 'Row Machine', 'Inverted Fly Machine', 'Hammer Curls', 'Wrist']
leg = ['seated leg press', 'leg extent', 'leg curl', 'pedal push', 'squats']
chest = ['dumbbell press', 'incline dumbbell press', 'Fly Machine', 'Trisepts Pull', 'Push Up']


tracker = gymTracker()

#a quick starter function
@bot.event
async def on_ready():
    await bot.change_presence(
        activity= discord.Activity(
            name = "HAS STARTED UP!"
        )
    )
    print('Bot is ready')

#grabs the data from modal
class MyChestModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for i in range(5):
          self.add_item(discord.ui.InputText(label=chest[i]))

    async def callback(self, interaction: discord.Interaction):
        chestList = []
        embed = discord.Embed(title="Modal Results")
        for i in range(5):
          embed.add_field(name=chest[i], value=self.children[i].value)
          chestList.append(self.children[i].value)
        await interaction.response.send_message(embeds=[embed])
        tracker.inputChest(chestList)

class MyBackModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for i in range(5):
          self.add_item(discord.ui.InputText(label=back[i]))

    async def callback(self, interaction: discord.Interaction):
        backList = []
        embed = discord.Embed(title="Modal Results")
        for i in range(5):
          embed.add_field(name=back[i], value=self.children[i].value)
          backList.append(self.children[i].value)
        await interaction.response.send_message(embeds=[embed])
        tracker.inputBack(backList)
        tracker.displayStat()

class MyLegModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        for i in range(5):
          self.add_item(discord.ui.InputText(label=leg[i]))

    async def callback(self, interaction: discord.Interaction):
        legList = []
        embed = discord.Embed(title="Modal Results")
        for i in range(5):
          embed.add_field(name=leg[i], value=self.children[i].value)
          legList.append(self.children[i].value)
        await interaction.response.send_message(embeds=[embed])
        tracker.inputLeg(legList)
#calls the modal functions
@bot.slash_command()
async def modal_chest(ctx: discord.ApplicationContext):
    """Save data on chest day!"""
    modal = MyChestModal(title="Modal via Slash Command")
    await ctx.send_modal(modal)

@bot.slash_command()
async def modal_back(ctx: discord.ApplicationContext):
    """Save data on back day!"""
    modal = MyBackModal(title="Modal via Slash Command")
    await ctx.send_modal(modal)

@bot.slash_command()
async def modal_leg(ctx: discord.ApplicationContext):
    """Save data on leg day!"""
    modal = MyLegModal(title="Modal via Slash Command")
    await ctx.send_modal(modal)



#scraps top 5 reddit post...
@bot.slash_command()
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



from scripts.methods_ import move_images, openAiReponse

image_types = ["png", "jpeg", "gif", "jpg"]
school_bin = 'C:/Users/andys/Desktop/DISCORD IMPORT/schoo l_photos'

@bot.event
async def on_message(message):
#checks if any files are images and saves them into a folder on my desktop
    self = await bot.fetch_user(221336351478513664)
    for attachment in message.attachments:
        if any(attachment.filename.lower().endswith(image) for image in image_types):
            embedVar = discord.Embed(title="Processed", color=0x00ff00)
            await attachment.save(attachment.filename)
            move_images(image_types)
            await message.channel.send(embed= embedVar)

#returns an openai reponse assistant ina sense
    if str(message.author) == "Tubby#0124":
        response = openAiReponse(message.content).strip()
        print(response)
        if "code" in message.content:
            await self.send("```\n {} \n```".format(response))
        else:
            await self.send(response)


bot.run('OTEzMzE2NDk1MzczNzk1MzQ5.GWW7cC.UhPjCYpu4fVHIuKYROjeCPIXgziTAXjY4fgyOA')



