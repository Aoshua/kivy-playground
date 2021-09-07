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
from kivy.graphics.vertex_instructions import Quad

# kivy.graphics.vertex_instructions.Line(VertexInstruction)

class MainWidget(Widget):
    from transforms import transform, transform_2D, transform_3D
    from userActions import keyboard_closed, on_keyboard_up, on_keyboard_down, on_touch_up, on_touch_down

    xPerspective = NumericProperty(0)
    yPerspective = NumericProperty(0)
    
    V_NUM_LINES = 4
    V_LINE_SPACING = .1 #% of screen width
    verticalLines = []

    H_NUM_LINES = 8
    H_LINE_SPACING = .1 #% of screen height
    horizontalLines = []

    SPEED_Y = 1.5
    currentYOffset = 0

    SPEED_X = 12
    currentXSpeed = 0
    currentXOffset = 0

    tile = None
    tiX = 1
    tiY = 2

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_vertical_lines()
        self.init_horizontal_lines()
        self.init_tiles()

        # attach keyboard listeners:
        if self.is_desktop():
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)

        Clock.schedule_interval(self.update, 1.0 / 60.0) # 60fps

    def is_desktop(self):
        if platform in ('linux', 'win', 'macosx'):
            return True
        return False

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

    def init_tiles(self):
        with self.canvas:
            Color(1, 1, 1)
            self.tile = Quad()

    def get_line_x_from_index(self, index):
        centerLineX = self.xPerspective
        spacing = self.V_LINE_SPACING * self.width
        offset = index - 0.5
        lineX = centerLineX + offset*spacing + self.currentXOffset
        return lineX

    def get_line_y_from_index(self, index):
        spacing = self.H_LINE_SPACING * self.height
        lineY = index*spacing - self.currentYOffset
        return lineY

    def get_tile_coordinates(self, tiX, tiY):
        x = self.get_line_x_from_index(tiX)
        y = self.get_line_y_from_index(tiY)
        return x, y

    def update_tiles(self):
        xMin, yMin = self.get_tile_coordinates(self.tiX, self.tiY)
        xMax, yMax = self.get_tile_coordinates(self.tiX + 1, self.tiY + 1)
        # 2    3
        #
        # 1    4
        x1, y1 = self.transform(xMin, yMin)
        x2, y2 = self.transform(xMin, yMax)
        x3, y3 = self.transform(xMax, yMax)
        x4, y4 = self.transform(xMax, yMin)

        self.tile.points = [x1, y1, x2, y2, x3, y3, x4, y4]

    
    def update_vertical_lines(self):
        startIndex = -int(self.V_NUM_LINES / 2) + 1 # -1 0 1 2
        for i in range(startIndex, startIndex + self.V_NUM_LINES):
            lineX = self.get_line_x_from_index(i)
            x1, y1 = self.transform(lineX, 0)
            x2, y2 = self.transform(lineX, self.height)
            self.verticalLines[i].points = [x1, y1, x2, y2]
    
    def update_horizontal_lines(self):
        startIndex = -int(self.V_NUM_LINES / 2) + 1
        endIndex = startIndex + self.V_NUM_LINES - 1

        xMin = self.get_line_x_from_index(startIndex)
        xMax = self.get_line_x_from_index(endIndex)
        for i in range(0, self.H_NUM_LINES):
            lineY = self.get_line_y_from_index(i)
            x1, y1 = self.transform(xMin, lineY)
            x2, y2 = self.transform(xMax, lineY)
            self.horizontalLines[i].points = [x1, y1, x2, y2]

    def update(self, dt): 
        # dt for delta time, which is useful to ensure that processing
        # speeds do not interfere with our fps (see timeFactor).
        timeFactor = dt * 60
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.update_tiles()
        # self.currentYOffset += self.SPEED_Y * timeFactor

        ySpacing = self.H_LINE_SPACING * self.height
        if self.currentYOffset >= ySpacing:
            self.currentYOffset -= ySpacing

        # self.currentXOffset += self.currentXSpeed * timeFactor


class GalaxyApp(App):
    pass

GalaxyApp().run()

#### Below we have example code that could be helpful for future reference: ####

# # Called when the widget is attached to the parent
# def on_parent(self, widget, parent): 
#     pass

# # Called on initally sizing the window, and when window size changes
# def on_size(self, *args): 
#     # self.update_vertical_lines()
#     # self.update_horizontal_lines()
#     pass

# # All class properties have this form of on change function:
# def on_xPerspective(self, widget, value):
#     # print("PX: " + str(value))
#     pass

# def on_yPerspective(self, widget, value):
#     # print("PY: " + str(value))
#     pass