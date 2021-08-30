# The following 3 lines ensure a set inital window height
from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.properties import Clock
from kivy.core.window import Window
from kivy import platform

# kivy.graphics.vertex_instructions.Line(VertexInstruction)

class MainWidget(Widget):
    xPerspective = NumericProperty(0)
    yPerspective = NumericProperty(0)
    
    V_NUM_LINES = 10
    V_LINE_SPACING = .2 #% of screen width
    verticalLines = []

    H_NUM_LINES = 8
    H_LINE_SPACING = .1 #% of screen height
    horizontalLines = []

    SPEED_Y = 1.5
    currentYOffset = 0

    SPEED_X = 12
    currentXSpeed = 0
    currentXOffset = 0

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_vertical_lines()
        self.init_horizontal_lines()

        # attach keyboard listeners:
        if self.is_desktop():
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)

        Clock.schedule_interval(self.update, 1.0 / 60.0) # 60fps

    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard.unbind(on_key_up=self.on_keyboard_up)
        self._keyboard = None

    def is_desktop(self):
        if platform in ('linux', 'win', 'macosx'):
            return True
        return False

    # Called when the widget is attached to the parent
    def on_parent(self, widget, parent): 
        pass

    # Called on initally sizing the window, and when window size changes
    def on_size(self, *args): 
        # self.update_vertical_lines()
        # self.update_horizontal_lines()
        pass

    # All class properties have this form of on change function:
    def on_xPerspective(self, widget, value):
        # print("PX: " + str(value))
        pass

    def on_yPerspective(self, widget, value):
        # print("PY: " + str(value))
        pass

    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.V_NUM_LINES):
                self.verticalLines.append(Line())

    def init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.H_NUM_LINES):
                self.horizontalLines.append(Line())
    
    def update_vertical_lines(self):
        centerLineX = int(self.width / 2)
        spacing = self.V_LINE_SPACING * self.width
        offset = -int(self.V_NUM_LINES/2)+0.5 #0.5 to make center space center
        for i in range(0, self.V_NUM_LINES):
            lineX = centerLineX + (offset*spacing) + self.currentXOffset
            x1, y1 = self.transform(lineX, 0)
            x2, y2 = self.transform(lineX, self.height)
            self.verticalLines[i].points = [x1, y1, x2, y2]
            offset += 1

    def update_horizontal_lines(self):
        centerLineX = int(self.width / 2)
        spacing = self.V_LINE_SPACING * self.width
        offset = -int(self.V_NUM_LINES/2)+0.5 #0.5 to make center space center

        xMin = centerLineX + offset*spacing + self.currentXOffset
        xMax = centerLineX - offset*spacing + self.currentXOffset
        ySpacing = self.H_LINE_SPACING * self.height
        for i in range(0, self.H_NUM_LINES):
            lineY = i * ySpacing - self.currentYOffset
            x1, y1 = self.transform(xMin, lineY)
            x2, y2 = self.transform(xMax, lineY)
            self.horizontalLines[i].points = [x1, y1, x2, y2]

    def transform(self, x, y):
        return self.transform_3D(x, y)
        #return self.transform_2D(x, y)

    def transform_3D(self, x, y):
        yLinear = (y * self.yPerspective) / self.height
        if yLinear > self.yPerspective: # can't go above
            yLinear = self.yPerspective

        xDiff = x - self.xPerspective
        yDiff = self.yPerspective - yLinear

        yFactor = yDiff / self.yPerspective
        yFactor = pow(yFactor, 3)

        xTransform = self.xPerspective + (xDiff * yFactor)
        yTransform = self.yPerspective - (yFactor * self.yPerspective)
        return int(xTransform), int(yTransform)

    def transform_2D(self, x, y):
        return int(x), int(y)

    def update(self, dt): 
        # dt for delta time, which is useful to ensure that processing
        # speeds do not interfere with our fps (see timeFactor).
        timeFactor = dt * 60
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.currentYOffset += self.SPEED_Y * timeFactor

        ySpacing = self.H_LINE_SPACING * self.height
        if self.currentYOffset >= ySpacing:
            self.currentYOffset -= ySpacing

        self.currentXOffset += self.currentXSpeed * timeFactor

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


class GalaxyApp(App):
    pass

GalaxyApp().run()