from kivy.uix.button import Button
from kivy.uix.layout import Layout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Inter_Label(Label):

    obj = None

    def __init__(self, TEXT=str or None):
        if TEXT is not None:
            self.text = TEXT

        self.obj = Label(text=TEXT, markup=True)
    
    def __call__(self):
        return self.obj

class Inter_Layout(Widget):
    obj = None

    def __init__(self):
        self.obj = Widget()
    
    def __call__(self):
        return self.obj

# Button Class
class Inter_Button(Button):
    obj = None # Kivy Button Object

    def _SetButtonPosition_(self, x=int, y=int):
        self.obj.pos = (x, y)

    def __init__(self, TEXT=str, PRESSFUNC=type(object) or None, POSITION=(int, int) or None):
        self.obj = Button(text=TEXT, on_press=PRESSFUNC, pos=POSITION)

    def __call__(self):
        return self.obj
    

class Screen(Layout):

    WidgetsList = []

    def addLayout(self):
        self.WidgetsList.append(Inter_Layout())

    # AddButton Function
    def addButton(self, TEXT=str, FUNC=type(object) or None, POSITION=(0, 0) or None):
        self.WidgetsList.append(Inter_Button(TEXT, FUNC, POSITION))

    def renderWidgets(self):
        for x in self.WidgetsList:
            self.add_widget(x.obj)

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

    def __call__(self):
        self.renderWidgets()
        return self
    

    class Box(BoxLayout):

        gridObj = None

        WidgetsList = []

        orientation = "vertical" # <vertical> and <horizontal>
        spacing = 5

        def addLabel(self, TEXT=str or None):
            self.WidgetsList.append(Inter_Label(TEXT))

        def getGrid(self):
            try:
                return self.WidgetsList[self.gridObj]
            except:
                raise Exception("This layout does not have a grid; Create with '<BoxLayoutObject>.addGridLayout()' first")

        def addGridLayout(self):
            gridTempObj = Screen.Grid()
            self.WidgetsList.append(gridTempObj)
            self.gridObj = self.WidgetsList.index(gridTempObj)
            

        def changeOrientation(self, ORIENTATION = str):
            self.orientation = ORIENTATION

        def addLayout(self):
            self.WidgetsList.append(Inter_Layout())

        # AddButton Function
        def addButton(self, TEXT=str, FUNC=type(object) or None, POSITION=(0, 0) or None):
            self.WidgetsList.append(Inter_Button(TEXT, FUNC, POSITION))
        
        def renderWidgets(self):
            for x in self.WidgetsList:
                self.add_widget(x.obj)


        def __init__(self, ORIENTATION = str or None, SPACING = int or None, **kwargs):
            super(Screen.Box, self).__init__(**kwargs)
            
            if ORIENTATION is not None:
                self.orientation = ORIENTATION

            if SPACING is not None:
                self.spacing = SPACING

        def __call__(self):
            self.renderWidgets()
            return self


    class Grid(GridLayout):

        obj = None

        WidgetsList = []

        cols = 2
        rows = 2

        def addLabel(self, TEXT=str or None):
            self.WidgetsList.append(Inter_Label(TEXT))

        def setRows(self, ROWS = int):
            self.rows = ROWS
        
        def setCols(self, COLS = int):
            self.cols = COLS

        def addLayout(self):
            self.WidgetsList.append(Inter_Layout())

        # AddButton Function
        def addButton(self, TEXT=str, FUNC=type(object) or None, POSITION=(0, 0) or None):
            self.WidgetsList.append(Inter_Button(TEXT, FUNC, POSITION))
        
        def renderWidgets(self):
            for x in self.WidgetsList:
                self.add_widget(x.obj)

        def __init__(self, **kwargs):
            super(Screen.Grid, self).__init__(**kwargs)
            self.obj = self
        
        def __call__(self):
            self.renderWidgets()
            return self
