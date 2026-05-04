from kivy.uix.button import Button
from kivy.uix.layout import Layout
from kivy.uix.gridlayout import GridLayout

# Button Class
class Inter_Button(Button):
    btn = None # Kivy Button Object

    def _SetButtonPosition_(self, x=int, y=int):
        self.btn.pos = (x, y)

    def __init__(self, TEXT=str, PRESSFUNC=type(object) or None, POSITION=(int, int) or None):
        self.btn = Button(text=TEXT, on_press=PRESSFUNC, pos=POSITION)

    def __call__(self):
        return self.btn
    
class Screen(Layout):

    WidgetsList = []

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        for x in Screen.WidgetsList:
            self.add_widget(x)

    def __call__(self):
        pass

    class Grid(GridLayout):
        cols = 2
        rows = 2
        padding = "padding_top"

        # AddButton Function
        def addButton(TEXT=str, FUNC=type(object) or None, POSITION=(0, 0) or None):
            Screen.WidgetsList.append(Inter_Button(TEXT, FUNC, POSITION).btn)

        def __init__(self, **kwargs):
            super(Screen.Grid, self).__init__(**kwargs)
        
        def __call__(self):
            return self
