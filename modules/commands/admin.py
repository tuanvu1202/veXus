import discord
from discord.ext import commands

class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() 
    async def on_ready(self):
        pass

    @commands.command()
    async def admin(self, ctx): 
        await ctx.send("pong!")

async def setup(bot):
    await bot.add_cog(admin(bot))
