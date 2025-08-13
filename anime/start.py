from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text(
        f"Hello {message.from_user.mention} 👋\n"
        "Main aapke liye Anime channel search bot hoon.\n"
        "Anime ka naam bhejo aur main aapko link dunga."
    )

@Client.on_message(filters.command("ping"))
async def ping_cmd(client, message):
    from time import time
    start = time()
    msg = await message.reply_text("Pinging...")
    end = time()
    await msg.edit_text(f"Pong! `{round((end-start)*1000)}ms`")

@Client.on_message(filters.command("help"))
async def help_cmd(client, message):
    help_text = (
        "**Bot Commands:**\n"
        "/start - Bot start message\n"
        "/help - Help message\n"
        "/ping - Check bot status\n\n"
        "/anime <name> - Search saved anime link\n"
        ".anime <name>-<link> (with image) - Add anime (Owner/Sudo only)\n"
        "/rmchannel <name>-<new link> - Update anime link (Owner/Sudo only)"
    )
    await message.reply_text(help_text)
