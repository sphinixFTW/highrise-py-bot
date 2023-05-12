from highrise.models import User, SessionMetadata, CurrencyItem, Item, Reaction, AnchorPosition, Position
from src.events import join, leave, emote, whisper, start, chat, tips, react, movement


async def handle_start(bot, session_metadata: SessionMetadata) -> None:
    try:
        await start.on_start(bot, session_metadata)
    except Exception as e:
        print(f"An Error Occured: {e}")


async def handle_join(bot, user: User) -> None:
    try:
        await join.on_join(bot, user)
    except Exception as e:
        print(f"An Error Occurred: {e}")


async def handle_leave(bot, user: User) -> None:
    try:
        await leave.on_leave(bot, user)
    except Exception as e:
        print(f"An Error Occurred: {e}")


async def handle_whisper(bot, user: User, message: str) -> None:
    try:
        await whisper.on_whisper(bot, user, message)
    except Exception as e:
        print(f"An Error Occured: {e}")


async def handle_chat(bot, user: User, message: str) -> None:
    try:
        await chat.on_chat(bot, user, message)
    except Exception as e:
        print(f"An Error Occured: {e}")


async def handle_emote(bot, user: User, emote_id: str, receiver: User) -> None:
    try:
        await emote.on_emote(bot, user, emote_id, receiver)
    except Exception as e:
        print(f"An Error Occured: {e}")


async def handle_reactions(bot, user: User, reaction: Reaction, receiver: User) -> None:
    try:
        await react.on_reaction(bot, user, reaction, receiver)
    except Exception as e:
        print(f"An Error Occured: {e}")


async def handle_movements(bot, user: User, destination: Position | AnchorPosition) -> None:
    try:
        await movement.on_move(bot, user, destination)
    except Exception as e:
        print(f"An Error Occured: {e}")


async def handle_tips(bot, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
    try:
        await tips.on_tip(bot, sender, receiver, tip)
    except Exception as e:
        print(f"An Error Occured: {e}")
