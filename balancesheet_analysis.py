import requests
import matplotlib.pyplot as plt

api_key = "bbed2d408d3f5c9ae5247358d2dab598"
company = "FB"
year = 8
balance_sheet = requests.get(
    f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?period =quarterly&limit={year}&apikey={api_key}')
balance_sheet = balance_sheet.json()

Parmaters = balance_sheet[0].keys()

total_current_asset = balance_sheet[0]['totalCurrentAssets']
print(f"Total Current assets of {company}:{total_current_asset}")

total_current_liabilities = balance_sheet[0]['totalCurrentLiabilities']
print(f"Total Current  of Liabilities {company}:{total_current_liabilities}")

asset_q1 = balance_sheet[4]['totalAssets']
asset_q2 = balance_sheet[3]['totalAssets']
asset_q3 = balance_sheet[2]['totalAssets']
asset_q4 = balance_sheet[1]['totalAssets']
asset_data = [asset_q1, asset_q2, asset_q3, asset_q4]
asset_data = [x / 1000000000 for x in asset_data]
plt.style.use('dark_background')
plt.bar([1, 2, 3, 4], asset_data, color='green')
plt.title(f"Quarterly total Assets of {company}")
plt.xlabel("Quarters")
plt.ylabel("Total Assets in (billions USD)")
plt.xticks([1, 2, 3, 4], ['Q1', 'Q2', 'Q3', 'Q4'])
plt.show()
