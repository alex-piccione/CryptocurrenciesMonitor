import requests

from cryptocurrencies.entities import Currency

# API documentation: "https://coinmarketcap.com/api"
api_url = "https://api.coinmarketcap.com/v1"


class CoinmarketcapApi():


    def get_currencies(self):

        currencies = []

        try:
            response = requests.get(f"{api_url}/ticker?limit=50") # limit to 50 top ranked coins
            if response.status_code != 200:
                raise Exception(f"GET request fail. Status code: {response.status_code}. Reason: {response.reason}")

            data = response.json()
            for item in data:
                name = item["name"]
                symbol = item["symbol"]
                price_usd = float(item["price_usd"])

                currency = Currency(name, symbol)
                currencies.append(currency)

            return currencies

        except Exception as error:
            print(f"Fail to load data from Coinmarketcap API. Error. {error}")


        

