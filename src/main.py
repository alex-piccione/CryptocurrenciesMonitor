import os
from cryptocurrencies.WebScraper import WebScraper
from utils.FileWriter import FileWriter
from UI.MainWindow import MainWindow

def main():
    
    file_name = "cryptocurrencies.txt"
    current_dir = os.path.dirname(os.path.realpath(__file__))
    destination_file = os.path.join(current_dir, "output", file_name)
    writer = FileWriter(destination_file)
    scraper = WebScraper(writer)    
    MainWindow(writer, scraper)    

if __name__ == "__main__":
    
    main()
