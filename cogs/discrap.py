from selfcord.ext import commands
from utils import embed, send_message, content
#config 
from config import CHANNEL_LIST,CHANNEL_GROUPCHATS


class DISCRAP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        CHECK IF CHAT IN LIST
        """
        if message.channel.id not in CHANNEL_LIST:
            return
        """
        WORK AROUND
        """
        ctx = message.content or ""

        if message.embeds:
            message = await embed(message)
            message = f"{ctx}\n{message}"
            for to_send in CHANNEL_GROUPCHATS:
                await send_message(to_send, message)

        elif message.content:
            for to_send in CHANNEL_GROUPCHATS:
                message = await content(message)
                await send_message(to_send, message)


async def setup(bot):
    """
    IMPORTANT:
        - be sure your class name is enough to other cogs from different folder

    bot.add_cog(CLASS_NAME(bot))
    """
    await bot.add_cog(DISCRAP(bot))
