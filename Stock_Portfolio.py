import matplotlib.pyplot as plt
import pandas_datareader as web
import datetime as dt

tickers = ["FB", "TSLA", "AXIS", "HDFCBANK"]
amount = [3, 7, 9, 10]
prices = []
total = []
start = dt.datetime(2021, 1, 1)
end = dt.datetime.now()

for ticker in tickers:
    df = web.DataReader('FB', 'yahoo', start, end)
    price = df[-1:]['Close'][0]
    prices.append(price)
    index = tickers.index(ticker)
    total.append(price * amount[index])

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.set_title('Stock Portfolio Visualizer', color="white", fontsize=20)
ax.tick_params(axis='x', color='white')
ax.tick_params(axis='y', color='white')
_, texts, _ = ax.pie(total, labels=tickers, autopct="%1.1f%%", pctdistance=0.8)
[text.set_color('white') for text in texts]
my_circle = plt.Circle((0, 0), 0.66, color='black')
plt.gca().add_artist(my_circle)
ax.text(-2, 1, 'PORTFOLIO OVERVIEW', color='yellow', fontsize=15, verticalalignment='center',
        horizontalalignment='center')
ax.text(-2, 0.75, f'Total USD Amount: {sum(total):.2f} $', color='yellow', fontsize=12, verticalalignment='center',
        horizontalalignment='center')
counter = 0.15
for ticker in tickers:
    ax.text(-2, 0.75 - counter, f'{ticker}: {total[tickers.index(ticker)]:.2f} $', color='yellow', fontsize=12,
            verticalalignment='center', horizontalalignment='center')
    counter += 0.20

plt.show()
