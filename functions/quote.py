import discord
import aiohttp
from discord.ext import commands

class Quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content.lower().strip() != "quote":
            return
        if not message.reference or not message.reference.message_id:
            return
        replied_message=await message.channel.fetch_message(
            message.reference.message_id
        )

        user=replied_message.author
        text=replied_message.content
        name=user.display_name
        image=user.display_avatar.url

        url="https://api.popcat.xyz/v2/quote"
        params={
            "image":image,
            "text":text,
            "name":name
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status != 200:
                    return
                image_data = await response.read()

        await message.channel.send(
            file=discord.File(
                __import__("io").BytesIO(image_data),
                filename="quote.png"
            )
        )

async def setup(bot):
    await bot.add_cog(Quote(bot))