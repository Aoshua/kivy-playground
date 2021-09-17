from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('time.kv')

    def show_time_picker(self):
        from datetime import datetime
        
        default_time = datetime.strptime("4:20:00", '%H:%M:%S').time()
        time_dialog = MDTimePicker()
        time_dialog.set_time(default_time)
        time_dialog.bind(on_cancel=self.on_cancel, time=self.get_time)
        time_dialog.open()

    def on_cancel(self, instance, time):
        self.root.ids.time_label.text = "You Clicked Cancel"

    def get_time(self, instance, time):
        self.root.ids.time_label.text = str(time)


MainApp().run()