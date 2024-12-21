import discord
from discord.ext import commands

class setname(commands.Cog):
    info = {
        "name": "setname",
        "version": "1.0.0",
        "author": "tuanvu1202",
        "description": "Đổi tên của người dùng",
        "catogery": "System",
        "usage": "",
        "cooldowns": 0
    }
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setname(self, ctx, member: discord.Member=None, *, new_name=None):
        if member == None:
            await ctx.send("Vui lòng @mention người muốn đổi tên!")
        if new_name == None:
            await ctx.send("Vui lòng nhập tên muốn đổi!")
        else:
            await member.edit(nick=new_name)
            await ctx.send(f"Đã thay đổi tên của **{member.name}** thành **{new_name}**!")

async def setup(bot):
    await bot.add_cog(setname(bot))
