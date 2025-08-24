import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
USDA_API_KEY = os.getenv("USDA_API_KEY")
BASE_URL = os.getenv("BASE_URL","https://api.nal.usda.gov/fdc/v1")

if not TELEGRAM_BOT_TOKEN or not USDA_API_KEY:
    raise ValueError("Missing API keys")
