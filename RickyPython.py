import random
import discord
from discord.ext import commands
import aiohttp
import json

intents = discord.Intents.all()
intents.typing = True
intents.presences = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, World!')

@bot.command(name='location', help = "Provides location information for a location in the series")
async def get_rick_and_morty_location(ctx, location_id: int):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f'https://rickandmortyapi.com/api/location/{location_id}') as response:
                if response.status == 200:
                    location_data = await response.text()
                    location_data = json.loads(location_data)

                    embed = discord.Embed(
                        title="Location Information",
                        description="Here's some information about the location:",
                        color=0x00FF00  # Green color
                    )

                    embed.add_field(name="Name", value=location_data['name'])
                    embed.add_field(name="Type", value=location_data['type'])
                    embed.add_field(name="Dimension", value=location_data['dimension'])

                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"Error: {response.status} - {response.reason}")
        except Exception as ex:
            await ctx.send(f"Error: {ex}")



@bot.command(name='episode', help = "Provides episode information for a episode in the series ")
async def get_rick_and_morty_episode(ctx, episode_id: int):
    api_url = f"https://rickandmortyapi.com/api/episode/{episode_id}"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(api_url) as response:
                if response.status == 200:
                    episode_data = await response.json()

                    name = episode_data['name']
                    air_date = episode_data['air_date']
                    episode_code = episode_data['episode']

                    embed = discord.Embed(
                        title="Episode Information",
                        description="Here's some information about the episode:",
                        color=0x00FF00  # Green color
                    )

                    embed.add_field(name="Name", value=name)
                    embed.add_field(name="Air Date", value=air_date)
                    embed.add_field(name="Episode Code", value=episode_code)

                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"Error: {response.status} - {response.reason}")
        except aiohttp.ClientError:
            await ctx.send("An error occurred while making the HTTP request. Please try again later.")
        except json.JSONDecodeError:
            await ctx.send("An error occurred while parsing the API response. Please try again later.")
        except Exception as ex:
            await ctx.send(f"An unexpected error occurred: {ex}")



@bot.command(name='character', help = "Provides charcter information for a character ")
async def get_rick_and_morty_character(ctx, character_id: int):
    if character_id < 1 or character_id > MaxCharacterId:
        await ctx.send("Invalid character ID. Please enter a valid character ID.")
        return

    api_url = f"https://rickandmortyapi.com/api/character/{character_id}"
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(api_url) as response:
                if response.status == 200:
                    character_data = await response.json()

                    name = character_data['name']
                    status = character_data['status']
                    species = character_data['species']
                    image = character_data['image']

                    embed = discord.Embed(
                        title="Character Information",
                        description="Here's some information about the character:",
                        color=0x00FF00  # Green color
                    )

                    embed.add_field(name="Name", value=name)
                    embed.add_field(name="Status", value=status)
                    embed.add_field(name="Species", value=species)
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"Error: {response.status} - {response.reason}")
        except aiohttp.ClientError:
            await ctx.send("An error occurred while making the HTTP request. Please try again later.")
        except json.JSONDecodeError:
            await ctx.send("An error occurred while parsing the API response. Please try again later.")
        except Exception as ex:
            await ctx.send(f"An unexpected error occurred: {ex}")


MaxCharacterId = 826

@bot.command(name='Rchar', help = "Provides a random character from the show")
async def get_random_character(ctx):
    random_character_id = random.randint(1, 826) 
    await bot.get_command("character").callback(ctx, character_id=random_character_id)


@bot.command(name='Rloca', help = "Provides a random location from the show")
async def get_random_character(ctx):
    random_location_id = random.randint(1, 108) 
    await bot.get_command("location").callback(ctx, location_id=random_location_id)

@bot.command(name='Repi', help = "Provides a random episode from the show")
async def get_random_character(ctx):
    random_episode_id = random.randint(1, 41) 
    await bot.get_command("episode").callback(ctx, episode_id=random_episode_id)



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return

    print(f'An error occurred: {error}')

token = "MTE2NDYwNzAyNzczNDExODUxMA.GJWt-X.HeHqx_hzLeBDUhi1_h4BxrqQVw6bZYleDKkofI" 
bot.run(token)


