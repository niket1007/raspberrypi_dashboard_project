from kivy.properties import StringProperty
from CustomScreen.customScreen import CustomScreen
from kivy.clock import Clock
from Storage.Cache import Cache
import requests
from decouple import config
from Logger.Logger import log
from Static.Messages.messages import (
    WEATHER_ON_ENTER_EVENT, WEATHER_SET_API_JOB,
    WEATHER_ON_LEAVE_EVENT, WEATHER_UNSET_API_JOB,
    WEATHER_DEFAULT_DATA, WEATHER_UPDATE_SCREEN_DATA,
    WEATHER_API_CALL_INITIATE, WEATHER_API_CALL_STATUS,
    WEATHER_API_CALL_DATA, WEATHER_API_URL, WEATHER_API_RESPONSE_DATA,
    UPDATE_CACHE_DATA)

class WeatherScreen(CustomScreen):
    temp = StringProperty("--°")
    description = StringProperty("Loading...")
    city = StringProperty("Loading...")
    min_max_temp = StringProperty("--/--")
    # background_color = ListProperty([0.961, 0.965, 0.98, 1]) # Default soothing color

    update_event = None
    reset_event = None
    api_call_frequency = config("weather_api_call_frequency", cast=int)
    cache = Cache()

    def on_enter(self):
        log.debug(WEATHER_ON_ENTER_EVENT)
        self.update_weather()

        log.debug(WEATHER_SET_API_JOB.format(self.api_call_frequency))
        self.update_event = Clock.schedule_interval(self.update_weather, self.api_call_frequency)
        return super().on_enter()


    def on_leave(self):
        log.debug(WEATHER_ON_LEAVE_EVENT)
        if self.update_event:
            log.debug(WEATHER_UNSET_API_JOB)
            self.update_event.cancel()
        return super().on_leave()

    def default_weather_data(self):
        log.debug(WEATHER_DEFAULT_DATA)
        return {
            "type": "default",
            "location": {"name": "Unknown"},
            "current": {
                "temp_c": "0",
                "condition": {"text": "The API has fallen. Yet, in its failure, it reveals the truth we always feared — that stability was only an illusion."},
                "feelslike_c": "0"
            }
        }

    def call_weather_api(self):
        try:
            lat, long = 28.6, 77.2
            log.debug(WEATHER_API_CALL_DATA.format(lat, long))
            url = f"{config('weather_api_path', cast=str)}?key={config('weather_api_key')}&q={lat},{long}"
            log.debug(WEATHER_API_URL.format(url))
            response = requests.request("GET", url)
            log.debug(WEATHER_API_CALL_STATUS.format(response.status_code))
            api_data = response.json()
        except Exception as e:
            log.error(e)
            api_data = self.default_weather_data()
        return api_data
        
    def update_weather(self, dt: float|None=None):
        log.debug(WEATHER_UPDATE_SCREEN_DATA)
        data = self.cache.get_weather_data()
        if data is None:
            log.debug(WEATHER_API_CALL_INITIATE)
            data = self.call_weather_api()
            log.debug(WEATHER_API_RESPONSE_DATA.format(str(data)))
            if data.get("type", None) is None:
                self.cache.set_weather_data(data)
                log.debug(UPDATE_CACHE_DATA)

        self.city = data['location']['name']
        self.temp = f"{int(data['current']['temp_c'])}°C"
        self.description = data['current']['condition']['text'].upper()
        self.min_max_temp = f"Feels like {int(data['current']['feelslike_c'])}°"