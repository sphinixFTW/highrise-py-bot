from highrise.models import User, Reaction
from config.config import loggers


async def on_reaction(bot, user: User, reaction: Reaction, receiver: User) -> None:
    if loggers.reactions:
        print(f"{user.username} send {reaction} to {receiver.username}")
