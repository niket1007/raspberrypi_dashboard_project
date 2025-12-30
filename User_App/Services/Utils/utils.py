import pandas as pd
import datetime

def convert_todo_str_to_dataframe(data: str|None) -> pd.DataFrame:
    if data is None or data == "":
        data = {"Todo": [""], "Completed": [False]}
    else:
        data = data.replace("•", "").strip().split("\n")
        data = {"Todo": data, "Completed": [False]*len(data)}
    
    return pd.DataFrame(data)

def convert_todo_dataframe_to_str(data: pd.DataFrame) -> str:
    data = data.to_dict()
    todos = [data["Todo"][index] for index in data["Todo"] if not data["Completed"][index]]
    result = ""
    if len(todos) > 0:
        for index in range(len(todos)):
            result += "• " + todos[index]
            if index != len(todos)-1:
                result += "\n"
    return result
        
def convert_meetings_str_to_dataframe(data: str|None) -> pd.DataFrame:
    new_data = {"Meeting": [], "DateTime": []}
    if data is None or data == "":
        new_data["Meeting"].append("")
        new_data["DateTime"].append(None)
    else:
        data = data.replace("•", "").strip().split("\n")
        for meeting in data:
            title, date_time = meeting.split("(")
            date_time = date_time.replace(")", "")
            new_data["Meeting"].append(title.strip())
            new_data["DateTime"].append(datetime.datetime.strptime(date_time, "%d %b %Y, %I:%M %p"))
    
    return pd.DataFrame(new_data)

def convert_meetings_dataframe_to_str(data: pd.DataFrame) -> str:
    data = data.to_dict()
    meetings = []
    for index in data["Meeting"]:
        meeting_name = data["Meeting"][index]
        date_time = data["DateTime"][index]
        date_time = date_time.strftime("%d %b %Y, %I:%M %p")
        meetings.append(
            f"• {meeting_name}({date_time})"
        )
    result = "\n".join(meetings)
    return result
        