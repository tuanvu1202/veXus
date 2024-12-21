import discord, json
from discord.ext import commands

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
        configPath = self.bot.configPath
        with open(configPath, "r") as f:
            configValue = json.load(f)
        
        # tempConfig = configPath + ".temp"
        
        # with open(tempConfig, "w", encoding='utf-8') as f:
        #     json.dump(configValue, f, indent=4,ensure_ascii=False)
        adminList = []
        
        for i in configValue["admin"]:
            user = self.bot.get_user(i)
            adminList.append(user.name)
        # for id in configValue["admin"]:
        #     adminList.append(id)
        # adminl = "\n".join(adminList)
    
        if str(ctx.author.id) in configValue["admin"]:
            if choose == None:
                await ctx.send("Vui lòng nhập lựa chọn [add/remove/list] @mention")
            if choose == "list":
                msg = discord.Embed(title="DANH SÁCH ADMIN",colour=ctx.author.color, description=f"{adminList}")
                await ctx.reply(embed=msg)
            elif member == None:
                await ctx.send("Vui lòng @mention")
            elif choose == "add":
                if member.id not in configValue["admin"]:
                    # try:
                    #     configValue["admin"].append(member.id)
                    #     with open(configPath, "w", encoding='utf-8') as f:
                    #         json.dump(configValue, f, indent=4,ensure_ascii=False)
                    #     await ctx.send(f"Đã thêm {member.name} vào danh sách Admin!")
                    # except Exception as e:
                    #     await ctx.send(f"Lỗi khi thêm người dùng: {e}")
                    pass
                else:
                    await ctx.send("Người dùng đã tồn tại!")
            elif choose == "remove":
                if member.id in configValue["admin"]:
                    pass
                else:
                    await ctx.send("Người dùng chưa tồn tại!")
            else:
                await ctx.send("Lựa chọn không hợp lệ!")
        else:
            await ctx.send("Bạn không có quyền sử dụng lệnh này!")

async def setup(bot):
    await bot.add_cog(admin(bot))
