import requests
import json

class TWSEStock:
    def __init__(self, symbol, date):
        self.symbol = symbol
        self.date = date
        self.date_tw = str(int(date[0:4]) - 1911) + '/' + date[4:6] + '/' + date[6:8] # Change to Taiwan's Date format
        self.base_url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY'

    def get_json(self):
        url = self.base_url + '?response=json&date=' + self.date + '&stockNo=' + self.symbol
        return requests.get(url)
    
    def get_table(self):
        stock_table = {
            "日期": "",
            "成交股數": "",
            "成交金額": "",
            "開盤價": "",
            "最高價": "",
            "最低價": "",
            "收盤價": "",
            "漲跌價差": "",
            "成交筆數": ""
        }
        response = self.get_json()

        if response.status_code == 200:
            stocks = json.loads(response.text)

            try:
                stock_exit = 0
                for stock in (stocks['data']):
                    stock_exit += 1
                    if self.date_tw in stock:
                        stock_table["日期"] = stock[0]
                        stock_table["成交股數"] = stock[1]
                        stock_table["成交金額"] = stock[2]
                        stock_table["開盤價"] = stock[3]
                        stock_table["最高價"] = stock[4]
                        stock_table["最低價"] = stock[5]
                        stock_table["收盤價"] = stock[6]
                        stock_table["漲跌價差"] = stock[7]
                        stock_table["成交筆數"] = stock[8]
                        return stock_table
                
                if stock_exit == 0:
                    return None
            except (KeyError, IndexError):
                return None
        else:
            return None
        
if __name__ == "__main__":
    symbol = "2330"
    date = "20231004"

    stock_date = TWSEStock(symbol, date)
    stock = stock_date.get_table()

    if stock is not None:
        print(stock)
    else:
        print(f"Failed to retrieve stock: {symbol}.")