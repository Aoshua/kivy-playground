from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line

# kivy.graphics.vertex_instructions.Line(VertexInstruction)

class MainWidget(Widget):
    perspectivePointX = NumericProperty(0)
    perspectivePointY = NumericProperty(0)
    
    V_NUM_LINES = 7
    V_LINE_SPACING = .1 #% of screen width
    verticalLines = []

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_vertical_lines()

    # Called when the widget is attached to the parent
    def on_parent(self, widget, parent): 
        pass

    # Called on initally sizing the window, and when window size changes
    def on_size(self, *args): 
        #print("on_size W:" + str(self.width) + " H:" + str(self.height))
        # self.perspectivePointX = self.width/2
        # self.perspectivePointY = self.height * .75
        self.update_vertical_lines()

    # All class properties have this form of on change function:
    def on_perspectivePointX(self, widget, value):
        print("PX: " + str(value))
        #pass

    def on_perspectivePointY(self, widget, value):
        print("PY: " + str(value))
        #pass

    def init_vertical_lines(self):
        with self.canvas:
            Color(1, 1, 1)
            # self.line = Line(points=[100 , 0, 100, 100])
            for i in range(0, self.V_NUM_LINES):
                self.verticalLines.append(Line())
    
    def update_vertical_lines(self):
        centerLineX = int(self.width/2)
        spacing = self.V_LINE_SPACING * self.width
        offset = -int(self.V_NUM_LINES/2)
        for i in range(0, self.V_NUM_LINES):
            lineX = centerLineX + (offset*spacing)
            self.verticalLines[i].points = [lineX, 0, lineX, self.height]
            offset += 1


class GalaxyApp(App):
    pass

GalaxyApp().run()