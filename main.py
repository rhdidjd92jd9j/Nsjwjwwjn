import urllib.request
import urllib.parse
import json
import time

TOKEN = "7808674214:AAFzx0mRxBdUPv4Xnf8tW-dT-tPPVLIyayk"
API_URL = f"https://api.telegram.org/bot{TOKEN}/"

def get_updates(offset=None):
    url = f"{API_URL}getUpdates?timeout=100"
    if offset is not None:
        url += f"&offset={offset}"
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read()).get("result", [])

def send_message(chat_id, text):
    encoded_text = urllib.parse.quote(text)
    url = f"{API_URL}sendMessage?chat_id={chat_id}&text={encoded_text}"
    with urllib.request.urlopen(url):
        pass  # No response handling needed here

def main():
    print("🤖 Telegram bot started (Python 3.12 style)")
    offset = None
    while True:
        updates = get_updates(offset)
        for update in updates:
            message = update.get("message", {})
            chat_id = message.get("chat", {}).get("id")
            text = message.get("text", "")

            if chat_id and text:
                print(f"Received from user: {text}")
                send_message(chat_id, "I am alive")
                offset = update["update_id"] + 1
        time.sleep(1)

if __name__ == "__main__":
    main()
