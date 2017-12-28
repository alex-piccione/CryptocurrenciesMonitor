from typing import Dict, List
from urllib.request import urlopen
from datetime import datetime
from bs4 import BeautifulSoup

from utils.FileWriter import FileWriter
from cryptocurrencies import currencies_utils
from cryptocurrencies.entities import *

url_coinmarketcap = "https://coinmarketcap.com" # used to obtain the list of Currencies, Exchanges, Markets


class WebScraper():

    def __init__(self, writer:FileWriter) -> Dict[str, Exchange]:
        self.writer = writer  


    def get_currency_pairs(self) -> List[str]:

        # todo: return data from cache/configuration then generate an update event when the load of fresh data contains changes
        ##return self._genearete_currency_pairs(currencies_from_cache)

        # load the currencies
        currencies = {}
        try:
            # todo: 
            response = urlopen(url_coinmarketcap) 
            bs = BeautifulSoup(response, "html5lib")

            # <table class="table dataTable no-footer" id="currencies" role="grid" style="width: 100%;">
            table = bs.find("table", {"id":"currencies"})

            # <span class="currency-symbol"><a href="/currencies/bitcoin/">BTC</a></span>
            # <a class="currency-name-container" href="/currencies/bitcoin/">Bitcoin</a>
            for row in table.tbody.find_all("tr"):                
                symbol = row.find(class_="currency-symbol").get_text().upper() # upper case
                name = row.find(class_="currency-name-container").get_text()
                if symbol in currencies.keys():
                    self._log(f"Duplicated currency found. Symbol: {symbol}. Name: {name}. Skip it.")
                    continue

                currency = Currency(symbol, name)
                currencies[symbol] = currency

        except Exception as error:
            self._log(f"Fail to load currencies. Error: {error}")
            raise Exception(f"Fail to load currencies. Error: {error}")

        # create the pairs
        return currencies_utils.generate_currency_pairs(list(currencies.values()))


    def get_data(self, filters=None) :

        try:
            base_url = url_coinmarketcap
            url = f"{base_url}/currencies/ripple/#markets"
            response = urlopen(url)
            bs = BeautifulSoup(response, "html5lib")

            exchanges = self._get_exchanges(bs, filters)

            # how to filter a dictionary https://stackoverflow.com/questions/2844516/how-to-filter-a-dictionary-according-to-an-arbitrary-condition-function

            return exchanges

        except Exception as error:
            self.writer.write(f"Error in {__name__}. {error}")
            print(f"Error in {__name__}. {error}")
            return 1  # Fatal error


    def _log(self, message):
        self.writer.write(message)



    def _get_exchanges(self, bs: BeautifulSoup, filters) -> List[Exchange]:

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
            
            if filters:
                if ("exchanges" in filters and exchange_name not in filters["exchanges"]) \
                or ("currency pairs" in filters and market_currencies not in filters["currency pairs"]):
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