import streamlit as st
from Services.Redis.redis import RedisStorage
from Services.Utils.utils import convert_calendar_dict_to_dataframe, convert_calendar_dataframe_to_dict

redis = RedisStorage()

if "Calendar" not in st.session_state:
    calendar_data = redis.get_calendar_user_data()
    st.session_state["Calendar"] = convert_calendar_dict_to_dataframe(calendar_data)

edited_df = st.data_editor(
    data=st.session_state["Calendar"], 
    column_config={
        "Date": st.column_config.DateColumn(
            label="Date", 
            format="YYYY-MM-DD", 
            default=None)
    },
    num_rows="dynamic")

is_submitted = st.button("Submit")

if is_submitted:
    data = convert_calendar_dataframe_to_dict(edited_df)
    redis.set_calendar_user_data(data) 
    st.session_state["Calendar"] = edited_df 
