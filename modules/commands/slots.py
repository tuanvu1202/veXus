import discord, random
from discord.ext import commands

class slots(commands.Cog):
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
    async def slots(self, ctx, *args): 
        def rollEmoji():
            randValue = random.random()
            if randValue < 0.1:return 1
            if randValue < 0.2:return 6
            return random.randint(2,5)

        try:
            playerName = ctx.author.name
            moneyTmp = 100000

            if len(args) == 0:
                return await ctx.send("Vui lòng nhập tiền cược!")
            elif args.isdigit() == False:
                return await ctx.send("Tiền cược không hợp lệ!")

        except:
            pass


async def setup(bot):
    await bot.add_cog(slots(bot))
