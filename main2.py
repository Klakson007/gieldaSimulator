'''
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
closing_price = historical_data["Close"][2]
str(sell_price)
print(sell_price)
'''
import plotly.graph_objs as go
import yfinance as yf
data = yf.download(tickers='GOOG', period = '5d', interval = '15m', rounding= True)
fig = go.Figure()
fig.add_trace(go.Candlestick(x=data.index,open = data['Open'], high=data['High'], low=data['Low'], close=data['Close'], name = 'market data'))
fig.update_layout(title = 'Google share price', yaxis_title = 'Stock Price (USD)')
fig.update_xaxes(
rangeslider_visible=True,
rangeselector=dict(
buttons=list([
dict(count=15, label='15m', step="minute", stepmode="backward"),
dict(count=45, label='45m', step="minute", stepmode="backward"),
dict(count=1, label='1h', step="hour", stepmode="backward”),
dict(count=6, label='6h', step="hour", stepmode=”backward”),
dict(step=”all”)
])
)
)
fig.show()