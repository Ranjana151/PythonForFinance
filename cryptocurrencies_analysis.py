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

"""plt.yscale('log')
for ticker in crypto:
    plt.plot(combined[ticker], label=ticker)

plt.legend(loc="upper right")"""
combined = combined.pct_change().corr(method="pearson")
sns.heatmap(combined, cmap="coolwarm", annot=True)
plt.show()
