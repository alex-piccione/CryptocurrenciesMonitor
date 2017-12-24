from typing import Dict
from urllib.request import urlopen
from datetime import datetime
from bs4 import BeautifulSoup

from utils.FileWriter import FileWriter
from cryptocurrencies.entities import Exchange, Market


class WebScraper():

    def __init__(self, writer:FileWriter, filters=None) -> Dict[str, Exchange]:
        self.writer = writer
        self.filters = filters

    def get_data(self, filters=None) :

        try:
            base_url = "https://coinmarketcap.com"
            url = f"{base_url}/currencies/ripple/#markets"
            response = urlopen(url)
            bs = BeautifulSoup(response, "html5lib")

            exchanges = self._get_exchanges(bs)

            # how to filter a dictionary https://stackoverflow.com/questions/2844516/how-to-filter-a-dictionary-according-to-an-arbitrary-condition-function

            date = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")  # 'YYYY-MM-DD HH:mm:ss'
            self.writer.write(f"Date: {date}\n")

            for exchange in exchanges:
                self.writer.write(f"\n# {exchange.name}")
                for market in exchange.markets.values():
                    self.writer.write(f"\t{market.name}: {market.price}")

            return exchanges

        except Exception as error:
            self.writer.write(f"Error in {__name__}. {error}")
            print(f"Error in {__name__}. {error}")
            return 1  # Fatal error


    def _get_exchanges(self, bs: BeautifulSoup) -> Dict[str, Exchange]:

        # table: <table id="markets-table" class="table no-border table-condensed">
        table = bs.find("table", {"id":"markets-table"})
        if not table:
            raise Exception("table (id=markets-table) not found.")

        exchanges = {}

        tr_list = table.find_all("tr")[1:]
        for tr in tr_list:
            
            # get exchange from 2nd td <td><a href="/exchanges/bittrex/">Bittrex</a>
            # get rate from 3rd td <td><a href="https://bittrex.com/Market/Index?MarketName=BTC-XRP" target="_blank">XRP/BTC</a></td>
            # get price from <span class="price" data-usd="0.855996"

            ## todo: use specific methods to track errors

            td_list = tr.find_all("td")  ## todo: try to usetr.find_all("td")[1::2]
            exchange_name = td_list[1].get_text()
            market_currencies = td_list[2].get_text()   

            if ("exchanges" in self.filters and exchange_name not in self.filters["exchanges"]) or ("markets" in self.filters and market_currencies not in self.filters["markets"]):
                continue

            
            #usd_price = self._get_price(td_list[3])
            #if usd_price == 0:
            #    usd_price = self._get_price_from_tr(tr)
            usd_price = self._get_price_from_tr(tr)

            market = Market.parse(market_currencies, usd_price)            

            if exchange_name not in exchanges:
                exchanges[exchange_name] = Exchange(exchange_name)

            exchange = exchanges[exchange_name]            
            exchange.add_market(market)            

        return exchanges.values()

    def _get_price(self, td):
        ## todo: it fails because td contains new lines character (?!)
        price = 0

        try:
            price_span = td.find("span", {"class": "price"})                
            price = price_span["data-usd"]
        except Exception as error:
            self.writer.write(f"Error. Fail to load price from TD. {error}")
            print(f"Error. {error}")
        
        return price

    def _get_price_from_tr(self, tr):
        price = 0

        try:
            price_span = tr.find("span", {"class": "price"})                
            price = price_span["data-usd"]
        except Exception as error:
            self.writer.write(f"Error. Fail to load price from TR. {error}")
            print(f"Error. {error}")
        
        return price