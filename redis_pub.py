from redis import Redis
from decouple import config

_redis = Redis(
            host=config("redis_host", cast=str),
            port=config("redis_port", cast=int),
            username=config("redis_username", cast=str),
            password=config("redis_password", cast=str),
            decode_responses=True
        )


result = _redis.pubsub_numsub("Dashboard-Commands")
print(result)
# if result[0][1] == 0:
#     print("No subscriber present for channel")
# else:
while True:
    message = input("Enter a message\n")
    _redis.publish("Dashboard-Commands", message)