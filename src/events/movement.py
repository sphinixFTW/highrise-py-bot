from highrise.models import User, Position, AnchorPosition
from config.config import loggers


async def on_move(bot, user: User, destination: Position | AnchorPosition) -> None:
    if loggers.userMovement:
        print(f"{user.username} movido para {destination}")
