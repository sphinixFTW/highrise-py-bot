class config:
    # Basic configuration: If you are unsure how to obtain the Bot ID, simply start the bot and it will be logged in the console.
    prefix = '/'
    botID = 'change-me'
    botName = 'change-me'
    ownerName = 'change-me'
    roomName = 'change-me'
    coordinates = {
        'x': 8.5,
        'y': 0.6000,
        'z': 20.5,
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
    emotes = False
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
    owners = ['55bb64735531104341039ca8']
    moderators = ['55bb64735531104341039ca8']


class authorization:
    # To obtain your token, visit https://highrise.game/ and log in. Then, go to the settings and create a new bot. Accept the terms and generate a token.
    # To obtain your room ID, go to the game and navigate to the top right corner where the player list is displayed. Click on "Share this room" and copy the ID.
    room = '6276f3ca8fa2ab3f786704ca'
    token = 'f397872fa4c14ea9874fe7c86aa0070eed9f62fc6c35804b005ccaae2f9b3fd4'
