import os
import pandas as pd
from alpaca_trade_api.rest import REST
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"

# Initialize Alpaca API connection
api = REST(API_KEY, SECRET_KEY, BASE_URL)

# Function to fetch historical stock data
def fetch_historical_stock_data(symbol, start_date, end_date, timeframe="1Day"):
    """
    Fetches historical stock data from Alpaca and saves it as a CSV file.
    :param symbol: Stock ticker (e.g., "AAPL")
    :param start_date: Start date (YYYY-MM-DD)
    :param end_date: End date (YYYY-MM-DD)
    :param timeframe: Time interval (default: "1Day")
    """
    try:
        # Fetch historical bars
        bars = api.get_bars(symbol, timeframe, start=start_date, end=end_date).df

        # Create data folder if it doesn't exist
        os.makedirs("data", exist_ok=True)

        # Save data to CSV
        file_path = f"data/{symbol}_historical_data.csv"
        bars.to_csv(file_path)
        print(f"✅ Data for {symbol} saved to {file_path}")

    except Exception as e:
        print(f"❌ Error fetching data for {symbol}: {e}")

# Example Usage
if __name__ == "__main__":
    stock_symbol = "AAPL"  # Example stock ticker
    fetch_historical_stock_data(stock_symbol, "2023-01-01", "2024-01-01")
