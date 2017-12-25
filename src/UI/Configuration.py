from typing import List

class Configuration:

    def __init__(self, exchanges: List[str], markets=List[str] ):

        self.exchanges = exchanges
        self.markets = markets
        

    