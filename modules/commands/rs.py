import discord, os, json, sys
from discord.ext import commands

class rs(commands.Cog):
    info = {
        "name": "rs",
        "version": "1.0.0",
        "author": "tuanvu1202",
        "description": "Khởi động lại Bot!",
        "catogery": "System",
        "usage": "",
        
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rs(self, ctx): 
        configPath = self.bot.configPath
        with open(configPath,"r") as f:
            configValue = json.load(f)
        
        if str(ctx.author.id) in configValue["admin"]:
            await ctx.send("Tiến hành khởi động lại :white_check_mark:")
            os.execv(sys.executable, ['python'] + sys.argv)
            
        self.bot.run(configValue["token"])

async def setup(bot):
    await bot.add_cog(rs(bot))
