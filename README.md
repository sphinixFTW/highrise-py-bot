# Highrise PY Bot Template

> **This python template helps you get started with your first Highrise Bot.**

## **⚙️ Installation** 
```
pip install highrise-bot-sdk==23.1.0b10
```

## **✨ Features**

- Easy-to-use interface.
- Beginner-friendly design.
- Advanced command and event handlers.
- Customizable permissions and cooldowns for commands.
- Flexible configuration file for easy modifications.


## **🎐 Usage**
To start the bot:
```
python main.py
```

PATH: config/config.py:
```py
class config:
    # Basic configuration: If you are unsure how to obtain the Bot ID, simply start the bot and it will be logged in the console.
    prefix = '/'
    botID = 'change-me'
    botName = 'change-me'
    ownerName = 'change-me'
    roomName = 'change-me'
    coordinates = {
        'x': 0,
        'y': 0,
        'z': 0,
        'facing': 'FrontRight'
    }

class authorization:
    # To obtain your token, visit https://highrise.game/ and log in. Then, go to the settings and create a new bot. Accept the terms and generate a token.
    # To obtain your room ID, go to the game and navigate to the top right corner where the player list is displayed. Click on "Share this room" and copy the ID.
    room = 'change-me'
    token = 'change-me'
```
PATH: config/permission.json
```json
{
    "permissions": [
        {
            "user_id": "change-me",
            "username": "change-me",
            "permissions": [
                "emote"
            ]
        }
    ]
}
```

## Note

While you have the freedom to modify this package to suit your needs, please refrain from claiming it as your own. Let's respect the efforts put into creating and sharing this resource.