import importlib.util
import os
import json
import time
from highrise import User


def get_user_permissions(user: User):
    with open("config/permissions.json", "r") as f:
        data = json.load(f)

    user_permissions = []

    for permission in data["permissions"]:
        if permission["username"] == user.username:
            user_permissions = permission["permissions"]
            break

    return user_permissions


class CommandHandler:
    def __init__(self, bot):
        self.bot = bot
        self.commands = {}
        self.cooldowns = {}  # dictionary to keep track of cooldowns for each command and user
        self.load_commands()

    def load_commands(self):
        """Load commands from modules in the src/commands directory"""
        commands_dir = os.path.join(
            os.path.dirname(__file__), "..", "commands")
        for category in os.listdir(commands_dir):
            category_dir = os.path.join(commands_dir, category)
            if os.path.isdir(category_dir):
                for command_file in os.listdir(category_dir):
                    if command_file.endswith(".py"):
                        # so now when you make a new file the file has to be the same as the command for example:
                        command_name = os.path.splitext(command_file)[0]
                        # this allow us to make categories for each command like moderation, general etc..
                        command_module = f"src.commands.{category}.{command_name}"
                        spec = importlib.util.spec_from_file_location(
                            command_module, os.path.join(
                                category_dir, command_file)
                        )
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
                        command = getattr(module, "Command")(self.bot)
                        if command_name in self.commands:
                            del self.commands[command_name]
                            for alias in command.aliases:
                                if alias in self.commands:
                                    # this allow us to add aliases to commands for example: help can also work with info
                                    del self.commands[alias]
                        self.commands[command.name] = command
                        if hasattr(command, "aliases"):
                            for alias in command.aliases:
                                self.commands[alias] = command

                                # now lets handle the command and add cooldowns per users

    async def handle_command(self, user, message):
        """handle a chat message that starts with prefix for example /"""
        parts = message[1:].split()  # here we split the "/" from the name
        command_name = parts[0]
        args = parts[1:]
        command = self.commands.get(command_name)
        if command:
            if hasattr(command, "permissions"):  # now lets check for permissions
                # call the functions we created earlier
                user_permissions = get_user_permissions(user)
                if not all(p in user_permissions for p in command.permissions):
                    # this will basically send a whisper letting
                    await self.bot.highrise.send_whisper(user.id, "You don't have permissions to use this command")
                    # the user know that they can't use the command
                    return
            cooldown = command.cooldown  # lets add the cooldown for each command per users
            user_id = user.id
            if command_name in self.cooldowns and user_id in self.cooldowns[command_name]:
                remaining_time = self.cooldowns[command_name][user_id] - time.time()
                if remaining_time > 0:
                    await self.bot.highrise.send_whisper(user_id, f"{command_name} is on cooldown. Try again in {int(remaining_time)} seconds.")
                    # this sends a whisper saying that they have to wait x seconds to re use the command
                    return
            if command_name not in self.cooldowns:
                # this is optional, if the command doesnt have a cooldown then cooldown is set to null
                self.cooldowns[command_name] = {}
            self.cooldowns[command_name][user_id] = time.time() + cooldown
            await command.execute(user, args, message)

            # now lets go to our main file to call the command handler..
