import discord
from discord.ext import commands

class setstatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener() 
    # async def on_ready(self):
    #     pass

    @commands.command()
    async def setstatus(self, ctx, new_status=None):
        if new_status == None:
            await self.bot.change_presence(activity=None)
            await ctx.send(self.bot.all_commands)

async def setup(bot):
    await bot.add_cog(setstatus(bot))
