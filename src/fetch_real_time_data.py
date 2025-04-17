import os
import pandas as pd
from alpaca_trade_api.rest import REST
from dotenv import load_dotenv
from datetime import datetime

# Load API keys from .env file
load_dotenv()
API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"

# Initialize Alpaca API connection
api = REST(API_KEY, SECRET_KEY, BASE_URL)

# Function to fetch only the latest stock price (for use in other scripts)
def get_latest_price(symbol):
    """
    Fetches and returns the latest stock price for a given symbol.
    :param symbol: Stock ticker (e.g., "AAPL")
    :return: Latest trade price (float)
    """
    try:
        latest_trade = api.get_latest_trade(symbol)
        last_price = latest_trade.price
        print(f"✅ {symbol} - Latest Price: ${last_price} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return last_price
    except Exception as e:
        print(f"❌ Error fetching latest price for {symbol}: {e}")
        return None

# Function to continuously fetch and log stock data (for real-time tracking)
def fetch_real_time_stock_data(symbol, interval=5):
    """
    Fetches real-time stock price and logs every request (even if price doesn't change).
    :param symbol: Stock ticker (e.g., "AAPL")
    :param interval: Time interval in seconds for fetching data
    """
    file_path = f"data/{symbol}_real_time_data.csv"
    
    # Initialize CSV file if it does not exist
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=["timestamp", "last_trade_price"])
        df.to_csv(file_path, index=False)

    try:
        while True:
            last_price = get_latest_price(symbol)
            if last_price is None:
                continue

            # Generate a fresh timestamp for every request
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Append new trade data to CSV (logs every request, even if price is unchanged)
            df = pd.read_csv(file_path)
            new_data = pd.DataFrame({"timestamp": [timestamp], "last_trade_price": [last_price]})
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_csv(file_path, index=False)

            print(f"✅ {symbol} - Logged Price: ${last_price} at {timestamp}")

            # Wait for the next interval
            import time
            time.sleep(interval)

    except Exception as e:
        print(f"❌ Error fetching real-time data: {e}")

# Example Usage
if __name__ == "__main__":
    stock_symbol = "AAPL"  # Example stock ticker
    fetch_real_time_stock_data(stock_symbol, interval=5)

