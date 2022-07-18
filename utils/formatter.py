async def embed(message):
    """
    EMBED FORMATTER:
        - format an embed message
        - telegram can only embed 1 image
        - lazy to make photo sender :)
    """
    message = message.embeds[0]
    if message.title:
        title = message.title or ""

    if message.description:
        desc = message.description or ""

    if message.image.url:
        image = message.image.url
        format_message = f"{title}\n{desc} [ ]({image})"
    else:
        format_message = f"{title}\n{desc}"

    return format_message


async def content(message):
    """
    CONTENT FORMAT:
        - if message doenst have image or no
        - only fetch 1 image for now, because telegram does not auto folder image link
    """
    if message.attachments:
        format_message = f"{message.content} [ ]({message.attachments[0]})"
    else:
        format_message = f"{message.content}"
        
    return format_message
