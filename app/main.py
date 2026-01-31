from fastapi import FastAPI

app = FastAPI(title="Cinema Hub")

@app.get("/")
def home():
    return {"status": "Cinema Hub Streaming Server Running"}