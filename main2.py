import yfinance as yf
data = yf.download(['GOOG','META'], period='1s')
data.head()
print(data)