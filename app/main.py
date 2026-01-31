from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI(title="Cinema Hub")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home():
    return {"status": "Cinema Hub Streaming Server Running"}

@app.get("/watch/{file_id}", response_class=HTMLResponse)
def watch_page(request: Request, file_id: int):
    return templates.TemplateResponse(
        "watch.html",
        {"request": request, "file_id": file_id}
    )