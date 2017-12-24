from tkinter import *
from tkinter.ttk import *

from utils.FileWriter import FileWriter
from cryptocurrencies import WebScraper

import UI


class MainWindow:

    def __init__(self, writer:FileWriter, scraper:WebScraper):
        self.writer = writer
        self.scraper = scraper

        self.tk = Tk()
        self.tk.title("Cryptocurrency Monitor")
        self.width=400
        self.height=500
        #self.tk.geometry(f"{self.width}x{self.height}")
        self.tk.bind("<Escape>", self._quit )

        self._create_ui()
        self.tk.mainloop()

    def _quit(self):
        self.tk.quit()

    def _create_ui(self):

        UI.set_style("Dark", self.tk)

        # main frame
        self._create_central_frame()

        # bottom buttons
        self._create_bottom_bar()


    def _create_central_frame(self):

        frame = Frame(self.tk)
        frame.grid(row=0, column=0, padx=10, pady=10)
        frame.config(height = 400, width=600)
        frame.grid_propagate(0)

        source = "https://coinmarketcap.com"        
        source_label = Label(frame, text=f"Source: {source}")
        source_label.grid(row=0, column=0, sticky=W)


    def _create_bottom_bar(self):
        
        frame = Frame(self.tk)
        frame.grid(row=1, sticky= "E", padx=10, pady=10, columnspan=3)

        self.refresh_button = UI.create_button(frame, "Refresh")
        #pad = {"padx":10, "pady":10}
        self.refresh_button.grid(row=0, column=0, padx=10, pady=10, ipadx=20)

        quit_button = UI.create_button(frame, text="Quit", command=self._quit)
        quit_button.grid(row=0, column=1, sticky=SE, padx=10, pady=10, ipadx=20)

    def _run_scraper():

        filters = {
            "exchanges": ["Gatehub", "Bitstamp", "Gate.io", "Binance", "Bitfinex"],
            "markets": ["XRP/USD", "XRP/BTC", "XRP/ETH", "XRP/LTC", "XLM/BTC"]
        }

        self.scraper.run(filters)