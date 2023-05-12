from highrise.models import User
from config.config import loggers


async def on_emote(bot, user: User, emote_id: str, receiver: User) -> None:
    if loggers.emotes:
        print(f"User {user.username} sent {emote_id} to {receiver.username}")
