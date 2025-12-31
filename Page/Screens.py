import streamlit as st
from streamlit_sortables import sort_items
from Services.Redis.redis import RedisStorage

redis = RedisStorage()
screens = None
if "Screens" not in st.session_state:
    screens = redis.get_screen_configuration()
    screen_lists = [
        {"header": "Visible", "items": []},
        {"header": "Hidden", "items": []}
    ]

    for screen in screens:
        index = 0 if screen["visibility"] else 1
        screen_lists[index]["items"].append(screen["name"])

    st.session_state["Screens"] = screen_lists

new_list = sort_items(st.session_state["Screens"], multi_containers=True)
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
    st.session_state["Screens"] = new_list