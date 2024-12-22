import discord
from discord.ext import commands

class gid(commands.Cog):
    info = {
        "name": "gid",
        "version": "1.0.0",
        "author": "tuanvu1202",
        "description": "Lấy ID của guild",
        "catogery": "System",
        "usage": "",
        
    }
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gid(self, ctx):
        await ctx.send(f"**{ctx.guild.name}**: {ctx.guild.id}")

async def setup(bot):
    await bot.add_cog(gid(bot))
