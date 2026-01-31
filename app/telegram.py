from pyrogram import Client
from app.config import API_ID, API_HASH, BOT_TOKEN

tg = Client(
    "cinema_hub_stream",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True
)