import json
import os
import asyncio
import discord
from discord.ext import commands
from core.utils.log import logger

def loadConfig():
    configPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.json"))
    try:
        with open(configPath) as f:
            logger("Config found!", "load")
            return json.load(f)
    except FileNotFoundError as e:
        logger("Config not found!", "error")
        return None
    except json.JSONDecodeError:
        logger("Error decoding Config.json!", "error")
        return None
    except Exception as e:
        print(f"An error occurred: {e}", "error")
        return None
    
async def loadModule(client):
    commandCout = 0
    eventCout = 0
    for command in os.listdir("./modules/commands"):
        if command.endswith(".py"):
            try:
                await client.load_extension(f"modules.commands.{command[:-3]}")
                commandCout+=1
                logger(f"Loaded command {command}!","load")
            except Exception as e:
                logger(f"Failed to load command {command[:-3]}: {e}","error")
            except Exception as e:
                logger(f"Unexpected error: {e}", "error")
                return None

    for event in os.listdir("./modules/events"):
        if event.endswith(".py"):
            try:
                await client.load_extension(f"modules.events.{event[:-3]}")
                eventCout+=1
                logger(f"Loaded event {event}!","load")

            except Exception as e:
                logger(f"Failed to load event {event[:-3]}: {e}","error")

            except Exception as e:
                logger(f"Unexpected error: {e}", "error")
                return None

    print(f"Loaded successfully {commandCout} Commands and {eventCout} Events!")

async def main():
    # Find Config
    config = loadConfig()
    if not config or "TOKEN" not in config:
        print("Config.json Error!")
        return 
    #Load commands and events
    client = commands.Bot(command_prefix=config["PREFIX"], intents=discord.Intents.all())
    async with client:
        await loadModule(client)
        await client.start(config["TOKEN"])

asyncio.run(main())