import streamlit as st
from Services.Redis.redis import RedisStorage
from Services.Utils.utils import convert_meetings_str_to_dataframe, convert_meetings_dataframe_to_str

redis = RedisStorage()
meetings_data = None
if "Meetings" in st.session_state:
    meetings_data = st.session_state["Meetings"]
else:
    meetings_data = redis.get_meetings_data()
    st.session_state["Meetings"] = meetings_data

meetings_data = convert_meetings_str_to_dataframe(meetings_data)

edited_df = st.data_editor(
    meetings_data, 
    column_config={
        "DateTime": st.column_config.DatetimeColumn(
            label="Timing",
            format="D MMM YYYY, h:mm A",
            required=True
        )
    },
    hide_index=True,
    num_rows='dynamic')

is_submit = st.button("Submit")

if is_submit:
    print(edited_df)
    data = convert_meetings_dataframe_to_str(edited_df)
    redis.set_meetings_data(data)