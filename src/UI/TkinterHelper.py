#from tkinter.ttk import *
from tkinter import *

class TkinterHelper():

    def __init__(self):

        self._load_images()

    def _load_images(self):

        import os
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_label_select_on = os.path.join(current_dir, "images", "item-check-on.png")
        file_label_select_off = os.path.join(current_dir, "images", "item-check-off.png")  
        # WARN: PhotoImage() must be called when root widget is defined or it raise "Too early to create image"
        self.image_label_select_on = PhotoImage(file=file_label_select_on)
        self.image_label_select_off = PhotoImage(file=file_label_select_off)