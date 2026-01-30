from flask import Flask, render_template, request
from Services.redis_service import RedisStorage
from decouple import config

app = Flask(__name__)

@app.route("/", methods=["GET"])
def screen_config_func():
    redis = RedisStorage()
    screen_data = redis.get_screen_configuration()
    return render_template(
        "Screen_Config.html", 
        data={
            "screens": enumerate(screen_data, start=1),
            "length": len(screen_data)
        })

@app.route("/process-screen-data", methods=["POST"])
def process_screen_data():
    try:
        data = request.get_json()
        if data is None:
            return {"error": "Data is empty."}
        redis = RedisStorage()
        redis.set_screen_configuration(data)
        return {"success": "Data updated successfully"}
    except Exception as e:
        return {"error": "Issue in server."}

@app.route("/todo")
def todo_func():
    redis = RedisStorage()
    data = redis.get_todo_data()
    return render_template(
        template_name_or_list="Todo.html", 
        data={
            "todos": enumerate(data, start=1),
            "length": len(data)
        })

@app.route("/update-todo-data", methods=["POST"])
def update_todo_data():
    try:
        data = request.get_json()
        if data is None:
            return {"error": "Data is empty."}
        redis = RedisStorage()
        redis.set_todo_data(data)
        return {"success": "Data updated successfully"}
    except Exception as e:
        return {"error": "Issue in server."}

@app.route("/meetings")
def meetings_func():
    redis = RedisStorage()
    data = redis.get_meetings_data()
    return render_template(
        "Meeting.html",
        data={
            "events": enumerate(data, start=1),
            "length": len(data)
        })

@app.route("/update-meeting-data", methods=["POST"])
def update_meeting_data():
    try:
        data = request.get_json()
        if data is None:
            return {"error": "Data is empty."}
        redis = RedisStorage()
        if isinstance(data, dict) and data.get("is_append", False):
            redis.append_meeting_data(data)
        else:
            redis.set_meetings_data(data)
        return {"success": "Data updated successfully"}
    except Exception as e:
        return {"error": "Issue in server."}

@app.route("/calendar")
def calendar_func():
    redis = RedisStorage()
    data = redis.get_calendar_user_data()
    print(data)
    return render_template(
        template_name_or_list="Calendar.html",
        data={
            "events": data,
            "length": len(data)
        })


@app.route("/update-calendar-data", methods=["POST"])
def update_calendar_data():
    # try:
        data = request.get_json()
        if data is None:
            return {"error": "Data is empty."}
        redis = RedisStorage()
        print(data)
        if data.get("is_append", False):
            redis.set_calendar_user_data(data)
        else:
            redis.delete_calendar_user_data(data)

        return {"success": "Data updated successfully"}
    # except Exception as e:
    #     print(str(e))
    #     return {"error": "Issue in server."}

if __name__ == "__main__":
    app.run(
        host=config("flask_host", cast=str), 
        port=config("flask_port", cast=int), 
        debug=config("flask_debug", cast=bool))