from highrise.models import CurrencyItem, Item, User
from config.config import loggers


async def on_tip(bot, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
    if loggers.tips:
        print(f"{sender.username} enviou uma gorgeta para {receiver.username} {tip.amount} {tip.type}!")
    await bot.highrise.chat(f"{sender.username} enviou uma gorgeta para {receiver.username} {tip.amount} {tip.type} 😎!")
