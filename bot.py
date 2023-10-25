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
async def on_ready() -> None:
    print(f"Logged in as {bot.user}")


@bot.command()
async def sync(ctx: commands.Context[commands.Bot]) -> None:
    synced = await bot.tree.sync()
    await ctx.send(f"Synced **{len(synced)}** command(s)")


@bot.tree.command(name="blud", description="What is blud waffling about?")
async def blud(interaction: discord.Interaction, member: discord.Member) -> None:
    await interaction.response.send_message(f"Blud {member.mention}")


class Bruh:
    def __init__(self):
        return


bot.run(TOKEN)
