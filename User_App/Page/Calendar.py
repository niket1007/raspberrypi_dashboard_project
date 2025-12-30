import streamlit as st
from Services.Redis.redis import RedisStorage

redis = RedisStorage()
calendar_data = None
if "Calendar" in st.session_state:
    calendar_data = st.session_state["Calendar"]
else:
    calendar_data = redis.get_calendar_user_data()
    st.session_state["Calendar"] = calendar_data

date_input = st.date_input("Select the date", value=None)
date_title = st.text_input("Event Name", value=None)
is_submitted = st.button("Submit")

st.text_area("Calendar Data", value=str(calendar_data) ,disabled=True)

if is_submitted:
    errors = []
    for field in [("Date", date_input), ("Event Name", date_title)]:
        if field[1] is None:
            errors.append(field[0])
    
    if len(errors) > 0:
        st.error(", ".join(errors) + " is required.")
    else:
        if str(date_input) in calendar_data:
            calendar_data[str(date_input)] += f", {date_title}"
        else:
            calendar_data[str(date_input)] = f"{date_title}"

        redis.set_calendar_user_data(calendar_data)
        st.write(calendar_data)
        
