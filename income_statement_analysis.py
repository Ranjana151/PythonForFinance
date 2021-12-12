import matplotlib.pyplot as plt
import requests

company = "AAPL"
years = 10
api_key = "bbed2d408d3f5c9ae5247358d2dab598"
income_statement = requests.get(
    f'https://financialmodelingprep.com//api/v3/income-statement/{company}?limit={years}&apikey={api_key}')
income_statement = income_statement.json()
columns = income_statement[0].keys()
revenues = list(reversed([income_statement[i]['revenue'] for i in range(len(income_statement))]))
profits = list(reversed([income_statement[i]['grossProfit'] for i in range(len(income_statement))]))
ax = plt.axes()
ax.plot(revenues, label="Revenues")
ax.plot(profits, label="Profit")
ax.legend(loc="upper center")
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='#FFFFFF')
ax.tick_params(axis='y', colors='#FFFFFF')
ax.set_title('Apple Company Income Statement Analysis ', color='blue', fontsize=30)

plt.show()
