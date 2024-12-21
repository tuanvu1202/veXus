import discord
from discord.ext import commands
import datetime

class upt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.UPT = None

    @commands.Cog.listener() 
    async def on_ready(self):
        self.UPT = datetime.datetime.now()

    @commands.command()
    async def upt(self, ctx):
        ping = self.bot.latency*1000
        def getStatusByPing(ping):
            if int(ping) < 200:
                return "Mượt"
            elif int(ping) < 800:
                return "Trung bình"
            else:
                return "Chậm"
        
        await ctx.send(f"Ping: **{int(ping)}** ms\nTình trạng: **{getStatusByPing(ping)}**")
        await ctx.send(self.UPT)
        

async def setup(bot):
    await bot.add_cog(upt(bot))
