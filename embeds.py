# imports-----------------------------------------------------------------------------------
import discord

# basic commands----------------------------------------------------------------------------
bcmd = discord.Embed(
    title='Команды',
    description='все команды бота в одном месте!',
    color=discord.Colour.from_rgb(100, 200, 90))
bcmd.add_field(
    name='Команды мини-игры',
    value='''попробуйте '/register'
             попробуйте '/prehistory'
             попробуйте '/guide'
             попробуйте '/train'
             попробуйте '/feed'
             попробуйте '/sleep'
             попробуйте '/attack'
             попробуйте '/shop'
             попробуйте '!cmd_game'
             (подробнее о командах игры)''')
bcmd.add_field(
    name='Команды глобального потепления',
    value='''попробуйте '!about'
             попробуйте '!reasons'
             попробуйте '!how_help'
             попробуйте '/quiz'
             попробуйте '!cmd_warming'
             (подробнее о командах о потеплении)''')

# global warming embeds-------------------------------------------------------------------
eq1 = discord.Embed(
    title='Первый вопрос',
    description='нажмите кнопку с правильным ответом',
    color=discord.Colour.from_rgb(100, 200, 90))
eq1.add_field(
    name='Что из нижеперичисленного главная и основная причина глобального потепления?',
    value='''A: парниковый эффект
             B: человеческая деятельность
             C: ледники тают''')

eq2 = discord.Embed(
    title='Второй вопрос',
    description='нажмите кнопку с правильным ответом',
    color=discord.Colour.from_rgb(100, 200, 90))
eq2.add_field(
    name='Что из нижеперичисленного главная и основная причина того, что глобальное потепление сложно остановить/замедлить?',
    value='''A: процесс перехода на альтернативные источники энергии очень долгий
             B: невыгодно переходить на альтернативные источники энергии 
             C: невозможно перейти на альтернативные источники питания''')

eq3 = discord.Embed(
    title='Третий вопрос',
    description='нажмите кнопку с правильным ответом',
    color=discord.Colour.from_rgb(100, 200, 90))
eq3.add_field(
    name='Что простой человек может сделать чтобы внести вклад в замедление глобального потепления?',
    value='''A: покупать специальные товары
             B: пользоваться общевственным транспортом или приобрести электрокар
             C: не пользоваться электричевством''')

eq4 = discord.Embed(
    title='Четвёртый вопрос',
    description='нажмите кнопку с правильным ответом',
    color=discord.Colour.from_rgb(100, 200, 90))
eq4.add_field(
    name='Что из нижеперичисленного является парниковым газом?',
    value='''A: Ag
             B: O2
             C: CO2''')

eq5 = discord.Embed(
    title='Пятый вопрос',
    description='нажмите кнопку с правильным ответом',
    color=discord.Colour.from_rgb(100, 200, 90))
eq5.add_field(
    name='Что именно стимулирует повышение концентрации парникового газа в атмосфере?',
    value='''A: Вырубка лесов и промышленное производство
             B: машины
             C: из за перенаселения планета не справляется с количевством выдыхаемого людми углекислого газа''')
