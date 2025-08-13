import os

# Telegram API keys (Render env vars se read kare)
API_ID = int(os.getenv("API_ID", "24787577"))
API_HASH = os.getenv("API_HASH", "5aad49131167d306d1cd33ffc9e01ec5")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8331452592:AAErTvCCSdV0OewXy2JuopwrE1fWrZ6BoCY")

# MongoDB config
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://Immortal_X_Xwaifu:SagarGupta0902@waifu.bebbu8f.mongodb.net/?retryWrites=true&w=majority&appName=waifu")
MONGO_DB = os.getenv("MONGO_DB", "animebot")
MONGO_COLL = os.getenv("MONGO_COLL", "animes")

# Owner & Sudo IDs
OWNER_ID = 8318394890  # apna Telegram user ID yaha daalo
SUDO_USERS = [8318394890, 987654321]  # list of IDs jo /anime use kar sakte hain

# Helper to check admin access
def is_admin(user_id: int) -> bool:
    return user_id == OWNER_ID or user_id in SUDO_USERS
