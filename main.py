import os
from fastapi import FastAPI, Request
import requests

app = FastAPI()

# URL Endpoint Hugging Face Space Anda yang baru
HF_API_URL = "https://andriandri-cs-komplain-bot.hf.space/predict"

@app.get("/")
def home():
    return {"status": "Server Jembatan Telegram Aktif!"}

@app.post("/telegram")
async def telegram_webhook(request: Request):
    try:
        data = await request.json()
        if "message" in data and "text" in data["message"]:
            chat_id = data["message"]["chat"]["id"]
            user_input = data["message"]["text"]
            
            # Kirim data teks ke Hugging Face secepat mungkin dengan timeout super pendek (1 detik)
            try:
                requests.post(HF_API_URL, json={"chat_id": chat_id, "text": user_input}, timeout=1)
            except requests.exceptions.Timeout:
                # Abaikan timeout karena Hugging Face memang butuh waktu untuk menerima thread background
                pass
    except Exception as e:
        print(f"Error pada jembatan: {e}")
        
    # KUNCI UTAMA: Langsung kembalikan status 200 OK ke Telegram dalam hitungan milidetik!
    return {"status": "ok"}
