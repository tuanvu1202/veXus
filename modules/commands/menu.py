import discord
from discord.ext import commands

class menu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() 
    async def on_ready(self):
        pass

    @commands.hybrid_command()
    async def menu(self, ctx): 
        await ctx.send("pong!")

async def setup(bot):
    await bot.add_cog(menu(bot))
