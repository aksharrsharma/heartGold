import yfinance as yf

# Test fetching Apple stock (AAPL) real-time data
symbol = "AAPL"
stock = yf.Ticker(symbol)

# Get the latest stock price
latest_price = stock.history(period="1m")["Close"].iloc[-1]
print(f"✅ {symbol} - Latest Price: ${latest_price}")
