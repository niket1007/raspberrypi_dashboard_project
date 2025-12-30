from redis import Redis
from decouple import config
from Services.Static.static import REDIS
import json

class RedisStorage:
    
    QUOTE_EXPIRE = config("quote_redis_data_expire", cast=int)
    WEATHER_EXPIRE = config("weather_redis_data_expire")

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RedisStorage, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self._redis = Redis(
            host=config("redis_host", cast=str),
            port=config("redis_port", cast=int),
            username=config("redis_username", cast=str, default=None),
            password=config("redis_password", cast=str, default=None),
            decode_responses=True
        )
    
    def get_screen_configuration(self) -> dict:
        data = self._redis.get("config:screens")
        if data is None:
            data = REDIS["CONFIG_SCREEN"]
        else:
            data = json.loads(data)
        
        return data
    
    def get_todo_data(self) -> str:
        data = self._redis.get("pages:todo:data")
        if data is None or data == "":
            return REDIS["TODO_DATA"]
        return data
    
    def get_meetings_data(self) -> str:
        data = self._redis.get("pages:meetings:data")
        if data is None or data == "":
            return REDIS["MEETINGS_DATA"]
        return data

    def set_quote_data(self, data) -> None:
        stringfied = json.dumps(data)
        self._redis.set("pages:quote:api_data", stringfied, ex=self.QUOTE_EXPIRE)
    
    def get_quote_data(self) -> dict|None:
        data = self._redis.get("pages:quote:api_data")
        if data is not None:
            data = json.loads(data)
        return data

    def set_weather_data(self, data: str) -> None:
        self._redis.set("pages:weather:api_data", data, ex=self.WEATHER_EXPIRE)
    
    def get_weather_data(self) -> str|None:
        data = self._redis.get("pages:weather:api_data")
        return data

    def get_calendar_user_data(self) -> dict|None:
        data = self._redis.get("pages:calendar:user_data")
        if data is not None:
            data = json.loads(data)
        return data