import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL Endpoint Hugging Face Space Anda
HF_API_URL = "https://andriandri-cs-komplain-bot.hf.space/predict"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Server Jembatan Vercel Aktif!"})

@app.route("/telegram", methods=["POST"])
def telegram_webhook():
    try:
        data = request.get_json()
        
        # Memastikan data berasal dari chat Telegram asli
        if data and "message" in data and "text" in data["message"]:
            # 1. Ambil ID asli pengguna Telegram yang mengirim pesan
            chat_id = data["message"]["chat"]["id"]
            # 2. Ambil teks asli yang diketik pengguna di Telegram
            user_input = data["message"]["text"]
            
            # KUNCI PERBAIKAN: Kirim 'chat_id' dan 'text' ASLI ke Hugging Face, bukan angka 123456789!
            try:
                requests.post(HF_API_URL, json={"chat_id": chat_id, "text": user_input}, timeout=1)
                print(f"Berhasil mengoper pesan asli dari {chat_id} ke Hugging Face")
            except requests.exceptions.Timeout:
                pass
                
    except Exception as e:
        print(f"Error pada jembatan: {e}")
        
    return jsonify({"status": "ok"}), 200
# Baris penyelamat: mengekspos aplikasi ke serverless handler Vercel
handler = app
