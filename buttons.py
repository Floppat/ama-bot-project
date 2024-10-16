# imports----------------------------------------------------------------------------------
import discord

# file-imports-----------------------------------------------------------------------------
from embeds import eq2,eq3,eq4,eq5

# global warming buttons-------------------------------------------------------------------
#создать словарь и добавлять туда 'dict[id] = []' 'dict[id].append(True)'
#await ctx.send('ohoho rules from evil daddy', embeds=[embed, embed1])
class bq1(discord.ui.View):
    def __init__(self, *, timeout = 180, user: int):
        super().__init__(timeout=timeout)
        self.user = user

    @discord.ui.button(label='A', style=discord.ButtonStyle.secondary)
    async def bq11(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="Неправильный ответ. правильный ответ  был: B", embed=eq2, view=bq2(user=self.user))

    @discord.ui.button(label='B', style=discord.ButtonStyle.secondary)
    async def bq12(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.user.right_answer()
        await interaction.response.edit_message(content="Правильный ответ!", embed=eq2, view=bq2(user=self.user))

    @discord.ui.button(label='C', style=discord.ButtonStyle.secondary)
    async def bq13(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="Неправильный ответ. правильный ответ был: B", embed=eq2, view=bq2(user=self.user))
    
    @discord.ui.button(label='закончить', style=discord.ButtonStyle.danger)
    async def end1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.user.quizresult(interaction=interaction, cancel = True)



class bq2(discord.ui.View):
    def __init__(self, *, timeout = 180, user: int):
        super().__init__(timeout=timeout)
        self.user = user

    @discord.ui.button(label='A', style=discord.ButtonStyle.secondary)
    async def bq21(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.user.right_answer()
        await interaction.response.edit_message(content="Правильный ответ!", embed=eq3, view=bq3(user=self.user))

    @discord.ui.button(label='B', style=discord.ButtonStyle.secondary)
    async def bq22(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="Неправильный ответ. правильный ответ был: А", embed=eq3, view=bq3(user=self.user))

    @discord.ui.button(label='C', style=discord.ButtonStyle.secondary)
    async def bq23(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="Неправильный ответ. правильный ответ был: А", embed=eq3, view=bq3(user=self.user))

    @discord.ui.button(label='закончить', style=discord.ButtonStyle.danger)
    async def end2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.user.quizresult(interaction=interaction, cancel = True)



class bq3(discord.ui.View):
    def __init__(self, *, timeout = 180, user: int):
        super().__init__(timeout=timeout)
        self.user = user

    @discord.ui.button(label='A', style=discord.ButtonStyle.secondary)
    async def bq31(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="Неправильный ответ. правильный ответ  был: B", embed=eq4, view=bq4(user=self.user))

    @discord.ui.button(label='B', style=discord.ButtonStyle.secondary)
    async def bq32(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.user.right_answer()
        await interaction.response.edit_message(content="Правильный ответ!", embed=eq4, view=bq4(user=self.user))

    @discord.ui.button(label='C', style=discord.ButtonStyle.secondary)
    async def bq33(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="Неправильный ответ. правильный ответ  был: B", embed=eq4, view=bq4(user=self.user))

    @discord.ui.button(label='закончить', style=discord.ButtonStyle.danger)
    async def end3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.user.quizresult(interaction=interaction, cancel = True)



class bq4(discord.ui.View):
    def __init__(self, *, timeout = 180, user: int):
        super().__init__(timeout=timeout)
        self.user = user

    @discord.ui.button(label='A', style=discord.ButtonStyle.secondary)
    async def bq41(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="Неправильный ответ. правильный ответ был: C", embed=eq5, view=bq5(user=self.user))

    @discord.ui.button(label='B', style=discord.ButtonStyle.secondary)
    async def bq42(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="Неправильный ответ. правильный ответ был: C", embed=eq5, view=bq5(user=self.user))

    @discord.ui.button(label='C', style=discord.ButtonStyle.secondary)
    async def bq43(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.user.right_answer()
        await interaction.response.edit_message(content="Правильный ответ!", embed=eq5, view=bq5(user=self.user))

    @discord.ui.button(label='закончить', style=discord.ButtonStyle.danger)
    async def end4(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.user.quizresult(interaction=interaction, cancel = True)



class bq5(discord.ui.View):
    def __init__(self, *, timeout = 180, user: int):
        super().__init__(timeout=timeout)
        self.user = user

    @discord.ui.button(label='A', style=discord.ButtonStyle.secondary)
    async def bq51(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.user.right_answer()
        await self.user.quizresult(interaction=interaction, cancel=False)

    @discord.ui.button(label='B', style=discord.ButtonStyle.secondary)
    async def bq52(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.user.quizresult(interaction=interaction, cancel=False)

    @discord.ui.button(label='C', style=discord.ButtonStyle.secondary)
    async def bq53(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.user.quizresult(interaction=interaction, cancel=False)