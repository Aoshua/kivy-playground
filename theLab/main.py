from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
# from kivy.uix.gridlayout import GridLayout

# Instead, we are defining this straight in the .kv
# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    # def __init__(self, **kwargs): # kivy constructors req. kwargs for internal operations
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B") # can also define appearance in the code, same names as in .kv
    #     b3 = Button(text="C")
    #     self.add_widget(b1) # self refers to the class that this class inherits from: BoxLayout
    #     self.add_widget(b2)
    #     self.add_widget(b3)
    pass


class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()