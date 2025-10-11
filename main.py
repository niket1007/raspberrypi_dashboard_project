from kivy.config import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ListProperty
from Logger.Logger import log
from Storage.Cache import Cache
from Static.Messages.messages import (
    BUILD_FUNC_LOG_MESSAGE, APP_ON_START_LOG_MESSAGE,
    APP_ON_TOUCH_DOWN_EVENT, APP_ON_TOUCH_UP_EVENT)

##### Screen Imports #####
from Weather_Page.WeatherScreen import WeatherScreen
from Todo_Page.TodoScreen import TodoScreen
from Quote_Page.QuoteScreen import QuoteScreen
from Calendar_Page.CalendarScreen import CalendarScreen
from ScreenSaver_Page.ScreenSaverScreen import ScreenSaverScreen
from Greetings_Page.GreetingsScreen import GreetingsScreen
##### Screen Imports #####

Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '320')
Config.set('graphics', 'borderless', '1')

class DashboardManager(ScreenManager):
    _touch_start_x = 0

    def on_touch_down(self, touch):
        log.debug(APP_ON_TOUCH_DOWN_EVENT)
        self._touch_start_x = touch.x
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        log.debug(APP_ON_TOUCH_UP_EVENT)
        swipe_distance = touch.x - self._touch_start_x
        if abs(swipe_distance) > 20:
            if swipe_distance > 0:
                self.transition.direction = 'right'
                self.current = self.previous()
            else:
                self.transition.direction = 'left'
                self.current = self.next()
        return super().on_touch_up(touch)


class DashboardApp(App):
    theme_colors: ListProperty = ListProperty([
        (0.961, 0.965, 0.98, 1),    # 0: Background (#f5f6fa)
        (0.184, 0.208, 0.259, 1),  # 1: Primary Text (#2f3542)
        (0.455, 0.725, 1.0, 1)     # 2: Accent Color (#74b9ff)
    ])
    screens: dict = {}
    cache = Cache()

    def build(self):
        self.screens = self.cache.get_screen_config()
        log.debug(BUILD_FUNC_LOG_MESSAGE)
        
        return Builder.load_file('main.kv')

    def on_start(self):
        log.debug(APP_ON_START_LOG_MESSAGE)
        
        self.root.ids.screen_manager.add_widget(ScreenSaverScreen(name='screensaver'))
        self.root.ids.screen_manager.add_widget(GreetingsScreen(name='greetings'))
        
        if self.screens["weather"]:    
            self.root.ids.screen_manager.add_widget(WeatherScreen(name='weather'))
        if self.screens["todo"]:
            self.root.ids.screen_manager.add_widget(TodoScreen(name='todo'))
        if self.screens["quote"]:
            self.root.ids.screen_manager.add_widget(QuoteScreen(name='quote'))
        if self.screens["calendar"]:
            self.root.ids.screen_manager.add_widget(CalendarScreen(name="calendar"))

if __name__ == '__main__':
    DashboardApp().run()