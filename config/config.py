class config:
    # Basic configuration: If you are unsure how to obtain the Bot ID, simply start the bot and it will be logged in the console.
    prefix = '/'
    botID = '01b50864d754b0b8522967751d2b34d252b2e8bcc065ef7327b70dfb9d14aaa6'
    botName = 'offsetbot'
    ownerName = 'daniel_offset'
    roomName = '🤖PM BOT🤖'
    coordinates = {
        'x':  7,
        'y':  0,
        'z':  7,
        'facing': 'FrontRight'
    }


class loggers:
    # The following settings are related to events. Each event log can be enabled or disabled. Note that turning these off will not affect their usage in the game.
    SessionMetadata = True
    messages = True
    whispers = True
    joins = True
    leave = True
    tips = True
    emotes = True
    reactions = False
    userMovement = False


class messages:
    # The following are optional and serve as a basic usage example for calling messages and replacing variables.
    invalidPosition = "Your position could not be determined."
    invalidPlayer = "{user} is not in the room."
    invalidUser = "User {user} is not found."
    invalidUsage = "Usage: {prefix}{commandName}{args}"
    invalidUserFormat = "Invalid user format. Please use '@username'."


class permissions:
    # You can add as many IDs as you want, for example: ['id1', 'id2'].
    owners = ['daniel_offset']
    moderators = ['55bb64735531104341039ca8']


class authorization:
    # To obtain your token, visit https://highrise.game/ and log in. Then, go to the settings and create a new bot. Accept the terms and generate a token.
    # To obtain your room ID, go to the game and navigate to the top right corner where the player list is displayed. Click on "Share this room" and copy the ID.
    room = '65bafc4d0738febd4d5b9a55'
    token = '01b50864d754b0b8522967751d2b34d252b2e8bcc065ef7327b70dfb9d14aaa6'
