from highrise.models import User
from config.config import loggers, config


async def on_whisper(bot, user: User, message: str) -> None:
    if loggers.whispers:
        print(f"(whisper) {user.username}: {message}")
    if message.lstrip().startswith(config.prefix):
        await bot.command_handler.handle_command(user, message)
