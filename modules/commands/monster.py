import discord
from discord.ext import commands

class example(commands.Cog):
    info = {
        "name": "",
        "version": "",
        "author": "",
        "description": "",
        "catogery": "",
        "usage": "",
        "cooldowns": 0
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def example(self, ctx): 
        pass

async def setup(bot):
    await bot.add_cog(example(bot))
