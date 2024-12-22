import discord, random, asyncio
from discord.ext import commands

class baucua(commands.Cog):
    info = {
        "name": "baucua",
        "version": "1.0.0",
        "author": "tuanvu1202 convert Mirai",
        "description": "Game Bầu cua",
        "catogery": "Game",
        "usage": "[bầu/cua/tôm/cá/nai/gà] [tiền cược]",
    }

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def baucua(self, ctx, *args):
        try:
            # Kiểm tra input
            if len(args) < 2 or not args[1].isdigit():
                await ctx.send("[veXus] Hãy nhập đúng định dạng: [bầu/cua/tôm/cá/nai/gà] [tiền cược]")
                return

            money_bet = int(args[1])
            if money_bet <= 0:
                await ctx.send("[veXus] Tiền cược phải lớn hơn 0!")
                return

            slot_items = ["bầu", "cua", "tôm", "cá", "nai", "gà"]
            user_choice = args[0].lower()
            if user_choice not in slot_items:
                await ctx.send("[veXus] Lựa chọn không hợp lệ! Hãy chọn: bầu/cua/tôm/cá/nai/gà")
                return

            icon_map = {
                "bầu": ("bau", "🍐"),
                "cua": ("cua", "🦀"),
                "cá": ("ca", "🐟"),
                "nai": ("nai", "🦌"),
                "gà": ("ga", "🐓"),
                "tôm": ("tom", "🦞"),
            }
            itemm, icon = icon_map[user_choice]

            # Xử lý kết quả
            number = [random.choice(slot_items) for _ in range(3)]
            count = number.count(user_choice)

            # Debugging log
            print(f"Debug: number = {number}, itemm = {itemm}, count = {count}")

            # Gửi tin nhắn lắc xúc xắc dưới dạng Embed
            embed_shaking = discord.Embed(
                title="Bầu Cua",
                description="⏳ Hãy chờ trong giây lát để xem kết quả...",
                colour=discord.Color.yellow()
            )
            embed_shaking.set_image(url="https://i.imgur.com/dlrQjRL.gif")
            message = await ctx.send(embed=embed_shaking)
            await asyncio.sleep(6)

            # Sửa nội dung Embed để hiển thị kết quả
            if count > 0:
                multiplier = count
                winnings = money_bet * multiplier
                embed_result = discord.Embed(
                    title="Bầu Cua",
                    colour=ctx.author.color,
                    description=f"🌟 Kết quả: {', '.join([icon_map[item][1] for item in number])}\n"
                                f"🎉 Bạn thắng **{winnings:,}** VNĐ vì có {count} {icon}!"
                )
            else:
                embed_result = discord.Embed(
                    title="Bầu Cua",
                    colour=ctx.author.color,
                    description=f"🌟 Kết quả: {', '.join([icon_map[item][1] for item in number])}\n"
                                f"💸 Bạn thua **{money_bet:,}** VNĐ vì không có {icon}!"
                )

            embed_result.set_footer(text="veXus Copyright © 2024-2025", icon_url="https://i.ibb.co/y063smH/veXus.png")
            await message.edit(embed=embed_result)

        except Exception as e:
            print(f"Error: {type(e).__name__} - {e}")
            await ctx.send(f"[veXus] Đã xảy ra lỗi: {type(e).__name__} - {e}")

async def setup(bot):
    await bot.add_cog(baucua(bot))
