# main.py
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

# Import handlers
import anime
import general

app = Client("anime-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Register handlers
anime.register_handlers(app)
general.register_handlers(app)

print("✅ Bot is running...")
app.run()
