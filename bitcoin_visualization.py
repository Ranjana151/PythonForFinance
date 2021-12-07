import pandas_datareader as web
import matplotlib.pyplot as plt
import mplfinance as mpf
import datetime as dt

crypto = "BTC"
currency = "USD"
start = dt.datetime(2021, 1, 1)
end = dt.datetime.now()
data = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
# print(data.head(5))
# print(data.columns)

mpf.plot(data, style="yahoo", type="candle", volume=True)
plt.show()
