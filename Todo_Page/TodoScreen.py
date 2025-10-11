from kivy.properties import StringProperty
from CustomScreen.customScreen import CustomScreen

class TodoScreen(CustomScreen):
    todo_list = StringProperty("Loading todos...")

    def on_enter(self, *args):
        self.todo_list = "• Finish Kivy UI\n• Test on Raspberry Pi\n• Buy more coffee"
        return super().on_enter()


