import discord, random, math, datetime, pytz, aiohttp, asyncio
from discord.ext import commands

class taixiu(commands.Cog):
    info = {
        "name": "taixiu",
        "version": "1.0.0",
        "author": "tuanvu1202",
        "description": "Game tài xỉu trên Discord",
        "catogery": "Game",
        "usage": "",
        
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1,10,commands.BucketType.user)
    async def tx(self, ctx, *args): 
        tilethang = 0.9
        timedelay = 1.5
    
        def rollDice():
            randValue = random.random()
            if randValue < 0.1:return 1
            if randValue < 0.2:return 6
            return random.randint(2,5)

        try:  
            name = ctx.author.name
            money = 100000
            
            if len(args) == 0:
                return await ctx.send("Vui lòng nhập tài/xỉu và tiền cược!")
            elif len(args) == 1:
                if args[0].isdigit():
                    return await ctx.send("Vui lòng nhập tài/xỉu!")
                else:
                    return await ctx.send("Vui lòng nhập số tiền cược!")
            
            inp = args[0]
            bet = None
            if args[1].lower() == "all" or args[1].lower() == "a":
                bet = money
            else:
                if args[0].isdigit():
                    return await ctx.send("Vui lòng nhập tài/xỉu và tiền cược!")
                elif not args[1].isdigit():
                    return await ctx.send("Vòng lòng nhập số tiền hợp lệ!")
                bet = float(args[1])
                    
            if bet > money:
                return await ctx.send("Bạn không đủ tiền để đặt được")
            elif bet < 1000 or bet > 100000000:
                return await ctx.send("**Min: 1,000 VNĐ**\n**Max: 100,000,000 VNĐ**")

            choose = None
            if inp in ['tài','Tài','-t', 't']:
                choose = 'tài'
            elif inp in ['xỉu','Xỉu','-x', 'x']:
                choose = 'xỉu'
            else:
                return "Sai Tag"
            
            number = []
            emoji = []
            for i in range(1,4):

                n = rollDice()
                
                number.append(n)
                
                emoji.append({
                    1: "<:xx1:1320030996485111891>", 
                    2: "<:xx2:1320031067918569572>", 
                    3: "<:xx3:1320031082690773043>", 
                    4: "<:xx4:1320031092341735456>", 
                    5: "<:xx5:1320031104778113024>", 
                    6: "<:xx6:1320031115469127721>"
                }[n])
                await asyncio.sleep(timedelay * 0)
                
            total = number[0] + number[1] + number[2]
            ans = None
            result = None
            mn = None
            mne = None
            
            if choose == "tài" or choose == "xỉu":
                if(total >= 11 and total <= 18):
                    ans = "tài"
                else:
                    ans = "xỉu"
                    
                if(ans == choose):
                    result = 'win'
                    mn = int(bet * tilethang)
                    mne = int(mn + money)
                else:
                    result = 'lose'
                    mn = int(bet)
                    mne = int(money - mn)
                
            if result == 'win':
                money += mn
            else:
                money -= mn
            
            msg = discord.Embed(title="🏮───「Tài Xỉu」───🏮",colour=ctx.author.color, description=
                f"**{name}** đã chọn: **{choose}**\n"
                f"Tổng xúc xắc: **Đang lắc**\n"
                f"Kết quả: **Chưa có**\n"
                f"Trạng thái: **Chưa có**\n"     
                f"Lắc...",
            )
            
            msg1 = discord.Embed(title="🏮───「Tài Xỉu」───🏮",colour=ctx.author.color, description=
                f"**{name}** đã chọn: **{choose}**\n"
                f"Tổng xúc xắc: **{number[0]}**\n"
                f"Kết quả: **Chưa có**\n"
                f"Trạng thái: **Chưa có**\n"
                f"{emoji[0]}"
            )
            
            msg2 = discord.Embed(title="🏮───「Tài Xỉu」───🏮",colour=ctx.author.color, description=
                f"**{name}** đã chọn: **{choose}**\n"
                f"Tổng xúc xắc: **{number[0]+number[1]}**\n"
                f"Kết quả: **Chưa có**\n"
                f"Trạng thái: **Chưa có**\n"
                f"{emoji[0]}  {emoji[1]}"
            )
            
            msg3 = discord.Embed(title="🏮───「Tài Xỉu」───🏮",colour=ctx.author.color, description=
                f"**{name}** đã chọn: **{choose}**\n"
                f"Tổng xúc xắc: **{total}**\n"
                f"Kết quả: **{ans}**\n"
                f"Trạng thái: {'lụm về' if result == 'win' else 'mất mẹ'} **{mn:,}** VNĐ\n"
                f"{emoji[0]}  {emoji[1]}  {emoji[2]}"
            )
            msg.set_footer(text = "veXus Copyright © 2024-2025", icon_url = "https://i.ibb.co/y063smH/veXus.png")
            msg1.set_footer(text = "veXus Copyright © 2024-2025", icon_url = "https://i.ibb.co/y063smH/veXus.png")
            msg2.set_footer(text = "veXus Copyright © 2024-2025", icon_url = "https://i.ibb.co/y063smH/veXus.png")
            msg3.set_footer(text = "veXus Copyright © 2024-2025", icon_url = "https://i.ibb.co/y063smH/veXus.png")
            
            msg.set_thumbnail(url="https://media.tenor.com/sUiwSBs8S6QAAAAj/dice-game.gif")
            msg1.set_thumbnail(url="https://media.tenor.com/sUiwSBs8S6QAAAAj/dice-game.gif")
            msg2.set_thumbnail(url="https://media.tenor.com/sUiwSBs8S6QAAAAj/dice-game.gif")
            msg3.set_thumbnail(url="https://luattriminh.vn/wp-content/uploads/2024/08/tai-xiu-online-la-gi-tinhay_org-1.png")
            
            msg = await ctx.reply(embed=msg)
            await asyncio.sleep(timedelay * 1)
            await msg.edit(embed=msg1)
            await asyncio.sleep(timedelay * 1)
            await msg.edit(embed=msg2)
            await asyncio.sleep(timedelay * 1)
            await msg.edit(embed=msg3)
        except Exception as e:
            await ctx.send(e)

async def setup(bot):
    await bot.add_cog(taixiu(bot))
