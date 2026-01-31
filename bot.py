from pyrogram import Client, filters
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
STREAM_SITE = "https://cinema-hub-stream.onrender.com"

app = Client(
    "cinema_hub_stream_bot",
    bot_token=BOT_TOKEN
)

@app.on_message(filters.video | filters.document)
async def give_link(client, message):
    file_id = message.video.file_id if message.video else message.document.file_id
    link = f"{STREAM_SITE}/watch/{file_id}"

    await message.reply_text(
        f"🎬 Streaming Link Ready\n\n{link}",
        disable_web_page_preview=True
    )

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "👋 Movie ya video bhejo.\n"
        "Main tumhe streaming link de dunga."
    )

app.run()