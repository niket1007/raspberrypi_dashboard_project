from redis import Redis
from decouple import config
import threading


class RedisSub:

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RedisSub, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self._redis = Redis(
            host=config("redis_host", cast=str),
            port=config("redis_port", cast=int),
            username=config("redis_username", cast=str),
            password=config("redis_password", cast=str),
            decode_responses=True
        )
        sub_thread = threading.Thread(target=self.__start_listening, daemon=True).start()

    def __start_listening(self):
        sub = self._redis.pubsub()
        sub.subscribe("Dashboard-Commands")
        
        for message in sub.listen():
            print(message.get("data", None))
