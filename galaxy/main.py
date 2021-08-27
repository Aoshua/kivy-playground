from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.properties import Clock

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

    SPEED = 1.5
    currentYOffset = 0

    SPEED_X = 1.5
    currentXOffset = 0

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_vertical_lines()
        self.init_horizontal_lines()
        Clock.schedule_interval(self.update, 1.0 / 60.0) # 60fps

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
            lineX = centerLineX + (offset*spacing)
            x1, y1 = self.transform(lineX, 0)
            x2, y2 = self.transform(lineX, self.height)
            self.verticalLines[i].points = [x1, y1, x2, y2]
            offset += 1

    def update_horizontal_lines(self):
        centerLineX = int(self.width / 2)
        spacing = self.V_LINE_SPACING * self.width
        offset = -int(self.V_NUM_LINES/2)+0.5 #0.5 to make center space center

        xMin = centerLineX + offset*spacing
        xMax = centerLineX - offset*spacing
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

    def update(self, dt): 
        # dt for delta time, which is useful to ensure that processing
        # speeds do not interfere with our fps (see timeFactor).
        timeFactor = dt * 60
        self.update_vertical_lines()
        self.update_horizontal_lines()
        self.currentYOffset += self.SPEED * timeFactor

        ySpacing = self.H_LINE_SPACING * self.height
        if self.currentYOffset >= ySpacing:
            self.currentYOffset -= ySpacing

    def transform_2D(self, x, y):
        return int(x), int(y)


class GalaxyApp(App):
    pass

GalaxyApp().run()