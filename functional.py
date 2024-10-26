# imports-----------------------------------------------------------------------------------
import discord

# file-imports------------------------------------------------------------------------------
from users import User

# functional--------------------------------------------------------------------------------
users_database = list()

async def get_user(user_id: int) -> User | None:
    for user in users_database:
        if user_id == user.user_id:
            return user
    return None

async def register(interaction: discord.Interaction) -> None:
    users_database.append(
        User(user_id=interaction.user.id, user_nickname=interaction.user.nick)
    )

async def change(interaction: discord.Interaction, new_nick: str, user_id: int):
    for user in users_database:
        if user_id == user.user_id:
            user.nickname=new_nick



#@bot.command('info')
#async def info(ctx: commands.Context):
#    embed = discord.Embed(
#        title='Информация о боте',
#        description='Бот создан для помощи в решении задачи "Защита от глобального потепления"',
#        color=discord.Colour.from_rgb(255, 0, 0)
#    )
#    await ctx.send(embed=embed)
#@bot.command('photo')
#async def photo(ctx: commands.Context):
#    await ctx.send(file=discord.File('photo.jpg'))

#создать словарь и добавлять туда 'dict[id] = []' 'dict[id].append(True)'

#await ctx.send('ohoho rules from evil daddy', embeds=[embed, embed1])