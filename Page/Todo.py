import streamlit as st
from Services.Redis.redis import RedisStorage
from Services.Utils.utils import convert_todo_str_to_dataframe, convert_todo_dataframe_to_str

redis = RedisStorage()

if "Todo" not in st.session_state:
    todo_data = redis.get_todo_data()
    st.session_state["Todo"] = convert_todo_str_to_dataframe(todo_data)

edited_df = st.data_editor(
    st.session_state["Todo"], 
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
    st.session_state["Todo"] = edited_df