from UI.Configuration import Configuration

class ConfigurationManager:


    def load_configuration():

        return Configuration(
            currencies = ["BTC", "XRP", "ETH", "LTC", "TRX"],
            currency_pairs = ["XRP/USD", "XRP/BTC", "XRP/ETH", "XRP/LTC", "XLM/BTC", "XRP/EUR", "ADA/USD", "ADA/BTC", "XRP/EUR"],
            exchanges = ["Gatehub", "Bitstamp", "Gate.io", "Binance", "Bitfinex"]            
        )
