from tkinter import *
from tkinter.ttk import *

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


    def create_Scrollbar(container, orient=HORIZONTAL, command=None):

        style = Style()

        # import the 'trough' element from the 'default' engine.        
        style.element_create("My.Vertical.Scrollbar.trough", "from", "default")

        # Redefine the horizontal scrollbar layout to use the custom trough.
        # This one is appropriate for the 'vista' theme.
        '''
        style.layout("My.Vertical.TScrollbar",
            [('My.Vertical.Scrollbar.trough', {'children':
                [('Vertical.Scrollbar.leftarrow', {'side': 'left', 'sticky': ''}),
                ('Vertical.Scrollbar.rightarrow', {'side': 'right', 'sticky': ''}),
                ('Vertical.Scrollbar.thumb', {'unit': '1', 'children':
                    [('Vertical.Scrollbar.grip', {'sticky': ''})],
                'sticky': 'nswe'}
                )],
            'sticky': 'we'
            })])
        '''

        style.layout("My.Vertical.TScrollbar", [
            ("My.Vertical.Scrollbar.trough", {
                "children": [
                    ["sti"]
                ]
            })
        ])

        # Copy original style configuration and add our new custom configuration option.
        style.configure("My.Vertical.TScrollbar", *style.configure("Vertical.TScrollbar"))
        style.configure("My.Vertical.TScrollbar", troughcolor="red")

        # Create and show a widget using the custom style
        scrollbar = Scrollbar(container, orient=orient, command=command, style="My.Vertical.TScrollbar")
        
        return scrollbar

