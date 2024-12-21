import discord
from discord.ext import commands

class join(commands.Cog):
    info = {
        "name": "joinnoti",
        "version": "1.0",
        "author": "tuanvu1202",
        "description": "Thông báo khi có người mới vào Guild!",
        "catogery": "System",
        "usage": "",
        "cooldowns": 0
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel()

async def setup(bot):
    await bot.add_cog(join(bot))
