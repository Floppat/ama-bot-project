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
