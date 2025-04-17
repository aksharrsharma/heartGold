
import time
from fetch_real_time_data import get_latest_price  # Now correctly importing the function
from alpaca_trade import buy_stock, sell_stock, check_positions

# Stock to trade
SYMBOL = "AAPL"

# Set buy/sell thresholds
BUY_THRESHOLD = -1.0  # Buy if price drops 1%
SELL_THRESHOLD = 1.0  # Sell if price increases 1%

# Store last price
last_price = None

def trade_logic():
    global last_price

    while True:
        latest_price = get_latest_price(SYMBOL)  # Fetch real-time stock price
        
        if latest_price is None:
            print("⚠️ No price data available, retrying...")
            time.sleep(5)
            continue

        print(f"📊 Current {SYMBOL} Price: ${latest_price}")

        # If first run, store the initial price
        if last_price is None:
            last_price = latest_price

        # Calculate percentage change
        price_change = ((latest_price - last_price) / last_price) * 100

        # Trading logic
        if price_change <= BUY_THRESHOLD:
            print(f"🔽 {SYMBOL} dropped by {price_change:.2f}%, BUYING...")
            buy_stock(SYMBOL, 1)  # Buy 1 share
            last_price = latest_price  # Update last price

        elif price_change >= SELL_THRESHOLD:
            print(f"🔼 {SYMBOL} increased by {price_change:.2f}%, SELLING...")
            sell_stock(SYMBOL, 1)  # Sell 1 share
            last_price = latest_price  # Update last price

        time.sleep(5)  # Check every 5 seconds

# Run trading logic
if __name__ == "__main__":
    trade_logic()
#python src/trade_bot.py