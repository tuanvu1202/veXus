import json, os, asyncio, fade, discord, requests
from discord.ext import commands
from core.utils.log import logger
# Load config
configPath = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.json"))
def loadConfig():
    try:
        with open(configPath) as f:
            logger("Config found!", "load")
            config = json.load(f)
            return config
    except FileNotFoundError as e:
        logger("Config not found!", "error")
        return None
    except json.JSONDecodeError:
        logger("Error decoding Config.json!", "error")
        return None
    except Exception as e:
        print(f"An error occurred: {e}", "error")
        return None
        
def updater():
    pass

def database():
    pass

# Load modules 
async def loadModule(client, config):
    commandCout = 0
    eventCout = 0
    for command in os.listdir("./modules/commands"):
        if command.endswith(".py") and command not in config["commandDisabled"]:
            try:
                await client.load_extension(f"modules.commands.{command[:-3]}")
                commandCout+=1
                logger(f"Loaded command {command}!","load")
                
                await asyncio.sleep(0.025)
            except Exception as e:
                logger(f"Failed to load command {command[:-3]}: {e}","error")
                await asyncio.sleep(0.025)

    for event in os.listdir("./modules/events"):
        if event.endswith(".py") and event not in config["eventDisabled"]:
            try:
                await client.load_extension(f"modules.events.{event[:-3]}")
                eventCout+=1
                logger(f"Loaded event {event}!","load")
                await asyncio.sleep(0.025)
            except Exception as e:
                logger(f"Failed to load event {event[:-3]}: {e}","error")
                await asyncio.sleep(0.025)

    logger(f"Loaded successfully {commandCout} Commands and {eventCout} Events!","")

# Main
async def main():
    logo = """
 ██▒   █▓▓█████ ▒██   ██▒ █    ██   ██████ 
▓██░   █▒▓█   ▀ ▒▒ █ █ ▒░ ██  ▓██▒▒██    ▒ 
 ▓██  █▒░▒███   ░░  █   ░▓██  ▒██░░ ▓██▄   
  ▒██ █░░▒▓█  ▄  ░ █ █ ▒ ▓▓█  ░██░  ▒   ██▒
   ▒▀█░  ░▒████▒▒██▒ ▒██▒▒▒█████▓ ▒██████▒▒
   ░ ▐░  ░░ ▒░ ░▒▒ ░ ░▓ ░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░
   ░ ░░   ░ ░  ░░░   ░▒ ░░░▒░ ░ ░ ░ ░▒  ░ ░
     ░░     ░    ░    ░   ░░░ ░ ░ ░  ░  ░  
      ░     ░  ░ ░    ░     ░           ░  
     ░                                     
"""
    print(fade.purpleblue(logo))
    # Find Config
    config = loadConfig()
    if not config:
        return  
    client = commands.Bot(command_prefix=config["prefix"], intents=discord.Intents.all())
    setattr(client, "configPath", configPath)
    


    async with client:
        await loadModule(client, config)
        await client.start(config["token"])

asyncio.run(main())