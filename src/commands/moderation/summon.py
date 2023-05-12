from highrise import User, Position
from config.config import config, messages


class Command:
    def __init__(self, bot):
        self.bot = bot
        self.name = "summon"
        self.description = "Teleport a player to your position"
        self.aliases = ['tptome']
        self.permissions = ['teleport']
        self.cooldown = 5

    async def execute(self, user: User, args: list, message: str):
        prefix = config.prefix
        response = await self.bot.highrise.get_room_users()
        users = [content[0] for content in response.content]
        usernames = [user.username.lower() for user in users]

        if len(args) != 1:
            await self.bot.highrise.send_whisper(user.id, f"{messages.invalidUsage.format(prefix=prefix, commandName='summon', args='<@username>')}")
            return

        if args[0].lower() == 'all':
            # Teleport all users to your position
            your_pos = None
            for content in response.content:
                if content[0].id == user.id:
                    if isinstance(content[1], Position):
                        your_pos = content[1]
                    break
            if not your_pos:
                await self.bot.highrise.send_whisper(user.id, f"{messages.invalidPosition}")
                return
            for user in users:
                await self.bot.highrise.teleport(user.id, your_pos)
        elif args[0].lower().startswith('@'):
            # Trim '@' symbol from the username
            username = args[0].lower()[1:]
            if username not in usernames:
                await self.bot.highrise.send_whisper(user.id, f"{messages.invalidPlayer.format(user=username)}")
                return
            # Teleport the specified user to your position
            your_pos = None
            for content in response.content:
                if content[0].id == user.id:
                    if isinstance(content[1], Position):
                        your_pos = content[1]
                    break
            if not your_pos:
                await self.bot.highrise.send_whisper(user.id, f"{messages.invalidPosition}")
                return
            user_id = next(
                (u.id for u in users if u.username.lower() == username), None)
            if not user_id:
                await self.bot.highrise.send_whisper(user.id, f"{messages.invalidUser.format(user=username)}")
                return
            await self.bot.highrise.teleport(user_id, your_pos)
        else:
            if args[0].lower() not in usernames:
                await self.bot.highrise.send_whisper(user.id, f"{messages.invalidPlayer.format(user=args[0])}")
                return
            # Teleport the specified user to your position
            your_pos = None
            for content in response.content:
                if content[0].id == user.id:
                    if isinstance(content[1], Position):
                        your_pos = content[1]
                    break
            if not your_pos:
                await self.bot.highrise.send_whisper(user.id, f"{messages.invalidPosition}")
                return
            user_id = next(
                (u.id for u in users if u.username.lower() == args[0].lower()), None)
            if not user_id:
                await self.bot.highrise.send_whisper(user.id, f"{messages.invalidPlayer.format(user=args[0])}")
                return
            await self.bot.highrise.teleport(user_id, your_pos)
