import discord
from discord.ext import commands
import os

class admin(commands.Cog):
    info = {
        "name": "admin",
        "version": "1.0.0",
        "author": "tuanvu1202",
        "description": "Quản lý Command của hệ thống",
        "catogery": "System",
        "usage": "load/loadall/unload/unloadall",
        "cooldowns": 0
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def admin(self, ctx, choose=None, member: discord.Member=None):
        config = self.bot.config
    
        if str(ctx.author.id) in config["admin"]:
            if choose == None:
                await ctx.send("Vui lòng nhập lựa chọn [add/remove/list] @mention")
            if choose == "list":
                await ctx.send("Danh sách Admin:\n")
                for id in config["admin"]:
                    user = self.bot.get_user(id)
                    await ctx.send(f"{user}\n")
                    
            elif member == None:
                await ctx.send("Vui lòng @mention")
            elif choose == "add":
                if member.id not in config["admin"]:
                    config["admin"].append(f"{id}")
                else:
                    await ctx.send("Người dùng đã tồn tại!")
            elif choose == "remove":
                if member.id in config["admin"]:
                    config["admin"].remove(f"{id}")
                else:
                    await ctx.send("Người dùng chưa tồn tại!")
            else:
                await ctx.send("Lựa chọn không hợp lệ!")
        else:
            await ctx.send("Bạn không có quyền sử dụng lệnh này!")

async def setup(bot):
    await bot.add_cog(admin(bot))
