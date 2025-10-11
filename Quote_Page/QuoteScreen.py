from kivy.properties import StringProperty
from CustomScreen.customScreen import CustomScreen
from Storage.Cache import Cache
from kivy.clock import Clock
from decouple import config
import requests
from Logger.Logger import log
from Static.Messages.messages import (
    QUOTE_ON_ENTER_EVENT, QUOTE_ON_ENTER_EVENT,
    QUOTE_ON_LEAVE_EVENT, QUOTE_UNSET_API_JOB,
    QUOTE_DEFAULT_DATA, QUOTE_API_URL, QUOTE_API_CALL_STATUS,
    QUOTE_UPDATE_SCREEN_DATA, QUOTE_API_CALL_INITIATE,
    QUOTE_API_RESPONSE_DATA, UPDATE_CACHE_DATA
)

class QuoteScreen(CustomScreen):
    quote_text = StringProperty("In the realm of servers and silence, only those who endure the wait will see the response....")
    cache = Cache()
    update_event = None
    api_call_frequency = config("quote_api_call_frequency", cast=int)

    def on_enter(self, *args):
        log.debug(QUOTE_ON_ENTER_EVENT)
        self.update_quote_data()

        log.debug(QUOTE_ON_ENTER_EVENT.format(self.api_call_frequency))
        self.update_event = Clock.schedule_interval(self.update_quote_data, self.api_call_frequency)
        return super().on_enter()

    def on_leave(self):
        log.debug(QUOTE_ON_LEAVE_EVENT)
        if self.update_event:
            log.debug(QUOTE_UNSET_API_JOB)
            self.update_event.cancel()
        return super().on_leave()
    
    def default_quote_data():
        log.debug(QUOTE_DEFAULT_DATA)
        return {
            'data': {
                'type': 'default',
                'content': 'To stand before a failing API is to stare into the abyss of your own creation — and choose to code again.', 
                'anime': {'name': 'API',}, 
                'character': {'name': 'Error'}
                }
            }

    def call_quote_api(self):
        data = None
        try:
            url = config("quote_api_path", cast=str)
            log.debug(QUOTE_API_URL.format(url))
            response = requests.get(url=url)
            log.debug(QUOTE_API_CALL_STATUS.format(response.status_code))
            data = response.json()
        except Exception as e:
            log.error(e)
            data = self.default_quote_data()
        return data 
      
    def update_quote_data(self):
        log.debug(QUOTE_UPDATE_SCREEN_DATA)
        data = self.cache.get_quote_data()
        if data is None:
            log.debug(QUOTE_API_CALL_INITIATE)
            data = self.call_quote_api()
            log.debug(QUOTE_API_RESPONSE_DATA.format(str(data)))
            if data.get("type", None) is None:
                self.cache.set_quote_data(data)
                log.debug(UPDATE_CACHE_DATA)

        data = data['data']
        self.quote_text = f"{data['content']}\n\n- {data['character']['name']}({data['anime']['name']})"

