import discord
from discord.ext import commands

class on_ready(commands.Cog):
    info = {
        "name": "on_ready",
        "version": "1.0",
        "author": "tuanvu1202",
        "description": "",
        "catogery": "System",
        "usage": "",
        "cooldowns": 0
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.event
    async def on_ready(self):
        print(f"Logged in as {self.user}!")

async def setup(bot):
    await bot.add_cog(on_ready(bot))
