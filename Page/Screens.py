import streamlit as st
from streamlit_sortables import sort_items
from Services.Redis.redis import RedisStorage

redis = RedisStorage()
screens = None
if "Screens" in st.session_state:
    screens = st.session_state["Screens"]
else:
    screens = redis.get_screen_configuration()
    st.session_state["Screens"] = screens

screen_lists = [
    {"header": "Visible", "items": []},
    {"header": "Hidden", "items": []}
]

for screen in screens:
    index = 0 if screen["visibility"] else 1
    screen_lists[index]["items"].append(screen["name"])

new_list = sort_items(screen_lists, multi_containers=True)
is_submit = st.button("Submit")

if is_submit:
    new_screens = []
    for screen_name in new_list[0]["items"]:
        new_screens.append({
            "name": screen_name,
            "visibility": True
        })
    for screen_name in new_list[1]["items"]:
        new_screens.append({
            "name": screen_name,
            "visibility": False
        })
    redis.set_screen_configuration(new_screens)