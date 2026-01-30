from redis import Redis
from decouple import config
import json

from Services.utils import (
    transform_screen_data, transform_todo_str_to_list, transform_todo_list_to_str,
    transform_meeting_str_to_list, transform_meeting_list_dict_to_str,
    transform_calendar_str_to_list, transform_calendar_dict_to_str, 
    transform_delete_calendar_dict_to_str)

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
        data = transform_screen_data(data)
        self._redis.set("config:screens", data)
    
    def get_todo_data(self) -> list[str]|None:
        data = self._redis.get("pages:todo:data")
        return transform_todo_str_to_list(data)
    
    def set_todo_data(self, data: list|None) -> None:
        data = transform_todo_list_to_str(data)
        if data is None:
            self._redis.delete("pages:todo:data")
        else:
            self._redis.set("pages:todo:data", data)
    
    def get_meetings_data(self) -> str:
        data = self._redis.get("pages:meetings:data")
        data = transform_meeting_str_to_list(data)
        return data
    
    def set_meetings_data(self, data: str|None) -> None:
        data = transform_meeting_list_dict_to_str(data)
        if data is None:
            self._redis.delete("pages:meetings:data")
        else:
            self._redis.set("pages:meetings:data", data)
    
    def append_meeting_data(self, data: list|dict) -> None:
        data = transform_meeting_list_dict_to_str(data)
        self._redis.append("pages:meetings:data", data)

    def get_calendar_user_data(self) -> dict:
        data = self._redis.get("pages:calendar:user_data")
        data = transform_calendar_str_to_list(data)
        return data

    def set_calendar_user_data(self, new_data: dict) -> None:
        exist_data = self._redis.get("pages:calendar:user_data")
        new_data = transform_calendar_dict_to_str(exist_data, new_data)
        self._redis.set("pages:calendar:user_data", new_data)
    
    def delete_calendar_user_data(self, delete_data: dict) -> None:
        exist_data = self._redis.get("pages:calendar:user_data")
        new_data = transform_delete_calendar_dict_to_str(exist_data, delete_data)
        print(exist_data, new_data)
        if new_data is None:
            self._redis.delete("pages:calendar:user_data")
        else:
            self._redis.set("pages:calendar:user_data", new_data)

    
    def publish_mesage(self, message: str):
        num = self._redis.publish("Dashboard-Commands", message)
        return num