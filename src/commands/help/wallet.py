from highrise import User


class Command:
    def __init__(self, bot):
        self.bot = bot
        self.name = "wallet"
        self.description = "Check the bot's wallet"
        self.cooldown = 5

    async def execute(self, user: User, args: list, message: str):
        wallet = await self.bot.highrise.get_wallet()
        for item in wallet.content:
            if item.type == "gold":
                gold = item.amount
                await self.bot.highrise.chat(f"Hello, {user.username}! My current balance is {gold} gold!")
                return
        await self.bot.highrise.chat(f"Hello, {user.username}! I don't have any gold.")
