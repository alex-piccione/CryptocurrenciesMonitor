from typing import List

class Configuration:

    def __init__(self, currencies: List[str], currency_pairs: List[str], exchanges: List[str]):
        self.currencies: List[str] = currencies        
        self.currency_pairs:List[str] = currency_pairs
        self.exchanges: List[str] = exchanges
        
