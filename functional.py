import discord

from config import database
from db import DB_Manager


db = DB_Manager(database)
db.create_tables()


def plus_xp(interaction: discord.Interaction):
    db.change('users',interaction.user.id,'xp',int,db.read('users',interaction.user.id,'xp')[0]+1)

def change_status(interaction: discord.Interaction, status_id: int, user_tag: int):
    if int(db.read('users',interaction.user.id,'status_id')[0]) == 2:
        return db.change('users',db.get_PK('users','tag',user_tag,str)[0],'status_id',int,status_id)
    else:
        return 'недостаточно прав чтобы выполнить'
    
def delete_user(interaction: discord.Interaction, user_tag: int):
    if int(db.read('users',interaction.user.id,'status_id')[0]) == 2:
        return db.delete('users',db.get_PK('users','tag',user_tag,str)[0])
    else:
        return 'недостаточно прав чтобы выполнить'


async def fetch_args(command: str, source: str) -> list[str]:
    return source.removeprefix(command).strip().split()
