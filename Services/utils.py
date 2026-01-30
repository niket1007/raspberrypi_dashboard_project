import json

def transform_screen_data(data: dict) -> str:
    sorted_data = sorted(data.items(), key=lambda i: int(i[0]))

    new_data = []
    for item in sorted_data:
        if item[0] != "-1":
            new_data.append({
                "name": item[1].get("name", None),
                "visibility": item[1].get("visible", True)
            })
    if "-1" in data:
        for item in data["-1"]:
            new_data.append({
                "name": item["name"],
                "visibility": item["visible"]
            })
    
    return json.dumps(new_data)


def transform_todo_str_to_list(data: str) -> list[str]|None:
    if data is None:
        return []
    data = data.replace("• ", "").split("\n")
    return data

def transform_todo_list_to_str(data: list[str]|None) -> str|None:
    if data == [] or data is None:
        return None
    return "\n".join(data)

def transform_meeting_str_to_list(data: str|None) -> list:
    if data is None:
        return []
    data = data.replace("• ", "").strip().split("\n")
    for index in range(len(data)):
        items = data[index].split(" ")
        data[index] = {
            "title": " ".join(items[:-2]).replace(":", ""),
            "date": items[-2],
            "time": items[-1]
        }
    return data

def transform_meeting_list_dict_to_str(data: list|dict) -> str|None:
    if data == [] or data is None:
        return None
    if isinstance(data, dict):
        return "• " + data["title"] + ": " + data["date"] + " " + data["time"] + "\n"
    else:
        combined_data = ""
        for item in data:
            combined_data += "• " + item["title"] + ": " + item["date"] + " " + item["time"] + "\n"
        return combined_data

def transform_calendar_str_to_list(data: str|None) -> list:
    if data is None:
        return {}
    data = json.loads(data)
    return data.items()

def transform_calendar_dict_to_str(old_data: str, data: dict) -> str:
    if old_data is None:
        old_data = {data["date"]: [data["event"]]}
    else:
        is_found = False
        old_data = json.loads(old_data)
        for key in old_data:
            if key ==  data["date"]:
                is_found = True
                old_data[key].append(data["event"])
        
        if(not is_found):
            # {'event': 'hjghjghj', 'date': '2026-01-29', 'is_append': True}
            old_data[data["date"]] = [data["event"]]
    return json.dumps(old_data)

def transform_delete_calendar_dict_to_str(old_data: str, delete: dict) -> str|None:
    if old_data is None:
        raise Exception("Nothing there to be deleted.")
    else:
        is_found = False
        old_data = json.loads(old_data)
        for key in old_data:
            if key == delete["date"]:
                for index,event in enumerate(old_data[key]):
                    if event.upper() == delete["event"].upper():
                        is_found = True
                        break
                if is_found:
                    break
        if is_found:
            old_data[key].pop(index)
            if len(old_data[key]) == 0:
                del old_data[key]
    
        return json.dumps(old_data) if old_data != {} else None
