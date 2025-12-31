import streamlit as st


pg = st.navigation(
    [
        "Page/Screens.py",
        "Page/Todo.py",
        "Page/Meetings.py",
        "Page/Calendar.py",
        "Page/Publish_Commands.py"
    ])
pg.run()