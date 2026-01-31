from pyrogram import Client, filters
import os

# ========= REQUIRED ENV VARIABLES =========
# BOT_TOKEN  -> BotFather se
# API_ID     -> my.telegram.org se
# API_HASH   -> my.telegram.org se

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

# ========= STREAMING WEBSITE =========
STREAM_SITE = "https://cinema-hub-stream.onrender.com"

# ========= PYROGRAM CLIENT =========
app = Client(
    "cinema_hub_stream_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ========= START COMMAND =========
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "👋 Movie / video bhejo ya forward karo.\n\n"
        "Main turant tumhe streaming link de dunga 🎬"
    )

# ========= HANDLE VIDEO / DOCUMENT =========
@app.on_message(filters.video | filters.document)
async def give_streaming_link(client, message):
    if message.video:
        file_id = message.video.file_id
    else:
        file_id = message.document.file_id

    link = f"{STREAM_SITE}/watch/{file_id}"

    await message.reply_text(
        f"🎬 **Streaming Link Ready**\n\n{link}",
        disable_web_page_preview=True
    )

# ========= RUN BOT =========
app.run()