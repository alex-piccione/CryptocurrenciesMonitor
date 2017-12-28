from tkinter.ttk import *

# ref (on layout): https://stackoverflow.com/questions/31606881/how-to-expand-widgets-size-in-a-frame-with-respect-to-other-frames-in-tkinter-h

class Dark:

    def __init__(self):
        color_1 = "#1F1F1F"  # background
        color_3 = "#444"  # controls background
        color_2 = "#CCC"  # foreground, text

        color_4 = "#292929"
        color_5 = "#202020"  # alternate

        self.frame_background = color_1

        self.label_background = color_1
        self.label_forground = color_2

        self.button_background = color_3
        self.button_foreground = color_2
        self.button_background_disabled = color_4
        self.button_foreground_disabled = color_3

        self.control_background = color_3

        self.table_cell_background = color_4
        self.table_cell_background_alt = color_5
        self.table_cell_foreground = color_2

def get_theme(theme_name:str):
    #if theme_name == "Dark"
    theme = Dark()
    return theme

def set_style(theme_name:str, window):
    #if theme_name == "Dark"
    theme = get_theme(theme_name)   

    style = Style()        

    window.configure(background=theme.frame_background)
    style.configure("TFrame", background=theme.frame_background)
    style.configure("TLabel", background=theme.label_background, foreground=theme.label_forground)
    style.configure("TButton", background=theme.button_background, 
        highlightbackground=theme.button_background, 
        foreground=theme.button_foreground )
    
    style.configure("TTreeView", background=theme.control_background) # does not work

    # table
    style.configure("table.TFrame", background=theme.control_background)
    style.configure("table_cell.TFrame", background=theme.table_cell_background)
    style.configure("table_cell_alt.TFrame", background=theme.table_cell_background_alt)
    style.configure("table_cell.TLabel", background=theme.table_cell_background, foreground=theme.table_cell_foreground)
    style.configure("table_cell_alt.TLabel", background=theme.table_cell_background_alt, foreground=theme.table_cell_foreground) # alternate
    
    # font=("Helvetica", 16)
    #style.configure(f'{theme}.TButton', foreground='black', background='gray')              
    #backButton = Button(self.bottomFrame, text="Back",
    #    command=lambda: controller.ShowFrame("StartPage"),  
    #    style='gray.TButton')      
    #    backButton.pack(side='left')


def create_button(container, theme_name:str, text:str, command=None):
    ''' Create a widget Button.
    @param container: it is the widget (Frame) where to insert the button.
    It use the tk.Button instead of the ttk.Button because the latter cannot change the background color.
    '''
    
    theme = get_theme(theme_name)

    import tkinter

    # ref (to set the bg when clicked) https://stackoverflow.com/questions/44323528/how-to-change-the-foreground-color-of-ttk-button-when-its-state-is-active

    #return tkinter.Button(container, {"text":text, "bg":"black", "fg":"#CCCCCC"})
    return tkinter.Button(container, {"text":text, "bg":theme.button_background, "fg":theme.button_foreground, 
        "relief": tkinter.FLAT
    }, command=command)

def create_Canvas(container, theme_name:str):

    theme = get_theme(theme_name)

    import tkinter

    # highlightthickness=0 remove the border (borderwidth is 0 by default)
    return tkinter.Canvas(container, background=theme.control_background, borderwidth=0, highlightthickness=0, closeenough=0)

def disable_button(button, theme_name:str):
    theme = get_theme(theme_name)
    button.configure({"bg": theme.button_background_disabled, "fg": theme.button_foreground_disabled})
    #button.configure({"bg": theme.button_background_disabled})

def enable_button(button, theme_name:str):
    theme = get_theme(theme_name)
    button.configure({"bg": theme.button_background, "fg": theme.button_foreground})