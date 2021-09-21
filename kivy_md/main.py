from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

class LoginScreen(Screen):
    def sign_in(self):
        print('this happened')
        # here we would send the credentials to an API
        # before switching to a new page
        self.manager.transition.direction = 'left'
        self.manager.current = 'dashboard'

class DashboardScreen(Screen):
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightGreen"
        Builder.load_file('awesome.kv')

        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        return sm

MainApp().run()