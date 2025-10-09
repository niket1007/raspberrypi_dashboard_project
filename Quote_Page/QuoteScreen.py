from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

class QuoteScreen(Screen):
    quote_text = StringProperty("Loading quote...")

    def on_enter(self, *args):
        self.quote_text = '"The best way to predict the future is to invent it."\n\n- Alan Kay'
        # return super().on_enter(*args)
