import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ochl
import datetime as dt

crypto = "BTC"
currency = "USD"
start = dt.datetime(2021, 1, 1)
end = dt.datetime.now()
data = web.DataReader(f"{crypto}-{currency}", "yahoo", start, end)
# print(data.head(5))
# print(data.columns)
data = data[['Open', 'Close', 'High', 'Low']]
# print(data.head(5))

data.reset_index(inplace=True)
# print(data.head(5))
data['Date'] = data['Date'].map(mdates.date2num)
# print(data['Date'])

# Visualization
ax = plt.subplot()
ax.grid(True)
ax.set_title('Bitcoin Share Visualization ', color='blue', fontsize=30)
ax.set_axisbelow(True)
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='#FFFFFF')
ax.tick_params(axis='y', colors='#FFFFFF')
plt.xlabel('Dates', color="blue", fontsize=25)
plt.ylabel('Prices(Millions)', color="blue", fontsize=25)

candlestick_ochl(ax, data.values, width=0.6, colorup="#00FF00")

ax.xaxis_date()
plt.show()
