from kivy.uix.screenmanager import Screen
from Logger.Logger import log
from Static.Messages.messages import SCREENSAVER_ON_TOUCH_UP_EVENT

class ScreenSaverScreen(Screen):
    
    def on_touch_up(self, touch):
        next_screen = "greetings"
        log.debug(SCREENSAVER_ON_TOUCH_UP_EVENT.format(next_screen))
        self.manager.current = next_screen
