import pandas_datareader as web
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

currency = "USD"

metric = "Close"

crypto = ["BTC", "ETH", "LTC", "BCH", "ADA"]
colNames = []
first = True
start = dt.datetime(2021, 1, 1)
end = dt.datetime.now()

for ticker in crypto:
    data = web.DataReader(f'{ticker}-{currency}', "yahoo", start, end)

    if first:
        combined = data[[metric]].copy()
        colNames.append(ticker)
        combined.columns = colNames
        first = False


    else:
        combined = combined.join(data[metric])
        colNames.append(ticker)
        combined.columns = colNames
ax = plt.axes()

for ticker in crypto:
    ax.plot(combined[ticker], label=ticker)
ax.legend(loc="upper center")
combined = combined.pct_change().corr(method="pearson")
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.set_title('CRYPTOCURRENCIES SHARE ANALYSIS', color="blue", fontsize=25)
ax.tick_params(axis='x', colors='#FFFFFF')
ax.tick_params(axis='y', colors='#FFFFFF')
plt.show()


"""sns.heatmap(combined, cmap="coolwarm", cbar=False, annot=True, ax=ax, cbar_kws={'label': 'Color range 0 to 1'})
ax.set_title('CRYPTOCURRENCIES SHARE ANALYSIS', color="blue", fontsize=25)
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='#FFFFFF')
ax.tick_params(axis='y', colors='#FFFFFF')
plt.show()"""
