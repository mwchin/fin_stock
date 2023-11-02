import requests
from bs4 import BeautifulSoup

class TWYahooStock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.base_url = "https://tw.stock.yahoo.com/quote/"
 
    def get_html(self):
        return requests.get(self.base_url + self.symbol)

    def get_name(self):
        response = self.get_html()

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            try:
                stock_name = soup.find_all("h1")[1]
                return stock_name.get_text()
            except (KeyError, IndexError):
                return None
        else:
            print("Failed to retrieve stock name.")
            return None
        
    def get_price(self):
        response = self.get_html()

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            try:
                stock_price = soup.select('.Fz\(32px\)')[0]
                return float(stock_price.get_text())
            except (KeyError, IndexError):
                return None
        else:
            print("Failed to retrieve stock price.")
            return None

if __name__ == "__main__":
    symbol = "2330"  # Change to the Stock Code. (ex. 2330, AAPL)
    stock = TWYahooStock(symbol)
    stock_name = stock.get_name()
    stock_price = stock.get_price()

    if stock_price is not None:
        print(f"The current price of {stock_name} {symbol} is ${stock_price:.2f}")
    else:
        print(f"Failed to retrieve the price for {symbol}")
