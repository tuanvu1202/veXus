import discord
from discord.ext import commands

class cid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() 
    async def on_ready(self):
        pass

    @commands.command()
    async def cid(self, ctx):
        await ctx.send(f"**{ctx.message.channel.name}**: {ctx.message.channel.id}")


async def setup(bot):
    await bot.add_cog(cid(bot))
