from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7319641531:AAFxJObCtlTv4KuwJH4i26fGgzZI8J0SmEg"  # Yeni token
CHAT_ID = "-1002562052036"  # Yeni chat ID

@app.route('/', methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return "OK", 200

    data = request.get_json()
    print(data)
    message = data.get("message", "Mesaj bulunamadı")
    print(message)
    send_message_to_telegram(message)
    return {"status": "ok"}, 200

def send_message_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)