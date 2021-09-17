from dictObj import DictObj
from kivy.config import Config
Config.set('graphics', 'width', '1728') # 1920 - 10%
Config.set('graphics', 'height', '972') # 1080 - 10%

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import StringProperty
import requests

class RootWidget(RelativeLayout):
    from dictObj import DictObj
    post = None
    post_title = StringProperty("Request not sent")

    def send_api_request(self):
        r = requests.get('https://api.dailysmarty.com/posts')
        postDict = r.json()['posts'][0]  # r.json() returns a dictionary of the response:
        
        # Convert to object with type:
        self.post = Post(postDict)
        self.post_title = self.post.title

        # Simply access as dictionary:
        # self.post = r.json()['posts'][0]
        # self.post_title = self.post['title']

    def on_request_btn_pressed(self):
        self.send_api_request()

class Post():
    id: int
    title: str
    content: str
    created_at: str
    url_for_post: str
    associated_topics: list
    post_links: list

    def __init__(self, dict:dict):
        for key in dict:
            setattr(self, key, dict[key])
   


class RequestsApp(App):
    pass

RequestsApp().run()