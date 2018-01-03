#from cryptocurrencies.FIATcurrencies import list as fiat_criptocurrencies

class Exchange():

    def __init__(self, name, markets=None):
        self.name = name
        self.markets = markets or {}

    def add_market(self, market):
        if market.name in self.markets:
            raise Exception(f"Market {market.name} already exists in Exchange {exchange.name}")
        
        self.markets[market.name] = market

# TODO: modify it to bind it ti an Exchange
class Market():
    ''' 
    Represents a pair of currencies and its price.
    Should be modified to comprehend the Exchange and use the CurrencyPair
    '''

    def __init__(self, currency_main, currency_base, price:float):
        '''
        @param currency_main is tha AAA in AAA/BBB
        @param currency_base is tha BBB in AAA/BBB
        '''
        self.currency_main = currency_main
        self.currency_base = currency_base
        self.name = f"{currency_main}/{currency_base}"
        self.price = price

    def parse(market_currencies:str, price):
        '''
        Create a market from the text "AAA/BBB"
        '''
        
        try:
            currencies = market_currencies.split("/")
            if len(currencies) == 2:
                return Market(currencies[0], currencies[1], price)
            else:
                raise Exception(f"Fail to parse market from {market_currencies}")
        except Exception as err:
            raise Exception(f"Fail to parse market from {market_currencies}")


class CurrencyPair():
    """ Represent a pair of currencies that can """

    def __init__(self, currency_main:str, currency_base:str):
        '''
        @param currency_main is tha AAA in AAA/BBB
        @param currency_base is tha BBB in AAA/BBB
        '''
        self.currency_main = currency_main
        self.currency_base = currency_base
        self.name = f"{currency_main}/{currency_base}"

    def parse(currencies:str):
        '''
        Create a CurrencyPair from a text like"AAA/BBB".
        '''
        
        try:
            currencies = market_currencies.split("/")
            if len(currencies) == 2:
                return CurrencyPair(currencies[0], currencies[1])
            else:
                raise Exception(f"Fail to parse market from {currencies}")
        except Exception as err:
            raise Exception(f"Fail to parse market from {currencies}")



class Currency():

    def __init__(self, name, code):
        """
        @param name (string): Name of the currency (Bitcoin, Ripple, Cardano ...) 
        @param code (string): 3 letters ISO code
        """

        from cryptocurrencies import FIAT_currencies

        self.name = name
        self.symbol = code
        self.fiat = code in FIAT_currencies.list  # indicates if is a FIAT currency


