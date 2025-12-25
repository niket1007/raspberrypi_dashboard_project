from redis import Redis as RedisConn
from decouple import config
from Services.Redis.default_data import CONFIG_SCREEN, TODO_DATA
import json

class RedisStorage:
    screens: list[dict] = []

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RedisStorage, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.redis = RedisConn(
            host=config("redis_host", cast=str),
            port=config("redis_port", cast=int),
            username=config("redis_username", cast=str, default=None),
            password=config("redis_password", cast=str, default=None),
            decode_responses=True
        )
    
    def get_screen_configuration(self) -> dict:
        data = self.redis.get("config:screens")
        if data is None:
            data = CONFIG_SCREEN
        else:
            data = json.loads(data)
        
        self.screens = data
        
        index = 0
        result = {}
        for screen in data:
            print(screen)
            if screen["visibility"] == True:
                result[index] = screen["name"]
                index += 1
        return result
    
    def get_todo_data(self):
        data = self.redis.get("pages:todo:data")
        if data is None:
            return TODO_DATA
        return data
