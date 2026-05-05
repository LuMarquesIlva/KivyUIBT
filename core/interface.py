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
        print(self.btn)
        return self.btn
    
class Screen(Layout):

    WidgetsList = []

    # AddButton Function
    def addButton(self, TEXT=str, FUNC=type(object) or None, POSITION=(0, 0) or None):
        self.WidgetsList.append(Inter_Button(TEXT, FUNC, POSITION))

    def renderWidgets(self):
        for x in self.WidgetsList:
            print(x)
            self.add_widget(x.btn)

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        print(self.WidgetsList)

    def __call__(self):
        self.renderWidgets()
        return self

    class Grid(GridLayout):

        WidgetsList = []

        cols = 2
        rows = 2

        # AddButton Function
        def addButton(self, TEXT=str, FUNC=type(object) or None, POSITION=(0, 0) or None):
            self.WidgetsList.append(Inter_Button(TEXT, FUNC, POSITION))
            print(self.WidgetsList)
        
        def renderWidgets(self):
            for x in self.WidgetsList:
                print(x)
                self.add_widget(x.btn)

        def __init__(self, **kwargs):
            super(Screen.Grid, self).__init__(**kwargs)
            print(self.WidgetsList)
        
        def __call__(self):
            self.renderWidgets()
            return self
