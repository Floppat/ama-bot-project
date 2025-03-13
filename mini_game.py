import discord
from discord.ext import commands

from users import registred, get_other_user


async def cmd(ctx: commands.Context) -> None:
    await ctx.send( '/change_nick       (изменяет ник который будет отображатся лидербордах)\n'
                    '/change_pet_name   (изменяет имя питомца)\n'
                    '/leaderboard       (entity= users/pets ; page= номер страницы ; \n'
                    'для users: tag/username/coins/quiz_record/xp , для pets: pet_name/str/xp\n'
                    '/prehistory        (предистория, немного сюжета)\n'
                    '/guide             (ввод в игру)\n'
                    '/me                (данные о вас как о пользователе амы)\n'
                    '/stats             (хар-ки вашего питомца)\n'
                    '/train             (+сила; -здоровье; -выносливость)\n'
                    '/feed              (+здоровье; +выносливость)\n'
                    '/sleep             (полное восстановление выносливости)\n'
                    '/attack            (-здоровье (ведь это же битва))\n'
                    '/shop              (покупка артефактов)\n'
                    '!cmd_game')

async def prehistory(interaction: discord.Interaction) -> None:
    registred(interaction=interaction)
    message =  ('давным-давно люди жили в мире с природой и животными...\n'
                'но не так давно, всего каких два века назад, люди забыли свою историю и начали загрязнять природу всё сильнее...\n'
                'это породило маленьких монстров - Карков\n'
                'Карки хотят уничтожить всю жизнь на земле, и нагревают её, и не остановятся пока земля не превратится в большую печку!\n'
                'спасите планету - победите всех Карков. но... проблема в том что люди не видят Карков... как же быть? природа поможет! \n' 
                'Ваш питомец - возможно единственный в своём роде, может остановить Карков! тренируёте его и спасите землю от Карков!\n')
    await interaction.response.send_message(message)

async def guide(interaction: discord.Interaction) -> None:
    registred(interaction=interaction)
    message =  ('чтобы играть, прежде надо зарегестрироватся\n'
                'каждый день (до использования команды /sleep) вы можете 2 раза потренироватся, затем 1 раз поесть.\n'
                'за день можно 2 раза потренироватся, или 1 раз потренироватся и 1 раз подратся\n'
                'совет: лучше перед боем не тренероватся, ведь будет меньше здоровья, а поесть вы не сможете\n'
                'тактика про: каждый день 2 раза тренироваться и 1 раз есть, после того как набралось 10 атаки на следущий день идти в бой\n' 
                'также противник становится сильнее не по дням, а по боям, так что покупайте артефакты, ведь они повышают защиту\n'
                'важно: руководство для новичков и после покупки первого артефакта численные данные становятся неактуальны\n')
    await interaction.response.send_message(message)


async def user(interaction: discord.Interaction, user_tag: str):
    user = registred(interaction=interaction)
    if user_tag == 'me':
        await interaction.response.send_message(f'{user}')
    else:
        await interaction.response.send_message(get_other_user(user_tag=user_tag))

async def stats(interaction: discord.Interaction):
    user = registred(interaction=interaction)
    await interaction.response.send_message(f'{user.pet}')

async def train(interaction: discord.Interaction):
    user = registred(interaction=interaction)
    await user.train(interaction=interaction)

async def feed(interaction: discord.Interaction):
    user = registred(interaction=interaction)
    await user.feed(interaction=interaction)

async def attack(interaction: discord.Interaction):
    user = registred(interaction=interaction)
    await user.attack(interaction=interaction)

async def sleep(interaction: discord.Interaction):
    user = registred(interaction=interaction)
    await user.sleep(interaction=interaction)

async def shop(interaction: discord.Interaction, item: str):
    user = registred(interaction=interaction)
    await user.shop(interaction=interaction, item=item)
