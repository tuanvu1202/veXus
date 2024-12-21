import discord
from discord.ext import commands
import os
import json

class hec(commands.Cog):
    info = {
        "name": "hec",
        "version": "1.0.0",
        "author": "tuanvu1202",
        "description": "Xem cách sử dụng lệnh cho người mới",
        "catogery": "System",
        "usage": "",
        "cooldowns": 0
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hec(self, ctx, module=None): 
        if module == None:
            await ctx.send("Vui lòng nhập tên lệnh!")
        else:
            file = os.path.abspath(os.path.join(os.path.dirname(__file__), f"{module}"))
            with open(file) as f:
                cmd = json.load(f)
            await ctx.send(cmd)


async def setup(bot):
    await bot.add_cog(hec(bot))
