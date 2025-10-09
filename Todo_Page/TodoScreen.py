from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

class TodoScreen(Screen):
    todo_list = StringProperty("Loading todos...")

    def on_enter(self, *args):
        self.todo_list = "• Finish Kivy UI\n• Test on Raspberry Pi\n• Buy more coffee"


