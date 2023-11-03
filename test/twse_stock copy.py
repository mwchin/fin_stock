import requests
import json

class TWSEStock:
    def __init__(self, symbol, date):
        self.symbol = symbol
        self.date = date
        self.base_url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY'

    def get_json(self):
        return requests.get(self.base_url + 'response=json&date=' + self.date + '&stockNo=' + self.symbol)
    
    def get_table(self):
        stock_table = {
            "Date": "",
            "Traded": "",
            "Price": "",
            "Open": "",
            "Highest": "",
            "Lowest": "",
            "Closed": "",
            "Diff": "",
            "Shares": ""
        }
        response = self.get_json()

        if response.status_code == 200:
            #stocks = json.loads(response.text)

            try:
                for stock in (response.text['data']):
                    if self.date in stock:
                        stock_table["Date"] = stock[0]
                        return stock_table
            except (KeyError, IndexError):
                return None
        else:
            print(f"Failed to retrieve stock: {self.symbol}.")
            return None
        
# if __name__ == "__main__":
#     symbol = "2330"
#     date = "20231001"

#     stock = TWSEStock(date, symbol)

#     if stock is not None:
#         print(stock.get_table())
#     else:
#         print(f"Failed to retrieve {symbol}")




url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20231001&stockNo=2330'

response = requests.get(url)
s = json.loads(response.text)

for data in (s['data']):
    if '112/10/04' in data:
      print(data)
