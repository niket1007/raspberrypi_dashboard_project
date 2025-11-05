from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from Logger.Logger import log
from decouple import config
from Static.Messages.messages import (
    CUSTOM_SCREEN_ON_ENTER_EVENT, CUSTOM_SCREEN_ON_LEAVE_EVENT,
    CUSTOM_SCREEN_ON_TOUCH_UP_EVENT, CUSTOM_SCREEN_RESET_FUNCTION)

class CustomScreen(Screen):
    reset_event = None
    frequency = config("screensaver_frequency", cast=int)

    def on_enter(self):
        log.debug(CUSTOM_SCREEN_ON_ENTER_EVENT.format(self.manager.current, self.frequency))
        self.reset_event = Clock.schedule_interval(self.reset_screen, self.frequency)
    
    def on_leave(self):
        log.debug(CUSTOM_SCREEN_ON_LEAVE_EVENT.format(self.manager.current))
        if self.reset_event:
            self.reset_event.cancel()
    
    def on_touch_up(self, touch):
        log.debug(CUSTOM_SCREEN_ON_TOUCH_UP_EVENT.format(self.manager.current))
        if self.reset_event:
            self.reset_event.cancel()
            self.reset_event = Clock.schedule_interval(self.reset_screen, self.frequency)
    
    def reset_screen(self, *args):
        log.debug(CUSTOM_SCREEN_RESET_FUNCTION.format(self.manager.current))
        self.manager.current = "screensaver"