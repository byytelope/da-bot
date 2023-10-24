# pyright: strict

import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = str(os.environ.get("BOT_TOKEN"))
GUILD_ID = discord.Object(id=835682783338561549)


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix=".")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


bot.run(TOKEN)
