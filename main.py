import discord
import random
import os
from discord.ext import commands
import requests
import bot_mantik
import math

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} giriş yaptı")

@bot.command()
async def film_öner(ctx):
    await ctx.send(bot_mantik.film_öner())

@bot.command()
async def dizi_öner(ctx):
    await ctx.send(bot_mantik.dizi_öner())

@bot.command()
async def faktoriyel(ctx, number: int):
    if number < 0:
        await ctx.send("Negatif sayıların faktöriyeli hesaplanamaz.")
    else:
        result = math.factorial(number)
        await ctx.send(f"{number}! = {result}")

@bot.command()
async def şifre_oluştur(ctx):
    await ctx.send(bot_mantik.sifre_olusturucu())

@bot.command()
async def yazımı_turamı(ctx):
    await ctx.send(bot_mantik.yazi_tura())

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

@bot.event
async def on_member_join(member):
    welcome_message = f"Selamun Aleyküm {member.name}! Sunucumuza hoş geldin!"
    channel = discord.utils.get(member.guild.channels, name='general')

    print(f"{member.name} sunucuya katıldı!")
    await member.send(welcome_message)
    if channel:
        await channel.send(welcome_message)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_fox_image_url():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

@bot.command()
async def fox(ctx):
    image_url = get_fox_image_url()
    await ctx.send(image_url)

@bot.command()
async def mem_oran(ctx):
    olasiliklar = [0.1, 0.3, 0.5]
    img_name = random.choices(os.listdir('picture'), weights=olasiliklar, k=1)[0]
    with open(f'picture/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def random_pokemon(ctx):
    random_pokemon_id = random.randint(1, 800)
    url = f'https://pokeapi.co/api/v2/pokemon/{random_pokemon_id}'
    res = requests.get(url)
    data = res.json()
    image_url = data['sprites']['front_default']
    await ctx.send(data["forms"][0]["name"])
    await ctx.send(image_url)

@bot.command()
async def pokemon(ctx, pokemon_name="charmander"):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        image_url = data['sprites']['front_default']
        await ctx.send(image_url)
    else:
        await ctx.send(f"{pokemon_name} adında bir Pokemon bulunamadı.")

bot.run("YOUR BOT'S TOKEN")
