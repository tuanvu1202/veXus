import discord
from discord.ext import commands
import datetime

class upt(commands.Cog):
    info = {
        "name": "upt",
        "version": "1.0.0",
        "author": "tuanvu1202",
        "description": "Xem thời gian Bot hoạt động",
        "catogery": "System",
        "usage": "",
        
    }
    
    def __init__(self, bot):
        self.bot = bot
        self.StartTime = None

    @commands.Cog.listener() 
    async def on_ready(self):
        self.StartTime = discord.utils.utcnow()

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
        
        msg = discord.Embed(
            title="veXus", 
            colour=ctx.author.color, 
            description=
            f"Uptime: {discord.utils.format_dt(self.StartTime, "F")}\n"
            f"Ping: **{int(ping)}ms**\n"
            f"Status: **{getStatusByPing(ping)}**"
        )
        msg.set_footer(text = "veXus Copyright © 2024-2025", icon_url = "https://i.ibb.co/y063smH/veXus.png") 
        await ctx.reply(embed=msg)

async def setup(bot):
    await bot.add_cog(upt(bot))
