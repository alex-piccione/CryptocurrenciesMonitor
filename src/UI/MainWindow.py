from typing import Dict, List
from tkinter import *
from tkinter.ttk import *

from UI.Configuration import Configuration
from utils.FileWriter import FileWriter
from cryptocurrencies import WebScraper
from cryptocurrencies.entities import Exchange, Market

import UI
from UI.TkinterHelper import TkinterHelper


class MainWindow:

    def __init__(self, configuration:Configuration, writer:FileWriter, scraper:WebScraper):
        self.configuration = configuration
        self.writer = writer
        self.scraper = scraper
        self.theme_name = "Dark"

        self.tk = Tk()
        self.helper = TkinterHelper() # should be called after root Widget creation
        
        self.tk.title("Cryptocurrency Monitor")
        self.tk.resizable(False, False)
        self.tk.bind("<Escape>", self._quit )
        
        self._create_ui()
        self._load_prices()
        self.tk.mainloop()

    def _quit(self):
        self.tk.quit()


    def _create_ui(self):
        
        UI.set_style(self.theme_name, self.tk)
        
        self.markets = self.scraper.get_markets()
        #self.exchanges = self.scraper.get_exchanges()

        # top frame
        self._create_top_frame()

        # main frame
        self._create_central_frame()

        # bottom buttons
        self._create_bottom_bar()

    def _create_top_frame(self):
        frame = Frame(self.tk)
        frame.grid(row=0, column=0, sticky=W, padx=5, pady=5,)
 
        self.filter_markets = {}

        column = 0
        for market in self.markets:
            selected = market in self.configuration.markets

            if selected: image = self.helper.image_label_select_on
            else: image = self.helper.image_label_select_off

            button = Label(frame, image=image, text=market, compound="left")           
            button.image = image    # ridiculous: http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm                        
            button.bind("<Button-1>", self._change_market_selection)
            button.grid(row=0, column=column)

            button.market = market
            button.selected = selected
            self.filter_markets[market] = selected

            column += 1           
    

    def _change_market_selection(self, event):
        market = event.widget.market
        if event.widget.selected:
            selected = False
            image = self.helper.image_label_select_off
        else:
            selected = True
            image = self.helper.image_label_select_on
       
        event.widget.configure(image=image)
        event.widget.image = image
        event.widget.selected = selected

        self.filter_markets[market] = selected
        # self._refresh_prices()

    def _create_central_frame(self):

        table_width = 600
        table_height = 200

        # ScrollBar cannot be associated to root widget and Frame, using canvas is the common solution
        canvas = UI.create_Canvas(self.tk, self.theme_name)
        canvas.grid(row=1, column=0, padx=5)             
        scrollbar = Scrollbar(self.tk, orient=VERTICAL, command=canvas.yview)
        scrollbar.grid(row=1, column=1, sticky="nse")         
        frame = Frame(canvas)
         
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.create_window((0,0), window=frame, anchor="nw")

        def resize(event):
            canvas.configure(scrollregion=canvas.bbox("all"), width=table_width, height=table_height)
        frame.bind("<Configure>", resize)

        self.central_frame = frame # set it visible

    def _create_bottom_bar(self):
        
        frame = Frame(self.tk)
        frame.grid(row=2, sticky="E", padx=5, pady=5, columnspan=3)

        self.refresh_button = UI.create_button(frame, self.theme_name, "Refresh", command=self._load_prices)
        #pad = {"padx":10, "pady":10}
        self.refresh_button.grid(row=0, column=0, padx=5, pady=5, ipadx=10)

        quit_button = UI.create_button(frame, self.theme_name, text="Quit", command=self._quit)
        quit_button.grid(row=0, column=1, sticky=SE, padx=5, pady=5, ipadx=10)

    def _load_prices(self):

        filters = {
            "exchanges": self.configuration.exchanges,
            "markets": self.configuration.markets,
        }

        data:List[Exchange] = self.scraper.get_data(filters)

        self._create_prices_table(data)

    def _create_prices_table(self, exchanges:Dict[str, Exchange]):

        table = Frame(self.central_frame, style="table.TFrame") 
        #table.grid_columnconfigure(0, weight=2)
        #table.grid_columnconfigure(1, weight=1)
        #table.grid_columnconfigure(2, weight=1)        

        row = 0
        for exchange in exchanges:
            for market in exchange.markets.values():
                self._create_cell(table, row, 0, exchange.name, "w")
                self._create_cell(table, row, 1, market.name, "w")
                self._create_cell(table, row, 2, market.price, "e")     
                row += 1
        
        table.grid(row=0, column=0)

    def _create_cell(self, table, row, column, text, sticky):
        if row % 2 == 0 : style = ["table_cell.TFrame", "table_cell.TLabel"]
        else: style = ["table_cell_alt.TFrame", "table_cell_alt.TLabel"]
        cell = Frame(table, style=style[0], width=180, height=25)        
        cell.grid_propagate(0)
        #cell = Frame(table, style=style[0])        
        cell.grid(row=row, column=column, sticky="nswe", padx=0, pady=0, ipadx=10)
        cell_content = Label(cell, text=text, anchor=E, style=style[1])          
        cell_content.grid(row=0, column=0, sticky="nswe", ipadx=0, ipady=1)    # this sticky does not work

        

