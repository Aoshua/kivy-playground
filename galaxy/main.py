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
    vertical_lines = []

    H_NUM_LINES = 8
    H_LINE_SPACING = .1 #% of screen height
    horizontal_lines = []

    SPEED_Y = 1.5
    current_y_offset = 0

    SPEED_X = 12
    current_x_speed = 0
    current_x_offset = 0

    tile = None
    ti_x = 1
    ti_y = 2

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
                self.vertical_lines.append(Line())

    def init_horizontal_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.H_NUM_LINES):
                self.horizontal_lines.append(Line())

    def init_tiles(self):
        with self.canvas:
            Color(1, 1, 1)
            self.tile = Quad()

    def get_line_x_from_index(self, index):
        center_line_x = self.xPerspective
        spacing = self.V_LINE_SPACING * self.width
        offset = index - 0.5
        line_x = center_line_x + offset*spacing + self.current_x_offset
        return line_x

    def get_line_y_from_index(self, index):
        spacing = self.H_LINE_SPACING * self.height
        line_y = index*spacing - self.current_y_offset
        return line_y

    def get_tile_coordinates(self, ti_x, ti_y):
        x = self.get_line_x_from_index(ti_x)
        y = self.get_line_y_from_index(ti_y)
        return x, y

    def update_tiles(self):
        x_min, y_min = self.get_tile_coordinates(self.ti_x, self.ti_y)
        x_max, y_max = self.get_tile_coordinates(self.ti_x + 1, self.ti_y + 1)
        # 2    3
        #
        # 1    4
        x1, y1 = self.transform(x_min, y_min)
        x2, y2 = self.transform(x_min, y_max)
        x3, y3 = self.transform(x_max, y_max)
        x4, y4 = self.transform(x_max, y_min)

        self.tile.points = [x1, y1, x2, y2, x3, y3, x4, y4]

    
    def update_vertical_lines(self):
        start_index = -int(self.V_NUM_LINES / 2) + 1 # -1 0 1 2
        for i in range(start_index, start_index + self.V_NUM_LINES):
            line_x = self.get_line_x_from_index(i)
            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]
    
    def update_horizontal_lines(self):
        start_index = -int(self.V_NUM_LINES / 2) + 1
        end_index = start_index + self.V_NUM_LINES - 1

        x_min = self.get_line_x_from_index(start_index)
        x_max = self.get_line_x_from_index(end_index)
        for i in range(0, self.H_NUM_LINES):
            line_y = self.get_line_y_from_index(i)
            x1, y1 = self.transform(x_min, line_y)
            x2, y2 = self.transform(x_max, line_y)
            self.horizontal_lines[i].points = [x1, y1, x2, y2]

    def update(self, dt): 
        # dt for delta time, which is useful to ensure that processing
        # speeds do not interfere with our fps (see time_factor).
        time_factor = dt * 60
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.update_tiles()
        self.current_y_offset += self.SPEED_Y * time_factor

        ySpacing = self.H_LINE_SPACING * self.height
        if self.current_y_offset >= ySpacing:
            self.current_y_offset -= ySpacing

        # self.current_x_offset += self.current_x_speed * time_factor


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