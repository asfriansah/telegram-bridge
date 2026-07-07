import os
from flask import Flask, request, jsonify
import requests

# Nama variabel WAJIB 'app'
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
        if "message" in data and "text" in data["message"]:
            chat_id = data["message"]["chat"]["id"]
            user_input = data["message"]["text"]
            
            # Kirim data ke Hugging Face dengan timeout 1 detik agar Vercel bisa langsung merespons Telegram
            try:
                requests.post(HF_API_URL, json={"chat_id": chat_id, "text": user_input}, timeout=1)
            except requests.exceptions.Timeout:
                pass
    except Exception as e:
        print(f"Error pada jembatan: {e}")
        
    return jsonify({"status": "ok"}), 200
