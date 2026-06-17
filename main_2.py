import requests
import json
import datetime

from datetime import datetime,date,timedelta


todays_date = date.today()
yesterday = todays_date-timedelta(days=1)

formated_yesterday = yesterday.strftime('%Y-%m-%d')

print(todays_date)
print(yesterday)
print('\n')
str_today = todays_date.strftime('%A')
str_yesterday = yesterday.strftime('%A')

print(str_today)
print(str_yesterday)



api_key = 'CMAG9Q86Y425F8XY'
stock_of_choice = 'TSLA'

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_of_choice}&apikey={api_key}'

stock = requests.get(url=url)

print(stock.status_code)

print('\n')

json_data = stock.json()
print(json_data.keys())
print('\n')

stock_data = json_data['Time Series (Daily)']
print('\n')
print(type(formated_yesterday))
print(stock_data[formated_yesterday])
open_close_yesterday = stock_data[formated_yesterday]


def calculate_earnings ():
    global open_close_yesterday

    open_yesterday = float(open_close_yesterday['1. open'])
    close_yesterday = float(open_close_yesterday['4. close'])

    op_1 = close_yesterday-open_yesterday
    op_2 = op_1/open_yesterday
    op_3 = op_2*100
    return op_3.__round__(2)
print('\n')
print(calculate_earnings())

print(f'youre_up {calculate_earnings()}%')


