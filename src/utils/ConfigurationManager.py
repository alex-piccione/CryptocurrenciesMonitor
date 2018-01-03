from UI.Configuration import Configuration

class ConfigurationManager:


    def load_configuration():

        return Configuration(
            currencies = ["BTC", "XRP", "ETH", "LTC", "TRX", "USD", "ADA", "XLM"],
            currency_pairs = ["XRP/USD", "XRP/BTC", "XRP/ETH", "XRP/LTC", "XLM/BTC", "XRP/EUR", "ADA/USD", "ADA/BTC", "BTC/ADA",
                	"LTC/USD", "LTC/XRP", "LTC/EUR",
                    "BTC/USD", "BTC/EUR", "BtC/XRP"
                ],
            exchanges = ["Gatehub", "Bitstamp", "Gate.io", "Binance", "Bitfinex", "Coinbase", "Bithumb"]
        )
