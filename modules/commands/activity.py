import discord
from discord.ext import commands

class activity(commands.Cog):
    info = {
        "name": "",
        "version": "",
        "author": "",
        "description": "",
        "catogery": "",
        "usage": "",
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def activity(self, ctx): 
        await ctx.send("HIEU LGBT")

async def setup(bot):
    await bot.add_cog(activity(bot))
