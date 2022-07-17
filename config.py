#Im Lazy to make Proper Database :)


API_ID   : int = 10101001
API_HASH : str = 'str10101010'
# Get your api hash and id here https://my.telegram.org/

DISCORD_SELFBOT_TOKEN : str = 'discordaccounttoken' 
# you can use real bot token too

TELEGRAM_BOT_TOKEN :    str = '101010:telegrambottoken'
# https://t.me/BotFather
# You can use telegram session string
# replace Bot.py token to session_string
# TelegramBot = Client("any_name_here",api_id=api_id,api_hash=api_hash,session_string=TELEGRAM_BOT_TOKEN,in_memory=True)




CHANNEL_LIST       : List[int] = [10101001]
"""
CHANNEL_LIST:
    FROM DISCORD:
        - Turn on discord developer mode and copy channel id
        - be sure that you can view the channel
"""
CHANNEL_GROUPCHATS : List[int] = [10101001]
"""
CHANNEL_GROUPCHATS:
    FROM TELEGRAM:
        - list of group chats you want to send
        - use miss_rose_bot command /id if you wanna get group chat id
"""
