import requests
import pandas as pd

url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?date=20231001&stockNo=2330'
#url = 'https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL'

response = requests.get(url)
#data = pd.DataFrame.from_dict(response.json(), orient='columns')
data = pd.DataFrame(response, orient='columns')

print(data)
#print(data[data['Code']=='2330'])