from UI.Configuration import Configuration

class ConfigurationManager:


    def load_configuration():

        return Configuration(exchanges=["Gatehub", "Bitstamp", "Gate.io", "Binance", "Bitfinex"],
            currency_pairs=["XRP/USD", "XRP/BTC", "XRP/ETH", "XRP/LTC", "XLM/BTC"]
        )
