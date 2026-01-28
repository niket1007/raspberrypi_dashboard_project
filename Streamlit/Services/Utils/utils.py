import pandas as pd
import datetime

def isDictEmpty(data: dict) -> bool:
    return data == {0: None} or data == {}

def convert_todo_str_to_dataframe(data: str|None) -> pd.DataFrame:
    if data is None or data == "":
        data = pd.DataFrame(columns=["Todo", "Completed"])
    else:
        data = data.replace("•", "").strip().split("\n")
        data = {"Todo": data, "Completed": [False]*len(data)}
        data = pd.DataFrame(data)
    
    return data

def convert_todo_dataframe_to_str(data: pd.DataFrame) -> str|None:
    data = data.to_dict()
    if isDictEmpty(data["Todo"]):
        return None
    todos = [data["Todo"][index] for index in data["Todo"] if not data["Completed"][index]]
    result = ""
    if len(todos) > 0:
        for index in range(len(todos)):
            result += "• " + todos[index]
            if index != len(todos)-1:
                result += "\n"
    return result
        
def convert_meetings_str_to_dataframe(data: str|None) -> pd.DataFrame:
    if data is None or data == "":
        new_data = pd.DataFrame(columns=["Meeting", "DateTime"])
    else:
        new_data = []
        data = data.replace("•", "").strip().split("\n")
        
        for meeting in data:
            title, date_time = meeting.split("(")
            date_time = date_time.replace(")", "")
            new_data.append(
                [title.strip(), 
                 datetime.datetime.strptime(date_time, "%d %b %Y, %I:%M %p")])
        
        new_data = pd.DataFrame(new_data, columns=["Meeting", "DataTime"])
    return pd.DataFrame(new_data)

def convert_meetings_dataframe_to_str(data: pd.DataFrame) -> str|None:
    data = data.to_dict()

    if isDictEmpty(data['Meeting']):
        return None
    else:
        meetings = []
        for index in data.get("Meeting", []):
            meeting_name = data["Meeting"][index]
            date_time = data["DateTime"][index]
            if isinstance(date_time, str):
                date_time = datetime.datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S.%f")
            date_time = date_time.strftime("%d %b %Y, %I:%M %p")
            meetings.append(
                f"• {meeting_name}({date_time})"
            )
        result = "\n".join(meetings)
        return result

def convert_calendar_dict_to_dataframe(data: dict|None) -> pd.DataFrame:
    print("cc", data)
    if data is None:
        new_data = pd.DataFrame(columns=["Date", "Events"])
    else:
        new_data = []
        data = data.items()

        for item in data:
            new_data.append(
                [datetime.datetime.strptime(item[0], "%Y-%m-%d"),
                item[1]])
        new_data = pd.DataFrame(new_data, columns=["Date", "Events"])
    return new_data

def convert_calendar_dataframe_to_dict(data: pd.DataFrame) -> dict|None:
    data = data.to_dict()
    if isDictEmpty(data["Date"]):
        return None

    new_data = {}
    for index in data.get("Date", []):
        date = data["Date"][index]
        if isinstance(date, str):
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
        date = date.strftime("%Y-%m-%d")
        new_data[date] = data["Events"][index]

    return new_data
