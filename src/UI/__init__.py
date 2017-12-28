from tkinter.ttk import *

# ref (on layout): https://stackoverflow.com/questions/31606881/how-to-expand-widgets-size-in-a-frame-with-respect-to-other-frames-in-tkinter-h

class Dark:

    def __init__(self):
        color_01 = "#0F0F0F"  # background
        color_11 = "#151515"  # background alternate
        color_03 = "#444"  # controls background
        color_02 = "#CCC"  # foreground, text

        color_04 = "#292929"   
        color_14 = "#202020"  # alternate

        color_07 = "#e65c00"     # active
        color_17 = "#cc5200"     # active alternate

        self.frame_background = color_01
        self.control_background = color_11

        self.label_background = color_01
        self.label_forground = color_02

        self.button_background = color_03
        self.button_foreground = color_02
        self.button_background_disabled = color_04
        self.button_foreground_disabled = color_03        
        self.button_background_active = color_07


        self.table_cell_background = color_04
        self.table_cell_background_alternate = color_14
        self.table_cell_foreground = color_02

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
    style.configure("table_cell_alternate.TFrame", background=theme.table_cell_background_alternate)
    style.configure("table_cell.TLabel", background=theme.table_cell_background, foreground=theme.table_cell_foreground)
    style.configure("table_cell_alternate.TLabel", background=theme.table_cell_background_alternate, foreground=theme.table_cell_foreground) # alternate
    
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
    Reference/Docs: http://effbot.org/tkinterbook/button.htm
    '''
    
    theme = get_theme(theme_name)

    import tkinter

    # ref (to set the bg when clicked) https://stackoverflow.com/questions/44323528/how-to-change-the-foreground-color-of-ttk-button-when-its-state-is-active
    # highlightcolor is the color of the border
    return tkinter.Button(container, {"text":text, "bg":theme.button_background, "fg":theme.button_foreground, 
        "activebackground": theme.button_background_active,  # "activeforeground": theme.button_foreground_disabled,
        "disabledforeground": theme.button_background_disabled,
        "borderwidth": 1, "relief": tkinter.FLAT, "overrelief": tkinter.FLAT   
        # "highlightbackground": "red", "highlightcolor": "yellow", "highlightthickness": 2,
             
    }, command=command)

def create_Canvas(container, theme_name:str):

    theme = get_theme(theme_name)

    import tkinter

    # highlightthickness=0 is needed to remove the border (borderwidth is 0 by default)
    return tkinter.Canvas(container, background=theme.control_background, borderwidth=0, highlightthickness=0, closeenough=0)

def disable_button(button, theme_name:str):
    theme = get_theme(theme_name)
    button.configure({"bg": theme.button_background_disabled, "fg": theme.button_foreground_disabled})

def enable_button(button, theme_name:str):
    theme = get_theme(theme_name)
    button.configure({"bg": theme.button_background, "fg": theme.button_foreground})