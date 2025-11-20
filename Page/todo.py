import tkinter as tk
from Services.Redis.redis import RedisStorage

class TodoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.widgetName = "Todo"
        self.redis = RedisStorage()

        # --- Todo List Content ---
        # Equivalent to the second Label bound to root.todo_list
        self.todo_label = tk.Label(self, 
                                   text="Loading todos...", 
                                   font=("Helvetica", 12),
                                   justify="left",
                                   wraplength=400,
                                   anchor="n") # Anchors text to the top (North)
        self.todo_label.pack(side="top", expand=True, fill="both", padx=20, pady=20)

        self.load_todos()

    def load_todos(self):
        todo_text = self.redis.get_todo_data()
        self.todo_label.config(text=todo_text)