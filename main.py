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
        if "message" in data and "text" in data["message"]:
            chat_id = data["message"]["chat"]["id"]
            user_input = data["message"]["text"]
            
            # Oper data teks ke Hugging Face dengan timeout super cepat (1 detik)
            try:
                requests.post(HF_API_URL, json={"chat_id": chat_id, "text": user_input}, timeout=1)
            except requests.exceptions.Timeout:
                # Abaikan timeout karena HF butuh waktu lama di background
                pass
    except Exception as e:
        print(f"Error pada jembatan: {e}")
        
    # KUNCI UTAMA: Langsung jawab OK ke Telegram dalam hitungan milidetik
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(debug=True)
