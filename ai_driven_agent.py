import tweepy
import logging
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("X_API_KEY")
API_SECRET = os.getenv("X_API_SECRET")
ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")

logging.basicConfig(level=logging.INFO)

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def post_message(image_path):
    message = f"Hello, world! The time is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    try:
        media = api.media_upload(image_path)
        api.update_status(status=message, media_ids=[media.media_id])
        logging.info(f"Posted message with media: {message}")
    except Exception as e:
        logging.error(f"Error posting message with media: {e}")

if __name__ == "__main__":
    post_message("images.jpeg")