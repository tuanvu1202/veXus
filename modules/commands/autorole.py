import discord
from discord.ext import commands
from discord.utils import get

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
        # guild = member.guild
        # roles = []
        
        if str(ctx.author.id) in config["admin"]:
            if choose == 'list':
                for i in config["autoRole"]:
                    # roleName = guild.get_role(i)
                    # roles.append(roleName)
                    await ctx.send(i)
                    
                await ctx.send(roles)
            elif choose == 'add':
                pass
            elif choose == 'remove':
                pass
            else:
                await ctx.send("Sai cú pháp!")
        else:
            await ctx.send("Bạn không có quyền sử dụng lệnh này!")
        
async def setup(bot):
    await bot.add_cog(autorole(bot))
