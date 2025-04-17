import os
from alpaca_trade_api.rest import REST
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = os.getenv("ALPACA_BASE_URL")

# Connect to Alpaca API
api = REST(API_KEY, SECRET_KEY, BASE_URL)

# Fetch account details
account = api.get_account()
print(f"Account Status: {account.status}")
