import discord
from discord.ext import commands
from discord import app_commands

class cid(commands.Cog):
    info = {
        "name": "cid",
        "version": "1.0.0",
        "author": "tuanvu1202",
        "description": "Lấy ID của channel",
        "catogery": "System",
        "usage": "",
        
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="cid")
    async def cid(self, ctx):
        await ctx.send(f"**{ctx.message.channel.name}**: {ctx.message.channel.id}")

async def setup(bot):
    await bot.add_cog(cid(bot))
