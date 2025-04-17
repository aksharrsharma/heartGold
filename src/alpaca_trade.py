import os
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()
API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = os.getenv("ALPACA_BASE_URL")

# Initialize Alpaca API
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version="v2")

# Function to check buying power
def check_account_info():
    account = api.get_account()
    print(f"💰 Account Balance: ${account.cash}")
    print(f"📈 Portfolio Value: ${account.portfolio_value}")
    print(f"🔹 Trading Status: {account.trading_blocked}")

# Function to place a market buy order
def buy_stock(symbol, qty):
    try:
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side="buy",
            type="market",
            time_in_force="gtc"
        )
        print(f"✅ Placed BUY order for {qty} shares of {symbol}")
    except Exception as e:
        print(f"❌ Error placing buy order: {e}")

# Function to place a market sell order
def sell_stock(symbol, qty):
    try:
        api.submit_order(
            symbol=symbol,
            qty=qty,
            side="sell",
            type="market",
            time_in_force="gtc"
        )
        print(f"✅ Placed SELL order for {qty} shares of {symbol}")
    except Exception as e:
        print(f"❌ Error placing sell order: {e}")

# Function to check current positions
def check_positions():
    positions = api.list_positions()
    if positions:
        for position in positions:
            print(f"📊 {position.qty} shares of {position.symbol} at ${position.current_price}")
    else:
        print("⚠️ No open positions.")

# Run account check
if __name__ == "__main__":
    check_account_info()
