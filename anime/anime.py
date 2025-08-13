# anime.py
from pyrogram import filters
from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB, MONGO_COLL, OWNER_ID, SUDO_USERS

mongo = MongoClient(MONGO_URI)
db = mongo[MONGO_DB]
collection = db[MONGO_COLL]

def is_sudo(user_id: int) -> bool:
    return user_id == OWNER_ID or user_id in SUDO_USERS

def register_handlers(app):

    # .anime - Add/Update anime (Owner/Sudo only)
    @app.on_message(filters.command("anime", prefixes=".") & filters.private)
    async def add_anime(client, message):
        if not is_sudo(message.from_user.id):
            return await message.reply_text("❌ Tumhe ye command use karne ka access nahi hai.")

        if not message.reply_to_message or not message.text:
            return await message.reply_text("ℹ Reply with image and text: `.anime Name - channel_link`")

        try:
            text = message.text.split(" ", 1)[1]
            name, link = text.split("-", 1)
            name, link = name.strip().lower(), link.strip()

            if not message.reply_to_message.photo:
                return await message.reply_text("❌ Please reply to a photo.")

            file_id = message.reply_to_message.photo.file_id

            collection.update_one(
                {"name": name},
                {"$set": {"link": link, "file_id": file_id}},
                upsert=True
            )

            await message.reply_text(f"✅ Anime `{name}` saved/updated successfully.")
        except Exception as e:
            await message.reply_text(f"⚠ Error: {e}")

    # /anime - Search anime
    @app.on_message(filters.command("anime", prefixes="/"))
    async def search_anime(client, message):
        if len(message.command) < 2:
            return await message.reply_text("ℹ Usage: `/anime anime_name`")

        name = " ".join(message.command[1:]).lower()
        anime = collection.find_one({"name": name})

        if not anime:
            return await message.reply_text("❌ Anime not found.")

        await message.reply_photo(
            photo=anime["file_id"],
            caption=f"📺 **{name.title()}**\n🔗 [Watch Here]({anime['link']})",
        )

    # /rmchannel - Update channel link
    @app.on_message(filters.command("rmchannel", prefixes="/"))
    async def update_channel(client, message):
        if not is_sudo(message.from_user.id):
            return await message.reply_text("❌ Tumhe ye command use karne ka access nahi hai.")

        if len(message.command) < 3:
            return await message.reply_text("ℹ Usage: `/rmchannel anime_name new_channel_link`")

        name = message.command[1].lower()
        new_link = message.command[2]

        result = collection.update_one({"name": name}, {"$set": {"link": new_link}})

        if result.modified_count:
            await message.reply_text(f"✅ Channel link updated for `{name}`.")
        else:
            await message.reply_text(f"❌ `{name}` not found in database.")
