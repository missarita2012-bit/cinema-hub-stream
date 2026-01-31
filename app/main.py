from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from pyrogram.types import Message
from app.telegram import tg
import asyncio

app = FastAPI(title="Cinema Hub")
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
async def start_bot():
    await tg.start()

@app.on_event("shutdown")
async def stop_bot():
    await tg.stop()

@app.get("/")
def home():
    return {"status": "Cinema Hub Streaming Website Running"}

@app.get("/watch/{file_id}", response_class=HTMLResponse)
def watch_page(request: Request, file_id: int):
    return templates.TemplateResponse(
        "watch.html",
        {"request": request, "file_id": file_id}
    )

# 🔥 STREAM ROUTE (VLC / MX / Browser)
@app.get("/stream/{file_id}")
async def stream(file_id: int):
    try:
        msg: Message = await tg.get_messages(chat_id=None, message_ids=file_id)
        if not msg or not msg.video:
            raise HTTPException(404, "Video not found")

        return StreamingResponse(
            msg.stream_video(),
            media_type="video/mp4"
        )
    except Exception as e:
        raise HTTPException(500, str(e))

# ⬇ DOWNLOAD ROUTE
@app.get("/download/{file_id}")
async def download(file_id: int):
    try:
        msg: Message = await tg.get_messages(chat_id=None, message_ids=file_id)
        if not msg or not msg.video:
            raise HTTPException(404, "Video not found")

        headers = {
            "Content-Disposition": f'attachment; filename="{msg.video.file_name or "video.mp4"}"'
        }

        return StreamingResponse(
            msg.stream_video(),
            headers=headers,
            media_type="application/octet-stream"
        )
    except Exception as e:
        raise HTTPException(500, str(e))