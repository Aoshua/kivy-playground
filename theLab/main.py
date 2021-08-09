from itertools import count
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.properties import StringProperty


class WidgetsExample(GridLayout):
    count = 1
    my_text = StringProperty(str(count))
    def on_button_click(self):
        self.count += 1
        self.my_text = str(self.count)

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "rl-bt"
        for i in range(0, 100):
            # size = dp(100) + i*10
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)

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