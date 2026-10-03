import discord
from discord.ext import commands
import config

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=config.prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(config.token)