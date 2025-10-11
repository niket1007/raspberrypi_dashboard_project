from redis import Redis
from decouple import config
from Logger.Logger import log
from Static.Messages.messages import (
    CACHE_NEW_MAGIC_METHOD, CACHE_REDIS_INITIATION,
    CACHE_SET_KEY_VALUE, CACHE_GET_KEY_VALUE, CACHE_CREATE_INSTANCE)

class Cache:
    weather_data = None
    redis = None

    def __new__(cls):
        log.debug(CACHE_NEW_MAGIC_METHOD)
        if not hasattr(cls, 'instance'):
            log.debug(CACHE_CREATE_INSTANCE)
            cls.instance = super(Cache, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        log.debug(CACHE_REDIS_INITIATION)
        self.redis = Redis(
            host=config("redis_host"), 
            port=config("redis_port", cast=int),
            username=config("redis_username"),
            password=config("redis_password"),
            decode_responses=True)

    def set_weather_data(self, data: dict|None) -> None:
        ttl = config("weather_api_call_frequency", cast=int)
        key = "weather:api_data"
        log.debug(CACHE_SET_KEY_VALUE.format(key, ttl, str(data)))
        self.redis.json().set(name=key, path="$", obj=data)
        self.redis.expire(name=key, time=ttl)

    def get_weather_data(self) -> dict|None:
        data = self.redis.json().get(name="weather:api_data")
        log.debug(CACHE_GET_KEY_VALUE.format("weather:api_data", str(data)))
        return data

    def get_screen_config(self) -> dict|None:
        data = self.redis.json().get("config:screens")
        log.debug(CACHE_GET_KEY_VALUE.format("config:screens", str(data)))
        return data    
    
    def set_quote_data(self, data: dict|None) -> None:
        key = "quote:api_data"
        ttl = config("quote_api_call_frequency", cast=int)
        log.debug(CACHE_SET_KEY_VALUE.format(key, ttl, str(data)))
        self.redis.json().set(name=key, path="$", obj=data)
        self.redis.expire(name=key, time=ttl)
    
    def get_quote_data(self) -> dict|None:
        data = self.redis.json().get("quote:api_data")
        log.debug(CACHE_GET_KEY_VALUE.format("quote:api_data", str(data)))
        return data
    
    def get_user_monthly_events(self, field: str) -> dict|None:
        data = self.redis.json().get("calendar:user_events", f"$['{field}']")
        log.debug(CACHE_GET_KEY_VALUE.format("calendar:user_events", str(data)))
        return data