import yfinance as yf

# Get the EUR/USD currency pair
eur_usd = yf.Ticker("EURUSD=X")

# Get the historical data for the previous week
historical_data = eur_usd.history(period="1wk")

# Get the closing price for the previous week
closing_price = historical_data["Close"][-1]

print(f"The closing price of EUR/USD for the previous week was {closing_price}")