#region Library Imports
# The following 3 lines ensure a set inital window height
from kivy.config import Config
Config.set('graphics', 'width', '1728') # 1920 - 10%
Config.set('graphics', 'height', '972') # 1080 - 10%

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
#endregion

class RootWidget(RelativeLayout):
    pass

class PrototypeApp(App):
    pass

PrototypeApp().run()