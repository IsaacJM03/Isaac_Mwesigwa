import requests
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # Add this to your .env
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")      # Add this to your .env

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Message sent!")
    else:
        print(f"Failed: {response.text}")

if __name__ == "__main__":
    send_telegram_message("Hello from my Python Telegram bot!")
    
# import tweepy
# import logging
# from datetime import datetime
# from dotenv import load_dotenv
# import os

# load_dotenv()

# API_KEY = os.getenv("X_API_KEY")
# API_SECRET = os.getenv("X_API_SECRET")
# ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
# ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")

# logging.basicConfig(level=logging.INFO)

# auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

# def post_message(image_path):
#     message = f"Hello, world! The time is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
#     try:
#         media = api.media_upload(image_path)
#         api.update_status(status=message, media_ids=[media.media_id])
#         logging.info(f"Posted message with media: {message}")
#     except Exception as e:
#         logging.error(f"Error posting message with media: {e}")

# if __name__ == "__main__":
#     post_message("images.jpeg")

# def post_message():
#     message = f"Hello, world! The time is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
#     try:
#         api.update_status(message)
#         logging.info(f"Posted message: {message}")
#     except Exception as e:
#         logging.error(f"Error posting message: {e}")

# # Example: post a message now
# if __name__ == "__main__":
#     post_message()
    
# import requests

# url = "https://api.twitter.com/2/tweets"

# payload = {
#     "card_uri": "<string>",
#     "community_id": "1146654567674912769",
#     "direct_message_deep_link": "<string>",
#     "for_super_followers_only": False,
#     "geo": {"place_id": "<string>"},
#     "media": {
#         "media_ids": ["1146654567674912769"],
#         "tagged_user_ids": ["2244994945"]
#     },
#     "nullcast": False,
#     "poll": {
#         "duration_minutes": 5042,
#         "options": ["<string>"],
#         "reply_settings": "following"
#     },
#     "quote_tweet_id": "1346889436626259968",
#     "reply": {
#         "exclude_reply_user_ids": ["2244994945"],
#         "in_reply_to_tweet_id": "1346889436626259968"
#     },
#     "reply_settings": "following",
#     "text": "Learn how to use the user Tweet timeline and user mention timeline endpoints in the X API v2 to explore Tweet\u2026 https:\/\/t.co\/56a0vZUx7i"
# }
# headers = {
#     "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAMhc2wEAAAAAwISmQPlpXOtNkQkpfM5K%2Bf2VdlA%3DnCbRA4dLlyEa7jR9pyrFQ4kQNeZUlJDEPXo3WSPaKRLLf2LVS7",
#     "Content-Type": "application/json"
# }

# response = requests.request("POST", url, json=payload, headers=headers)

# print(response.text)