from highrise import User


class Command:
    def __init__(self, bot):
        self.bot = bot
        self.name = 'test'
        self.description = "Your command description"
        self.cooldown = 5

    async def execute(self, user: User, args: list, message: str):
        # now notice that we used self.bot.highrise and not self.highrise, keep this in mind
        await self.bot.highrise.chat('this is a test')
        # now you can use this template for all commands just copy and paste it
        # now i removed the permissions and the aliases so i can show u how it work without both ..
