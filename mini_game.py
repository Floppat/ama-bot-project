# imports-----------------------------------------------------------------------------------
import discord
from discord.ext import commands

# file-imports------------------------------------------------------------------------------
from functional import register, get_user

# functions---------------------------------------------------------------------------------
async def mini_game_cmd(ctx: commands.Context) -> None:
    await ctx.send('попробуйте  /register     (после регистрации доступны все команды)\n'
                   'попробуйте  /prehistory   (предистория, немного сюжета)\n'
                   'попробуйте  /guide        (ввод в игру)\n'
                   'попробуйте  /train        (+сила; -здоровье; -выносливость)\n'
                   'попробуйте  /feed         (+здоровье; +выносливость)\n'
                   'попробуйте  /sleep        (полное восстановление выносливости)\n'
                   'попробуйте  /attack       (-здоровье (ведь это же битва))\n'
                   'попробуйте  /shop         (покупка артефактов)\n'
                   'попробуйте  !cmd_game')

async def mini_game_prehistory(interaction: discord.Interaction) -> None:
    message =  ('давным-давно люди жили в мире с природой и животными...\n'
                'но не так давно, всего каких два века назад, люди забыли свою историю и начали загрязнять природу всё сильнее...\n'
                'это породило маленьких монстров - Карков\n'
                'Карки хотят уничтожить всю жизнь на земле, и нагревают её, и не остановятся пока земля не превратится в большую печку!\n'
                'спасите планету - победите всех Карков. но... проблема в том что люди не видят Карков... как же быть? природа поможет! \n' 
                'Ваш питомец - возможно единственный в своём роде, может остановить Карков! тренируёте его и спасите землю от Карков!\n')
    await interaction.response.send_message(message)

async def mini_game_guide(interaction: discord.Interaction) -> None:
    message =  ('чтобы играть, прежде надо зарегестрироватся\n'
                'каждый день (до использования команды /sleep) вы можете 2 раза потренироватся, затем 1 раз поесть.\n'
                'за день можно 2 раза потренироватся, или 1 раз потренироватся и 1 раз подратся\n'
                'совет: лучше перед боем не тренероватся, ведь будет меньше здоровья, а поесть вы не сможете\n'
                'тактика про: каждый день 2 раза тренироваться и 1 раз есть, после того как набралось 10 атаки на следущий день идти в бой\n' 
                'также противник становится сильнее не по дням, а по боям, так что покупайте артефакты, ведь они повышают защиту\n')
    await interaction.response.send_message(message)

async def mini_game_train(interaction: discord.Interaction):
    user = await get_user(user_id=interaction.user.id)
    if not user:
        await register(interaction = interaction)
        user = await get_user(user_id=interaction.user.id)
    await user.train(interaction=interaction)

async def mini_game_feed(interaction: discord.Interaction):
    user = await get_user(user_id=interaction.user.id)
    if not user:
        await register(interaction = interaction)
        user = await get_user(user_id=interaction.user.id)
    await user.feed(interaction=interaction)

async def mini_game_attack(interaction: discord.Interaction):
    user = await get_user(user_id=interaction.user.id)
    if not user:
        await register(interaction = interaction)
        user = await get_user(user_id=interaction.user.id)
    await user.attack(interaction=interaction)

async def mini_game_sleep(interaction: discord.Interaction):
    user = await get_user(user_id=interaction.user.id)
    if not user:
        await register(interaction = interaction)
        user = await get_user(user_id=interaction.user.id)
    await user.sleep(interaction=interaction)

async def mini_game_shop(interaction: discord.Interaction, item: str):
    user = await get_user(user_id=interaction.user.id)
    if not user:
        await register(interaction = interaction)
        user = await get_user(user_id=interaction.user.id)
    await user.shop(interaction=interaction, item=item)
