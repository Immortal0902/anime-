# general.py
import time
from pyrogram import filters

def register_handlers(app):

    # /start command
    @app.on_message(filters.command("start"))
    async def start_command(client, message):
        await message.reply_text(
            f"👋 Hello {message.from_user.first_name}!\n\n"
            "Main ek Anime Link Finder bot hoon.\n"
            "📌 Commands dekhne ke liye `/help` use karo."
        )

    # /ping command
    @app.on_message(filters.command("ping"))
    async def ping_command(client, message):
        start = time.time()
        msg = await message.reply_text("🏓 Pong...")
        end = time.time()
        await msg.edit_text(f"🏓 Pong! `{round((end - start) * 1000)} ms`")

    # /help command
    @app.on_message(filters.command("help"))
    async def help_command(client, message):
        help_text = (
            "📜 **Bot Commands**\n\n"
            "**For Everyone:**\n"
            "`/start` - Bot start kare\n"
            "`/ping` - Check bot speed\n"
            "`/anime <name>` - Anime ka link & image dega\n\n"
            "**For Owner/Sudo:**\n"
            "`.anime <name> - <channel_link>` (reply to image) - Add/Update anime\n"
            "`/rmchannel <name> <new_link>` - Update channel link"
        )
        await message.reply_text(help_text)
