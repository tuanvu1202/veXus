import discord, os, json
from discord.ext import commands
from core.utils.log import logger

class cmd(commands.Cog):
    info = {
        "name": "cmd",
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
    async def cmd(self, ctx, choose=None, command:str=None):
        configPath = self.bot.configPath
        with open(configPath,"r") as f:
            configValue = json.load(f)
    
        commandSuccess = 0
        commandFailed = 0
        if str(ctx.author.id) in configValue["admin"]:
            if choose == None:
                await ctx.send("Vui lòng nhập theo cú pháp [load/unload/loadAll/unloadAll] [command]!")
            elif choose.lower() == "load" and command != None: 
                try:
                    commandFound = False
                    for file in os.listdir("./modules/commands"):
                        if(file.endswith(".py") and file[:-3] == command):
                            commandFound = True
                            try:
                                await self.bot.load_extension(f"modules.commands.{command}")
                                if file in configValue["commandDisabled"]:
                                    configValue["commandDisabled"].remove(file)
                                    with open(configPath, "w", encoding='utf-8') as f:
                                        json.dump(configValue, f, indent=4,ensure_ascii=False)
                                        await ctx.send("Load thành công 1 lệnh!")
                                        logger(f"Load thành công {file}", "load")
                                        return
                                else:
                                    await ctx.send("Lệnh đã được Load trước đó!")
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

            elif choose.lower() == "unload" and command != None: 
                try:
                    commandFound = False
                    for file in os.listdir("./modules/commands"):
                        if(file.endswith(".py") and file[:-3] == command):
                            commandFound = True
                            try:
                                await self.bot.unload_extension(f"modules.commands.{command}")
                                if file not in configValue["commandDisabled"]:
                                    configValue["commandDisabled"].append(file)
                                    with open(configPath, "w", encoding='utf-8') as f:
                                        json.dump(configValue, f, indent=4,ensure_ascii=False)
                                        await ctx.send("Unload thành công 1 lệnh!")
                                        logger(f"Unload thành công {file}", "load")
                                        return
                                else:
                                    await ctx.send("Lệnh đã được Unload trước đó!")
                            except commands.ExtensionNotLoaded:
                                await ctx.send("Lệnh chưa được Load!")
                                logger(f"Unload không được {file}", "error")
                                return
                            except Exception as e:
                                await ctx.send("Unload thành công 0 lệnh!")
                                logger(f"Unload thành công {file}", "load")
                                await ctx.send(e)
                                return
                    if not commandFound:
                        await ctx.send("Lệnh không tồn tại!")
                except Exception as e:
                    await ctx.send("Unload thành công 0 lệnh!")
                    logger(f"Unload không được {file}", "error")
                    await ctx.send(e)

            elif choose.lower() == "loadall":
                try:
                    for file in os.listdir("modules/commands"):
                        if file.endswith(".py"):
                            try:
                                if file in configValue["commandDisabled"]:
                                    configValue["commandDisabled"].remove(file) 
                                    with open(configPath, "w", encoding='utf-8') as f:
                                        json.dump(configValue, f, indent=4,ensure_ascii=False)
                                await self.bot.load_extension(f"modules.commands.{file[:-3]}")
                                logger(f"Load thành công {file}", "load")
                                commandSuccess+=1
                            except commands.ExtensionAlreadyLoaded:
                                try:
                                    await self.bot.reload_extension(f"modules.commands.{file[:-3]}")
                                    logger(f"Reload thành công {file}", "load")
                                    commandSuccess+=1
                                except Exception as e:
                                    await ctx.send(e)
                            except Exception as e:
                                logger(f"Reload thất bại {file}", "error")
                                await ctx.send(e)
                                commandFailed+=1
                    await ctx.send(f"Load thành công {commandSuccess} lệnh và thất bại {commandFailed} lệnh!")
                except Exception as e:
                    await ctx.send(e)

            elif choose.lower() == "unloadall":
                try:
                    for file in os.listdir("modules/commands"):
                        if file.endswith(".py"):
                            try:
                                if file not in configValue["commandDisabled"]:
                                    configValue["commandDisabled"].append(file)
                                with open(configPath, "w", encoding='utf-8') as f:
                                        json.dump(configValue, f, indent=4,ensure_ascii=False)
                                await self.bot.unload_extension(f"modules.commands.{file[:-3]}")
                                logger(f"Unload thành công {file}", "load")
                                commandSuccess+=1;
                            except commands.ExtensionNotLoaded:
                                try:
                                    await self.bot.load_extension(f"modules.commands.{file[:-3]}")
                                    await self.bot.unload_extension(f"modules.commands.{file[:-3]}")
                                except Exception as e:
                                    await ctx.send(f"Unload không được {file}: {e}")
                            except Exception as e:
                                logger(f"Unload không được {file}", "error")
                                await ctx.send(e)
                                commandFailed+=1
                                
                    await ctx.send(f"Unload thành công {commandSuccess} lệnh và thất bại {commandFailed} lệnh!")
                except Exception as e:
                    await ctx.send(e)
                    
            else:
                await ctx.send("Sai cú pháp!")
                
        else:
            await ctx.send("Bạn không có quyền sử dụng lệnh này!")

async def setup(bot):
    await bot.add_cog(cmd(bot))
