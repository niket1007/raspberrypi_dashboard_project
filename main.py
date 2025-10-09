from kivy.config import Config
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty
from kivy.clock import Clock
from Weather_Page.WeatherScreen import WeatherScreen
from Todo_Page.TodoScreen import TodoScreen
from Quote_Page.QuoteScreen import QuoteScreen
from Calendar_Page.CalendarScreen import CalendarScreen

Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '320')

SHOW_SPECIAL_SCREEN = True


class SpecialScreen(Screen):
    pass

class DashboardManager(ScreenManager):
    _touch_start_x = 0

    def on_touch_down(self, touch):
        self._touch_start_x = touch.x
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
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
    theme_colors = ListProperty([
        (0.961, 0.965, 0.98, 1),    # 0: Background (#f5f6fa)
        (0.184, 0.208, 0.259, 1),  # 1: Primary Text (#2f3542)
        (0.455, 0.725, 1.0, 1)     # 2: Accent Color (#74b9ff)
    ])

    def build(self):
        # This is the line we changed.
        return Builder.load_file('main.kv')

    def on_start(self):
        # We need to use self.root to get the ScreenManager now
        self.root.ids.screen_manager.add_widget(WeatherScreen(name='weather'))
        self.root.ids.screen_manager.add_widget(TodoScreen(name='todo'))

        if SHOW_SPECIAL_SCREEN:
            self.root.ids.screen_manager.add_widget(SpecialScreen(name='special'))

        self.root.ids.screen_manager.add_widget(QuoteScreen(name='quote'))
        self.root.ids.screen_manager.add_widget(CalendarScreen(name="calendar"))



if __name__ == '__main__':
    DashboardApp().run()