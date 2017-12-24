from UI.Configuration import Configuration

class ConfigurationManager:


    def load_configuration():

        return Configuration(exchanges=["Gatehub", "Bitstamp", "Gate.io", "Binance", "Bitfinex"])
