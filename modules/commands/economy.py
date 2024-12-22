import discord, json
from discord.ext import commands
from database.mongo import db
from pymongo import MongoClient

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cluster  = MongoClient("mongodb://localhost:27017/")
        cluster  = MongoClient("mongodb://localhost:27017/")
        self.collection = cluster
        
    @commands.command()
    async def cash(self, ctx):    
        async def createAccount(id):
            await col.insert_one({
                "_id": id,
                "money": 100000,
                "bank": 100000
            })
                
        cluster = MongoClient("mongodb://localhost:27017/")
        db = cluster.get_database("veXus")
        col = db.get_collection("economy")
        find = col.find_one({"_id": ctx.author.id})
        if not find:
            await createAccount(ctx.author.id)
        check = col.find_one({"_id": ctx.author.id})
        embed = discord.Embed(
            title="Your Wallet",
            colour=ctx.author.color,
            description=
            f"Money: {check['money']:,} VNĐ"
        )
        embed.set_footer(text = "veXus Copyright © 2024-2025", icon_url = "https://i.ibb.co/y063smH/veXus.png")
        await ctx.reply(embed=embed)
        
async def setup(bot):
    print("Setting up Economy System")
    await bot.add_cog(Economy(bot))