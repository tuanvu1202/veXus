import discord
from discord.ext import commands
import os

class cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() 
    async def on_ready(self):
        pass

    @commands.command()
    @commands.is_owner()
    async def cmd(self, ctx,choose,command:str=None):
        commandSuccess = 0
        commandFailed = 0
        if choose.lower() == "load": 
            try:
                await self.bot.load_extension(f"modules.commands.{command}")
                await ctx.send("Load thành công 1 lệnh!")
            except Exception as e:
                await self.bot.reload_extension(f"modules.commands.{command}")
                await ctx.send("Load thành công 1 lệnh!")
            except Exception as e:
                await ctx.send("Unload thành công 0 lệnh!")
                await ctx.send(e)

        if choose.lower() == "loadall":
            try:
                for filename in os.listdir("modules/commands"):
                    if filename.endswith(".py"):
                        try:
                            await self.bot.reload_extension(f"modules.commands.{filename[:-3]}")
                            commandSuccess+=1
                        except Exception as e:
                            await ctx.send(e)
                            commandFailed+=1
                await ctx.send(f"Load thành công {commandSuccess} lệnh và thất bại {commandFailed} lệnh!")        
            except Exception as e:
                await ctx.send(e)
        if choose.lower() == "unload": 
            try:
                await self.bot.unload_extension(f"modules.commands.{command}")
                await ctx.send("Unload thành công 1 lệnh!")
            except Exception as e:
                await ctx.send("Unload thành công 0 lệnh!")
                await ctx.send(e)
        if choose.lower() == "unloadall":
            try:
                for filename in os.listdir("modules/commands"):
                    if filename.endswith(".py"):
                        try:
                            await self.bot.unload_extension(f"modules.commands.{filename[:-3]}")
                            commandSuccess+=1;
                        except Exception as e:
                            await ctx.send(e)
                            commandFailed+=1
                await ctx.send(f"Unload thành công {commandSuccess} lệnh và thất bại {commandFailed} lệnh!")
            except Exception as e:
                await ctx.send(e)

async def setup(bot):
    await bot.add_cog(cmd(bot))
