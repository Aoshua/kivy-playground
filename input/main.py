from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy import platform

class RootWidget(RelativeLayout):

    lbl_txt = StringProperty("Welcome to input tester")

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

        if self.is_desktop():
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down = self.on_keyboard_down)
        
        Window.bind(on_joy_hat = self.on_joy_hat)

    def is_desktop(self):
        if platform in ('linux', 'win', 'macosx'):
            return True
        return False

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.lbl_txt = "Left Key"
        elif keycode[1] == 'right':
            self.lbl_txt = "Right Key"
        return True

    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard.unbind(on_key_up=self.on_keyboard_up)
        self._keyboard = None

    def on_touch_down(self, touch):
        if touch.x < self.width / 2:
            self.lbl_txt = "Touch Left"
        else:
            self.lbl_txt = "Touch Right"
        return super(RelativeLayout, self).on_touch_down(touch)

    def on_joy_hat(self, win, stickid, hatid, value):
        self.lbl_txt = f'Joy Hat, StickId: {str(stickid)}, HatId: {str(hatid)}, Value: {str(value)}'



class InputApp(App):
    pass

InputApp().run()