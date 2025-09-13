import discord
from discord.ext import commands

class help(commands.Cog):
    info = {
        "name": "",
        "version": "",
        "author": "",
        "description": "",
        "catogery": "",
        "usage": "",
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx): 
        msg = discord.Embed(
            title="veXus", 
            colour=ctx.author.color, 
            description=
            f"\n"
        )
        msg.set_footer(text = "veXus Copyright © 2024-2025", icon_url = "https://i.ibb.co/y063smH/veXus.png") 
        await ctx.reply(embed=msg)

async def setup(bot):
    await bot.add_cog(help(bot))
