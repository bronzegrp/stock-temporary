import requests
import json

api_key = 'xxxxxxxxxxx'
stock_of_choice = 'TSLA'

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_of_choice}&apikey={api_key}'

stock = requests.get(url=url)

print(stock.status_code)

print('\n')

json_data = stock.json()
print(json_data.keys())

print(type(json_data['Meta Data']))
print(type(json_data['Time Series (Daily)']))

print(json_data['Meta Data'].keys())




