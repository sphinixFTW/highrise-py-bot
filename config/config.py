class config:
    # Basic configuration: If you are unsure how to obtain the Bot ID, simply start the bot and it will be logged in the console.
    prefix = '/'
    botID = '65c8f079a34c5583eed6b80d'
    botName = 'G4mi_Sales'
    ownerName = 'Y4gami'
    roomName = 'LOJINHA DO GAMI'
    coordinates = {
        'x': 16.5,
        'y': -10,
        'z': -12,
        'facing': 'FrontLeft'
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
    reactions = True
    userMovement = True


class messages:
    # The following are optional and serve as a basic usage example for calling messages and replacing variables.
    invalidPosition = "Sua posição não pode ser determinada"
    invalidPlayer = "{user} não está na sala"
    invalidUser = "Usuario {user} não encontrado"
    invalidUsage = "Usage: {prefix}{commandName}{args}"
    invalidUserFormat = "Invalid user format. Please use '@username'."


class permissions:
    # You can add as many IDs as you want, for example: ['id1', 'id2'].
    owners = ['60976207a0cc22f26e9afdda']
    moderators =['60976207a0cc22f26e9afdda']


class authorization:
    # To obtain your token, visit https://highrise.game/ and log in. Then, go to the settings and create a new bot. Accept the terms and generate a token.
    # To obtain your room ID, go to the game and navigate to the top right corner where the player list is displayed. Click on "Share this room" and copy the ID.
    room = '64164c725d27124026dfdc94'
    token = 'dd4cd59b201a1ecf81942432df8ca5fb150103d2eddd36e5f096a2e14fef5e2b'
