from typing import List, Iterable
from cryptocurrencies.entities import CurrencyPair, Currency



def generate_currency_pairs(currencies:Iterable[Currency]) -> List[CurrencyPair]:
    """ 
    From the currencies A,B,C generate A/B, A/C, B/C.
    The priority between the 2 possible direction of a pair is not defined.
    """

    pairs = []

    index = 1
    currencies = list(currencies)
    for currency_a in currencies:
        for currency_b in currencies[index:]:
            if currency_a.code != currency_b.code:
                pair = CurrencyPair(currency_a.code, currency_b.code)
                pairs.append(pair)
        index += 1

    return pairs