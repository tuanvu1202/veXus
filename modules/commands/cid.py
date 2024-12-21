import discord
from discord.ext import commands

class cid(commands.Cog):
    info = {
        "name": "cid",
        "version": "1.0.0",
        "author": "tuanvu1202",
        "description": "Lấy ID của channel",
        "catogery": "System",
        "usage": "",
        "cooldowns": 0
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cid(self, ctx):
        await ctx.send(f"**{ctx.message.channel.name}**: {ctx.message.channel.id}")


async def setup(bot):
    await bot.add_cog(cid(bot))
