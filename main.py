from flask import Flask, request, jsonify
from decouple import config
from redis import Redis
import json

app = Flask(__name__)

CLIENT_ID = config("api_client_id", cast=str)
CLIENT_SECRET = config("api_client_secret", cast=str)

_redis = Redis(
    host=config("redis_host", cast=str),
    port=config("redis_port", cast=int),
    username=config("redis_username", cast=str, default=None),
    password=config("redis_password", cast=str, default=None),
    decode_responses=True
)

@app.route("/push_notifications", methods=["POST"])
def push_notifications():

    username = request.headers.get("Username", None)
    password = request.headers.get("Password", None)

    if username != CLIENT_ID or password != CLIENT_SECRET:
        return jsonify({
            "message": "Unauthorized user"
        }), 403

    body = request.json

    _redis.publish("live_notifications", json.dumps(body))

    return jsonify({
        "msg": "Message Published."
    }), 202

if __name__ == "__main__":
    app.run(host=config("host", cast=str), port=config("port", cast=int))