from tkinter.ttk import *

theme = None

# ref (on layout): https://stackoverflow.com/questions/31606881/how-to-expand-widgets-size-in-a-frame-with-respect-to-other-frames-in-tkinter-h

class Dark:

    def __init__(self):
        color_1 = "#333"  # background
        color_3 = "#666"  # controls background
        color_2 = "#CCC"  # foreground

        self.frame_background = color_1

        self.label_background = color_1
        self.label_forground = color_2

        self.button_background = color_3
        self.button_foreground = color_2


def set_style(theme_name:str, window):
    #if theme_name == "Dark"
    theme = Dark()    

    style = Style()        

    window.configure(background=theme.frame_background)
    style.configure("TFrame", background=theme.frame_background)
    style.configure("TLabel", background=theme.label_background, foreground=theme.label_forground)
    style.configure("TButton", background=theme.button_background, 
        highlightbackground=theme.button_background, 
        foreground=theme.button_foreground )

    #style.configure(f'{theme}.TButton', foreground='black', background='gray')              
    #backButton = Button(self.bottomFrame, text="Back",
    #    command=lambda: controller.ShowFrame("StartPage"),  
    #    style='gray.TButton')      
    #    backButton.pack(side='left')


def create_button(container, text:str, command=None):
    ''' Create a widget Button.
    @param container: it is the widget (Frame) where to insert the button.
    @param 
    It use the tk.Button instead of the ttk.Button because the latter cannot change the background color.
    '''

    # ref (to set the bg when clicked) https://stackoverflow.com/questions/44323528/how-to-change-the-foreground-color-of-ttk-button-when-its-state-is-active

    import tkinter

    bg_color = "black" # for "Dark" theme

    #if theme_name == "Dark"
    theme = Dark()

    #return tkinter.Button(container, {"text":text, "bg":"black", "fg":"#CCCCCC"})
    return tkinter.Button(container, {"text":text, "bg":theme.button_background, "fg":theme.button_foreground }, command=command)

