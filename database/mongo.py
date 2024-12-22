from motor.motor_asyncio import AsyncIOMotorClient
import json
with open("config.json", "r") as f:
    config = json.load(f)
    
class db():
    client = AsyncIOMotorClient(config["database"]["mongoUri"])
    database = client[config["database"]["mongoDB"]]
