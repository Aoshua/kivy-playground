from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.graphics.vertex_instructions import Line
from kivy.graphics import *
from kivy.metrics import dp
from kivy.properties import Clock

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 0)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(800, 100, 300, 200), width=8)
            self.rect = Rectangle(pos=(400, 200), size=(150, 100))

    def onButtonAClick(self):
        x, y, = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)

        diff = self.width - (x + w)
        if diff < inc:
            inc = diff

        x += inc
        self.rect.pos = (x, y)

    def onButtonBClick(self):
        x, y, = self.rect.pos
        if x - dp(10) > 0:
            x -= dp(10)
        self.rect.pos = (x, y)


class BouncyBall(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ballSize = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:
            Color(.49, .41, .921)
            self.ball = Ellipse(pos=self.center, size=(self.ballSize, self.ballSize))
        Clock.schedule_interval(self.update, 1/60) #2nd parameter in seconds

    def update(self, dt):
        x, y = self.ball.pos #x,y are lower and left

        x += self.vx
        y += self.vy

        # self.ball_size is right top
        if x < 0: #collides with left side
            x = 0
            self.vx = -self.vx
        if x + self.ballSize > self.width: # collides with right side
            x = self.width - self.ballSize
            self.vx = -self.vx
        if y < 0: # collides with bottom
            y = 0
            self.vy = -self.vy
        if y + self.ballSize > self.height: # collides with top
            y = self.height - self.ballSize
            self.vy = -self.vy

        self.ball.pos = (x, y)

    def on_size(self, *args):
        # print("on size: " + str(self.width) + ", " +str(self.height))
        self.ball.pos = (self.center_x - self.ballSize/2, self.center_y - self.ballSize/2)

class CanvasExample6(Widget):
    pass

class CanvasApp(App):
    pass


CanvasApp().run()