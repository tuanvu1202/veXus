import discord
from discord.ext import commands
import os

class restart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener() 
    # async def on_ready(self):
    #     pass

    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx):
        await ctx.send("Restarting the bot!")
        await self.bot.logout()

async def setup(bot):
    await bot.add_cog(restart(bot))
