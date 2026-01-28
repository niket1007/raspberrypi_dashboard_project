import tkinter as tk
from decouple import config
from Services.Redis.redis import RedisStorage
from Services.Style import TodoPageStyle, MainPageStyle

class TodoPage(tk.Frame):

    UPDATE_INTERVAL = config("todo_redis_frequency", cast=int)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=MainPageStyle.BackgroundColor)
        self.controller = controller
        self.widgetName = "Todo"
        self.redis = RedisStorage()

        # --- Todo List Content ---
        self.todo_label = tk.Label(self, **TodoPageStyle.TodoLabel)
        self.todo_label.pack(**TodoPageStyle.TodoLabelPack)

        self.load_todos()

    def load_todos(self):
        todo_text = self.redis.get_todo_data()
        self.todo_label.config(text=todo_text)
        
        self.after(self.UPDATE_INTERVAL, self.load_todos)
