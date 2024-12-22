import discord
from discord.ext import commands

class example(commands.Cog):
    info = {
        "name": "cash",
        "version": "1.0.0",
        "author": "tuanvu1202",
        "description": "Kiểm tra tiền của bản thân hoặc @mention",
        "catogery": "Utils",
        "usage": "",
        "cooldowns": 0
    }

    def __init__(self, bot):
        self.bot = bot
    
    async def create_account(self, user):
        

    @commands.command()
    async def example(self, ctx): 
        pass

async def setup(bot):
    await bot.add_cog(example(bot))
