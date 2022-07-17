import re, asyncio
from Bot import TelegramBot as app
from pyrogram import enums
from pyrogram.errors import FloodWait, MessageEmpty, ChatAdminRequired

regex = re.compile(r"<[@!#&ta:@]+[\w]+[>:tTdDfFR\d]+")
everyhere = re.compile("@everyone|@here")


async def send_message(chat_id: int, message: str, pin: bool = False):
    """
    SEND_MESSAGE:
        - remove @mention #channel and epoch time
        - modify regex if you want to change it
    """
    everyone_here = re.sub(everyhere, "", message)
    message = re.sub(regex, "", everyone_here)

    try:
        to_send = await app.send_message(chat_id=chat_id, text=message,parse_mode=enums.ParseMode.MARKDOWN)
        if pin:
            print(to_send.id)
            await app.pin_chat_message(chat_id=chat_id, message_id=to_send.id)

        """
        HANDLE PYROGRAM EXCEPTION ERRORS
        """
    except FloodWait as e:
        await asyncio.sleep(e.value)
    except MessageEmpty:
        return
    except ChatAdminRequired:
        return
    except Exception as e:
        print(e)
