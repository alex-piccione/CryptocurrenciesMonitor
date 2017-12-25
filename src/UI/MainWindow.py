from typing import Dict, List
from tkinter import *
from tkinter.ttk import *

from UI.Configuration import Configuration
from utils.FileWriter import FileWriter
from cryptocurrencies import WebScraper
from cryptocurrencies.entities import Exchange, Market

import UI


class MainWindow:

    def __init__(self, configuration:Configuration, writer:FileWriter, scraper:WebScraper):
        self.configuration = configuration
        self.writer = writer
        self.scraper = scraper
        self.theme_name = "Dark"

        self.tk = Tk()
        self.tk.title("Cryptocurrency Monitor")
        # set it as non-resizable
        #self.width=400
        #self.height=500
        #self.tk.geometry(f"{self.width}x{self.height}")
        self.tk.bind("<Escape>", self._quit )

        self._create_ui()
        self._load_data()
        self.tk.mainloop()

    def _quit(self):
        self.tk.quit()

    def _create_ui(self):
        
        UI.set_style(self.theme_name, self.tk)

        # top frame
        self._create_top_frame()

        # main frame
        self._create_central_frame()

        # bottom buttons
        self._create_bottom_bar()

    def _create_top_frame(self):
        frame = Frame(self.tk)
        frame.grid(row=0, column=0, padx=5, pady=5)

        source = "https://coinmarketcap.com"        
        source_label = Label(frame, text=f"Source: {source}")
        source_label.grid(row=0, column=0, sticky=W)


    def _create_central_frame(self):

        # ScrollBar cannot be associated to root widget and Frame, using canvas is the common solution
        canvas = UI.create_Canvas(self.tk, self.theme_name,)
        canvas.grid(row=1, column=0, columnspan=3)        
        scrollbar = Scrollbar(self.tk, orient=VERTICAL, command=canvas.yview)
        scrollbar.grid(row=1, column=3, sticky="ns")        
        frame = Frame(canvas)
        
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.create_window((0,0), window=frame, anchor="nw")
        def resize(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=600, height=400)
        frame.bind("<Configure>", resize)

        #frame.grid(row=1, column=0, padx=5, pady=5)
        #frame.config(height = 400, width=600)
        #frame.grid_propagate(0)        
        
        #scroll = Scrollbar(self.central_frame)
        #scroll.grid(row=1, column=0, padx=5, pady=5)

        self.central_frame = frame # set it visible

    def _create_bottom_bar(self):
        
        frame = Frame(self.tk)
        frame.grid(row=2, sticky= "E", padx=5, pady=5, columnspan=3)

        self.refresh_button = UI.create_button(frame, self.theme_name, "Refresh", command=self._load_data)
        #pad = {"padx":10, "pady":10}
        self.refresh_button.grid(row=0, column=0, padx=10, pady=10, ipadx=20)

        quit_button = UI.create_button(frame, self.theme_name, text="Quit", command=self._quit)
        quit_button.grid(row=0, column=1, sticky=SE, padx=10, pady=10, ipadx=20)

    def _load_data(self):

        filters = {
            "exchanges": self.configuration.exchanges,
            "markets": ["XRP/USD", "XRP/BTC", "XRP/ETH", "XRP/LTC", "XLM/BTC"]
        }

        data:List[Exchange] = self.scraper.get_data(filters)

        self._create_prices_table(data)

    def _create_prices_table(self, exchanges:Dict[str, Exchange]):

        #table = Treeview(self.central_frame)
        table = Frame(self.central_frame, style="table.TFrame")

        row = 0
        for exchange in exchanges:
            for market in exchange.markets.values():
                exchange_cell = Label(table, text=exchange.name, style="table_cell.TLabel", borderwidth="20m")
                market_cell = Label(table, text=market.name, style="table_cell.TLabel", borderwidth="20m")
                price_cell = Label(table, text=market.price, style="table_cell.TLabel", borderwidth="20m")
            
                exchange_cell.grid(row=row, column=0, sticky="nsew", padx=2, pady=2, ipadx=5, ipady=1)
                market_cell.grid(row=row, column=1, sticky="we", padx=2, pady=2, ipadx=5, ipady=1)
                price_cell.grid(row=row, column=2, sticky="we", padx=2, pady=2, ipadx=5, ipady=1)

                row += 1

        table.grid(row=0, column=0)

