from redis import Redis
from decouple import config
import json

class RedisStorage:

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
        if data is not None:
            data = json.loads(data)
        return data
    
    def set_screen_configuration(self, data: dict) -> None:
        data = json.dumps(data)
        self._redis.set("config:screens", data)
    
    def get_todo_data(self) -> str:
        print("Called")
        data = self._redis.get("pages:todo:data")
        return data
    
    def set_todo_data(self, data: str) -> None:
        self._redis.set("pages:todo:data", data)
    
    def get_meetings_data(self) -> str:
        data = self._redis.get("pages:meetings:data")
        return data
    
    def set_meetings_data(self, data: str) -> None:
        self._redis.set("pages:meetings:data", data)

    def get_calendar_user_data(self) -> dict|None:
        data = self._redis.get("pages:calendar:user_data")
        if data is not None:
            data = json.loads(data)
        return data

    def set_calendar_user_data(self, data: dict) -> None:
        data = json.dumps(data)
        self._redis.set("pages:calendar:user_data", data)
    
    def publish_mesage(self, message: str):
        num = self._redis.publish("Dashboard-Commands", message)
        return num