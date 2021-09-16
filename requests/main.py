from kivy.config import Config
Config.set('graphics', 'width', '1728') # 1920 - 10%
Config.set('graphics', 'height', '972') # 1080 - 10%

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty
import requests

class RootWidget(RelativeLayout):
    post = None
    post_title = StringProperty("Request not sent")

    def send_api_request(self):
        r = requests.get('https://api.dailysmarty.com/posts')
        # r.json() returns a dictionary of the response
        self.post = r.json()['posts'][0]
        self.post_title = self.post['title']

    def on_request_btn_pressed(self):
        self.send_api_request()

class RequestsApp(App):
    pass

RequestsApp().run()