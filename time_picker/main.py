from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('time.kv')

    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.on_cancel, time=self.get_time)
        time_dialog.open()

    def on_cancel(self, instance, time):
        self.root.ids.time_label.text = "You Clicked Cancel"

    def get_time(self, instance, time):
        self.root.ids.time_label.text = str(time)


MainApp().run()