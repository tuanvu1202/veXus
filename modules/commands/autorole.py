import discord, json
from discord.ext import commands

class autorole(commands.Cog):
    info = {
        "name": "autosetrole",
        "version": "1.0.0",
        "author": "tuanvu1202",
        "description": "Tự động set role cho thành viên mới tham gia",
        "catogery": "Utils",
        "usage": "setrole [add/remove/list]",
        "cooldowns": 0
    }

    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join():
        pass

    @commands.command()
    async def autorole(self, ctx, choose=None, *role, member: discord.Member=None): 
        configPath = self.bot.configPath
        with open(configPath, "r") as f:
            configValue = json.load(f)
        
        if str(ctx.author.id) in configPath["admin"]:
            if choose == 'list':
                # for i in configPath["autoRole"]:
                #    uo
                pass
            elif choose == 'add':
                if str(role) not in configValue["autoRole"]:
                    try:
                        configValue["autoRole"].append(str(guild))
                        with open(configPath, "w", encoding='utf-8') as f:
                            json.dump(configValue, f, indent=4,ensure_ascii=False)
                        await ctx.send(f"Đã thêm {member.name} vào danh sách Admin!")
                    except Exception as e:
                        await ctx.send(f"Lỗi khi thêm người dùng: {e}")
                    pass
                else:
                    await ctx.send("Người dùng đã tồn tại!")
            elif choose == 'remove':
                pass
            else:
                await ctx.send("Sai cú pháp!")
        else:
            await ctx.send("Bạn không có quyền sử dụng lệnh này!")
        
async def setup(bot):
    await bot.add_cog(autorole(bot))
