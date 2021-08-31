def on_touch_down(self, touch):
    if touch.x < self.width / 2:
        self.currentXSpeed = self.SPEED_X
    else:
        self.currentXSpeed = -self.SPEED_X

def on_touch_up(self, touch):
    self.currentXSpeed = 0

def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'left':
        self.currentXSpeed = self.SPEED_X
    elif keycode[1] == 'right':
        self.currentXSpeed = -self.SPEED_X
    return True

def on_keyboard_up(self, keyboard, keycode):
    self.currentXSpeed = 0

def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.unbind(on_key_up=self.on_keyboard_up)
    self._keyboard = None