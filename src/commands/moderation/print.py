from highrise import User, Position, AnchorPosition
from config.config import config, messages, permissions


class Command:
    def __init__(self, bot):
        self.bot = bot
        self.name = "print"
        self.description = "Print someone's data"
        self.aliases = ['location', 'coords']
        self.cooldown = 5

    async def execute(self, user: User, args: list, message: str):
        if user.id not in permissions.moderators:
            return await self.bot.highrise.send_whisper(user.id, f"Este comando é um comando apenas para moderadores.")
        else:
            prefix = config.prefix
            # Get the room users
            response = await self.bot.highrise.get_room_users()
            users = [content[0]
                     for content in response.content]  # Extract the User objects
            # Extract the usernames in lowercase
            usernames = [user.username.lower() for user in users]

            # Check if the specified user is in the room
            if len(args) != 1:
                await self.bot.highrise.send_whisper(user.id, f"{messages.invalidUsage.format(prefix=prefix, commandName='print',args='@username')}")
                return
            # Check if the lowercase version of the username is in the list
            elif args[0].startswith("@") and len(args[0]) > 1:
                # extract the username by removing the "@" symbol
                username = args[0][1:]
            else:
                username = args[0]
            if username.lower() not in usernames:
                await self.bot.highrise.send_whisper(user.id, f"{messages.invalidPlayer.format(user=username)}")
                return

            # Get the position of the specified user
            # Find the User object for the specified username
            user = users[usernames.index(username.lower())]
            position = None
            for content in response.content:
                if content[0].id == user.id:
                    if isinstance(content[1], Position):
                        position = content[1]
                        msg = f"@{user.username} is at ({position.x}x, {position.y}y, {position.z}z) facing '{position.facing}'"
                    elif isinstance(content[1], AnchorPosition):
                        position = content[1]
                        msg = f"@{user.username} is on entity: {position.entity_id} anchor: {position.anchor_ix}"
                    break

            # Print the user ID and position
            print(msg)
            await self.bot.highrise.chat(msg)
