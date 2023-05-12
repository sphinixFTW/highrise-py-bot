from highrise import User
from config.config import config


class Command:
    def __init__(self, bot):
        self.bot = bot
        self.name = "say"
        self.description = "Give the bot a prompt to say"
        self.permissions = ["say"]
        self.aliases = ['speak', 'talk']
        self.cooldown = 1

    async def execute(self, user: User, args: list, message: str):
        prefix = config.prefix
        text = message.replace(f"{prefix}say", "").strip()
        await self.bot.highrise.chat(text)
