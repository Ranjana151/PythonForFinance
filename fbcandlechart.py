import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick_ochl

# date
start = dt.datetime(2021, 1, 1)
end = dt.datetime.now()

data = web.DataReader('FB', 'yahoo', start, end)
# print(data.head())
# print(data.columns)

# Reformatting data

data = data[['Open', 'Close', 'High', 'Low']]
# print(data.head(5))

data.reset_index(inplace=True)
# print(data.head(5))
data['Date'] = data['Date'].map(mdates.date2num)
# print(data['Date'])

# Visualization
ax = plt.subplot()
ax.grid(True)
ax.set_title('FB Share prize ', color='#FFFFFF')
ax.set_axisbelow(True)
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='#FFFFFF')
ax.tick_params(axis='y', colors='#FFFFFF')
ax.xaxis_date()

candlestick_ochl(ax, data.values, width=0.5, colorup="#00FF00")
plt.show()
