from typing import List

class Configuration:

    def __init__(self, exchanges: List[str], currency_pairs=List[str] ):

        self.exchanges = exchanges
        self.currency_pairs:List[str] = currency_pairs
        
