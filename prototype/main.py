#region Library Imports
# The following 3 lines ensure a set inital window height
from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

from kivy.app import App
#endregion

class MainWidget(RelativeLayout):
    pass

class PrototypeApp(App):
    pass

PrototypeApp().run()