import discord, os, json
from discord.ext import commands
from core.utils.log import logger

class load(commands.Cog):
    info = {
        "name": "load",
        "version": "1.0.0",
        "author": "tuanvu1202",
        "description": "Load Command của hệ thống",
        "catogery": "System",
        "usage": "load",
        
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def load(self, ctx, command:str=None):
        configPath = self.bot.configPath
        with open(configPath,"r") as f:
            configValue = json.load(f)

        if str(ctx.author.id) in configValue["admin"]:
            try:
                commandFound = False
                for file in os.listdir("./modules/commands"):
                    if(file.endswith(".py") and file[:-3] == command):
                        commandFound = True
                        try:
                            await self.bot.load_extension(f"modules.commands.{command}")
                            await ctx.send("Load thành công 1 lệnh!")
                            logger(f"Load thành công {file}", "load")
                            return
                        except commands.ExtensionAlreadyLoaded:
                            try:
                                await self.bot.reload_extension(f"modules.commands.{command}")
                                await ctx.send("Load thành công 1 lệnh!")
                                logger(f"Load thành công {file}", "load")
                                return
                            except Exception as e:
                                await ctx.send("Load thành công 0 lệnh!") 
                                logger(f"Không load được {file}", "error")
                                return      
                        except Exception as e:
                            await ctx.send("Load thành công 0 lệnh!")
                            logger(f"Không load được {file}", "error")
                            await ctx.send(e)
                            return
                if not commandFound:
                    await ctx.send("Lệnh không tồn tại!")
            except Exception as e:
                await ctx.send("Load thành công 0 lệnh!")
                logger(f"Load không được {file}", "error")
                await ctx.send(e)
        else:
            await ctx.send("Bạn không có quyền sử dụng lệnh này!")

async def setup(bot):
    await bot.add_cog(load(bot))
