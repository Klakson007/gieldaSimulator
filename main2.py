import yfinance as yf
import string
print("sell")
# Get the EUR/USD currency pair
eur_usd = yf.Ticker("EURUSD=X")
info = eur_usd.info
print("sell")
buy_price = info['regularMarketPrice']
sell_price = str(info['regularMarketPreviousClose'])
print("sell")
# Get the historical data for the previous week
historical_data = eur_usd.history(period="1wk")
print("sell")
# Get the closing price for the previous week
closing_price = historical_data["Close"][-1]
str(sell_price)
