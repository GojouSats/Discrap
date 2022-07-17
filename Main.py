import asyncio
from pyrogram import Client
from Bot import TelegramBot
from pyrogram import idle
from selfcord.ext import commands
from config import DISCORD_SELFBOT_TOKEN


bot = commands.Bot('prefix_command_symbol_or_name', self_bot=True)
"""
commands prefix for later use:
  - if you want more cogs
"""

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
    await TelegramBot.start()
    print('Bot Started')
    


    


if __name__ == "__main__":
    bot.run(DISCORD_SELFBOT_TOKEN)
