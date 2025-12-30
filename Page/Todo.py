import streamlit as st
from Services.Redis.redis import RedisStorage
from Services.Utils.utils import convert_todo_str_to_dataframe, convert_todo_dataframe_to_str

redis = RedisStorage()
todo_data = None
if "Todo" in st.session_state:
    todo_data = st.session_state["Todo"]
else:
    todo_data = redis.get_todo_data()
    st.session_state["Todo"] = todo_data

todo_data = convert_todo_str_to_dataframe(todo_data)

edited_df = st.data_editor(
    todo_data, 
    column_config={
        "Completed": st.column_config.CheckboxColumn(
            "Is completed?",
            default=False
        )
    },
    hide_index=True,
    num_rows='dynamic')

is_submit = st.button("Submit")

if is_submit:
    data = convert_todo_dataframe_to_str(edited_df)
    redis.set_todo_data(data)