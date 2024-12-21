import discord
from discord.ext import commands

class kick(commands.Cog):
    info = {
        "name": "kick",
        "version": "1.0.0",
        "author": "tuanvu1202",
        "description": "Xóa người cần xóa bằng @mention",
        "catogery": "System",
        "usage": "@mention",
        "cooldowns": 0
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member: discord.Member=None, reason=None): 
        if member == None:
            await ctx.send("Vui lòng @mention người bạn muốn xóa!")
        else:
            await member.kick(reason=reason)
            await ctx.send(f"Đã xóa thành công **{member.name}** khỏi nhóm với lí do: **{reason}!**")

async def setup(bot):
    await bot.add_cog(kick(bot))
