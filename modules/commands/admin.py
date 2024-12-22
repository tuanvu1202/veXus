import discord, json
from discord.ext import commands

class admin(commands.Cog):
    info = {
        "name": "admin",
        "version": "1.0.0",
        "author": "tuanvu1202",
        "description": "Quản lý Command của hệ thống",
        "catogery": "System",
        "usage": "admin [add/remove/list/only]",
        
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def admin(self, ctx, choose=None, member: discord.Member=None):
        configPath = self.bot.configPath
        
        with open(configPath, "r") as f:
            configValue = json.load(f)
    
        if str(ctx.author.id) in configValue["admin"]:
            if choose == None:
                await ctx.send("Vui lòng nhập lựa chọn [add/remove/list] @mention")
                return
            if choose == "list":
                adminList = []
                i = 0
                for adUser in configValue["admin"]:
                    i+=1
                    adminList.append(f"{i}. <@{adUser}>")
                boardAd = "\n".join(adminList)
                msg = discord.Embed(title="DANH SÁCH ADMIN",colour=ctx.author.color, description=f"{boardAd}")
                msg.set_footer(text = "veXus Copyright © 2024-2025", icon_url = "https://i.ibb.co/y063smH/veXus.png")
                await ctx.reply(embed=msg)
            elif choose == "only":
                if "adminOnly" not in configValue:
                    configValue["adminOnly"] = True
                    with open(configPath, "w", encoding='utf-8') as f:
                        json.dump(configValue, f, indent=4,ensure_ascii=False)
                        await ctx.send("Đã bật thành công chế độ AdminOnly!")
                else:
                    if configValue["adminOnly"] == True:
                        configValue["adminOnly"] = False
                        with open(configPath, "w", encoding='utf-8') as f:
                            json.dump(configValue, f, indent=4,ensure_ascii=False)
                            await ctx.send("Đã tắt thành công chế độ AdminOnly!")
                    elif configValue["adminOnly"] == False:
                        configValue["adminOnly"] = True
                        with open(configPath, "w", encoding='utf-8') as f:
                            json.dump(configValue, f, indent=4,ensure_ascii=False)
                            await ctx.send("Đã bật thành công chế độ AdminOnly")
            elif member == None:
                await ctx.send("Vui lòng @mention")
            elif choose == "add":
                if str(member.id) not in configValue["admin"]:
                    try:
                        configValue["admin"].append(str(member.id))
                        with open(configPath, "w", encoding='utf-8') as f:
                            json.dump(configValue, f, indent=4,ensure_ascii=False)
                        await ctx.send(f"Đã thêm **{member.name}** vào danh sách Admin!")
                    except Exception as e:
                        await ctx.send(f"Lỗi khi thêm người dùng: {e}")
                    pass
                else:
                    await ctx.send("Người dùng đã tồn tại!")
            elif choose == "remove":
                if str(member.id) in configValue["admin"]:
                    try:
                        configValue["admin"].remove(str(member.id))
                        with open(configPath, "w", encoding='utf-8') as f:
                            json.dump(configValue, f, indent=4,ensure_ascii=False)
                        await ctx.send(f"Đã xóa **{member.name}** khỏi danh sách Admin!")
                    except Exception as e:
                        await ctx.send(f"Lỗi khi xóa người dùng: {e}")
                    pass
                else:
                    await ctx.send("Người dùng không tồn tại!")
            else:
                await ctx.send("Lựa chọn không hợp lệ!")
        else:
            await ctx.send("Bạn không có quyền sử dụng lệnh này!")

async def setup(bot):
    await bot.add_cog(admin(bot))
