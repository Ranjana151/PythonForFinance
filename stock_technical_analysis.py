import pandas_datareader as web
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd

start = dt.datetime(2021, 1, 1)
end = dt.datetime.now()
ticker = 'FB'
data = web.DataReader('FB', 'yahoo', start, end)

delta = data['Adj Close'].diff(1)
delta.dropna(inplace=True)

positive = delta.copy()
negative = delta.copy()

positive[positive < 0] = 0
negative[negative > 0] = 0

days = 14
average_gain = positive.rolling(window=days).mean()
average_loss = abs(negative.rolling(window=days).mean())
relative_strength = average_gain / average_loss
relative_strength_index = 100.0 - (100.0 / (1.0 + relative_strength))
combined = pd.DataFrame()
combined['Adj Close'] = data['Adj Close']
combined['RSI'] = relative_strength_index

plt.figure(figsize=(10, 6))
ax = plt.subplot(211)
ax.plot(combined.index, combined['Adj Close'], color='lightgray')
ax.set_title('Adjusted Close Price', color='white', fontsize=15)
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.grid(True)
ax.set_axisbelow(True)
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

ax1 = plt.subplot(212, sharex=ax)
ax1.plot(combined.index, combined['RSI'], color='lightgray')
ax1.set_facecolor('black')
ax1.figure.set_facecolor('#121212')
ax1.axhline(0, linestyle='--', color="#FF0000")
ax1.axhline(10, linestyle='--', color="#FFE536")
ax1.axhline(20, linestyle='--', color="yellow")
ax1.axhline(30, linestyle='--', color="#cccccc")
ax1.axhline(70, linestyle='--', color="#cccccc")
ax1.axhline(80, linestyle='--', color="yellow")
ax1.axhline(90, linestyle='--', color="#FFE536")
ax1.axhline(100, linestyle='--', color="#FF0000")

ax1.grid(False)
ax1.set_axisbelow(True)
ax1.tick_params(axis='x', colors='white')
ax1.tick_params(axis='y', colors='white')
ax.set_title('FB STOCK TECHNICAL ANALYSIS ', color="blue", fontsize=25)

plt.show()
