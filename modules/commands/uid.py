import discord
from discord.ext import commands

class uid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() 
    async def on_ready(self):
        pass

    @commands.command()
    async def uid(self, ctx, member: discord.Member=None):
        if member == None:
            await ctx.send(f"**{ctx.author.name}**: {ctx.author.id}")
        else:
            await ctx.send(f"**{member.name}**: {member.id}")

async def setup(bot):
    await bot.add_cog(uid(bot))
