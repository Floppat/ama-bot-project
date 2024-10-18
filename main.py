# imports-----------------------------------------------------------------------------------
import discord
from discord.ext import commands

# file-imports------------------------------------------------------------------------------
from mini_game      import *
from global_warming import *
from embeds import bcmd

# bot settings------------------------------------------------------------------------------
bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

# event function----------------------------------------------------------------------------
@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} готов.')
    synced = await bot.tree.sync()
    print(f'{len(synced)} / команды доступны.')

# basic commands----------------------------------------------------------------------------
@bot.tree.command(name='cmd', description='все команды бота')
async def cmd(interaction: discord.Interaction) -> None:
        await interaction.response.send_message(embed=bcmd)

# mini-game commands------------------------------------------------------------------------
@bot.command('cmd_game')
async def cmd_game(ctx: commands.Context):
    await mini_game_cmd(ctx)
@bot.tree.command(name='prehistory', description='ура сюжет')
async def prehistory(interaction: discord.Interaction) -> None:
    await mini_game_prehistory(interaction)

@bot.tree.command(name='guide', description='Отображает справку по игре')
async def guide(interaction: discord.Interaction) -> None:
    await mini_game_guide(interaction)

@bot.tree.command(name='register', description='Позволяет зарегистрироваться в игре')
async def register(interaction: discord.Interaction, nickname: str) -> None:
    await mini_game_register(interaction, nickname)

@bot.tree.command(name='train', description='Потренируйте питомца!')
async def train(interaction: discord.Interaction) -> None:
    await mini_game_train(interaction)

@bot.tree.command(name='feed', description='Покормите питомца!')
async def feed(interaction: discord.Interaction) -> None:
    await mini_game_feed(interaction)

@bot.tree.command(name='attack', description=' Настало время драки!')
async def attack(interaction: discord.Interaction) -> None:
    await mini_game_attack(interaction)

@bot.tree.command(name='sleep', description='У-устал')
async def sleep(interaction: discord.Interaction) -> None:
    await mini_game_sleep(interaction)

@bot.tree.command(name='shop', description='Напишите ? или help если не знаете ассортимент')
async def shop(interaction: discord.Interaction, item: str) -> None:
    await mini_game_shop(interaction, item)

@bot.tree.command(name='goofyahh', description='супер важная секретная команда')
async def goofyahh(interaction: discord.Interaction) -> None:
    await mini_game_goofyahh(interaction)

# global warming commands-------------------------------------------------------------------
@bot.command('cmd_warming')
async def cmd_warming(ctx: commands.Context) -> None:
    await global_warming_cmd(ctx)
@bot.command('about')
async def about(ctx: commands.Context) -> None:
    await global_warming_about(ctx)

@bot.command('reasons')
async def reasons(ctx: commands.Context) -> None:
    await global_warming_reasons(ctx)

@bot.command('how_help')
async def how_help(ctx: commands.Context) -> None:
    await global_warming_how_help(ctx)

@bot.tree.command(name='quiz', description='небольшая викторина о глобальном потеплении')
async def quiz(ctx: commands.Context):
    await global_warming_quiz(ctx)


# bot run-----------------------------------------------------------------------------------
bot.run('')
