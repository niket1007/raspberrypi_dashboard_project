import tkinter as tk
from tkinter import ttk, font
import time
import datetime
import holidays
from decouple import config

# Services
from Services.Style import GreetingsPageStyle
from Services.Redis.redis import RedisStorage
from Services.utils import Utils

class GreetingsPage(tk.Frame):

    DATETIME_UPDATE_TIMER = config("date_time_update_frequency", cast=int)
    WEATHER_UPDATE_TIMER = config("weather_api_call_frequency", cast=int)
    TODO_UPDATE_TIMER = config("todo_redis_frequency", cast=int)
    MEETING_UPDATE_TIMER = config("meetings_redis_frequency", cast=int)
    EVENTS_UPDATE_TIMER = config("calendar_update_frequency", cast=int)
    QUOTE_UPDATE_TIMER = config("quote_sliding_frequency", cast=int)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.widgetName = "" # Kept empty for styling
        self._redis = RedisStorage()
        self._utils = Utils()

        self.bold_font_11 = font.Font(self, **GreetingsPageStyle.BoldFont11)
        self.normal_font_9 = font.Font(self, **GreetingsPageStyle.NormalFont9)
        self.bold_font_9 = font.Font(self, **GreetingsPageStyle.BoldFont9)
        self.underline_bold_9 = font.Font(self, **GreetingsPageStyle.UnderlineBold9)

        top_frame_1 = tk.Frame(self, **GreetingsPageStyle.FrameOne)
        top_frame_1.place(**GreetingsPageStyle.TopFrame1Place)

        top_frame_2 = tk.Frame(self, **GreetingsPageStyle.FrameOne)
        top_frame_2.place(**GreetingsPageStyle.TopFrame2Place)

        mid_frame_1 = tk.Frame(self, **GreetingsPageStyle.FrameTwo)
        mid_frame_1.place(**GreetingsPageStyle.MidFrame1Place)

        mid_frame_2 = tk.Frame(self, **GreetingsPageStyle.FrameTwo)
        mid_frame_2.place(**GreetingsPageStyle.MidFrame2Place)

        second_last_frame = tk.Frame(self, **GreetingsPageStyle.FrameOne)
        second_last_frame.place(**GreetingsPageStyle.SecondLastFramePlace)

        last_frame_1 = tk.Frame(self, **GreetingsPageStyle.FrameTwo)
        last_frame_1.place(**GreetingsPageStyle.LastFrame1Place)

        last_frame_2 = tk.Frame(self, **GreetingsPageStyle.FrameTwo)
        last_frame_2.place(**GreetingsPageStyle.LastFrame2Place)

        ###### Date and Time Fields ######
        self.time_label = ttk.Label(
            top_frame_1, font=self.bold_font_11,**GreetingsPageStyle.LabelWithoutText)
        self.time_label.place(**GreetingsPageStyle.TimeLablePlace)

        self.date_label = ttk.Label(
            top_frame_1, font=self.normal_font_9, **GreetingsPageStyle.LabelWithoutText)
        self.date_label.place(**GreetingsPageStyle.DateLabelPlace)

        ###### Temperature Fields ######
        self.temp_label = ttk.Label(
            top_frame_2, font=self.bold_font_11, **GreetingsPageStyle.LabelWithoutText)
        self.temp_label.place(**GreetingsPageStyle.TempLabelPlace)

        self.temp_loc_label = ttk.Label(
            top_frame_2, font= self.normal_font_9, **GreetingsPageStyle.LabelWithoutText)   
        self.temp_loc_label.place(**GreetingsPageStyle.TempLocLabelPlace)

        ###### Todo's Fields ######
        todo_label = ttk.Label(
            mid_frame_1, text="Todo", font=self.bold_font_11, **GreetingsPageStyle.LabelWithoutText)
        todo_label.place(**GreetingsPageStyle.TodoLabelPlace)

        self.todo_items = ttk.Label(
            mid_frame_1, font= self.normal_font_9, **GreetingsPageStyle.LabelWithoutText)
        self.todo_items.place(**GreetingsPageStyle.TodoItemsPlace)

        self.todo_more = ttk.Label(
            mid_frame_1, font=self.underline_bold_9, **GreetingsPageStyle.LabelWithoutText)
        self.todo_more.place(**GreetingsPageStyle.TodoMorePlace)

        ###### Meetings Fields ######
        meetings_label = ttk.Label(
            mid_frame_2, text="Meetings", font=self.bold_font_11, **GreetingsPageStyle.LabelWithoutText)
        meetings_label.place(**GreetingsPageStyle.MeetingsLabelPlace)

        self.meetings_items = ttk.Label(
            mid_frame_2, font=self.normal_font_9, **GreetingsPageStyle.LabelWithoutText)
        self.meetings_items.place(**GreetingsPageStyle.MeetingsItemsPlace)

        self.meetings_more = ttk.Label(
            mid_frame_2, font=self.underline_bold_9, **GreetingsPageStyle.LabelWithoutText)
        self.meetings_more.place(**GreetingsPageStyle.MeetingsMorePlace)

        ###### Events Fields ######
        event_label = ttk.Label(
            second_last_frame, text="Events", font=self.bold_font_11, **GreetingsPageStyle.LabelWithoutText)
        event_label.place(**GreetingsPageStyle.EventLabelPlace)

        self.events_item_1 = ttk.Label(
            second_last_frame, font=self.normal_font_9, **GreetingsPageStyle.LabelWithoutText)
        self.events_item_1.place(**GreetingsPageStyle.EventsItem1Place)

        self.events_item_2 = ttk.Label(
            second_last_frame, font=self.normal_font_9, **GreetingsPageStyle.LabelWithoutText)
        self.events_item_2.place(**GreetingsPageStyle.EventsItem2Place)

        self.events_item_3 = ttk.Label(
            second_last_frame, font=self.normal_font_9, **GreetingsPageStyle.LabelWithoutText)
        self.events_item_3.place(**GreetingsPageStyle.EventsItem3Place)

        self.events_item_4 = ttk.Label(
            second_last_frame, font=self.normal_font_9, **GreetingsPageStyle.LabelWithoutText)
        self.events_item_4.place(**GreetingsPageStyle.EventsItem4Place)

        self.events_more = ttk.Label(
            second_last_frame, font=self.underline_bold_9, **GreetingsPageStyle.LabelWithoutText)
        self.events_more.place(**GreetingsPageStyle.EventsMorePlace)

        ###### Quote Fields #####
        quote_label = ttk.Label(
            last_frame_1, text="Quote", font= self.bold_font_9, **GreetingsPageStyle.LabelWithoutText)
        quote_label.place(**GreetingsPageStyle.QuoteLabelPlace)

        self.quote_text = ttk.Label(
            last_frame_2, font= self.bold_font_9, **GreetingsPageStyle.LabelWithoutText)
        self.quote_text.place(**GreetingsPageStyle.QuoteTextPlace)


        self.update_time_and_greeting()
        self.update_weather()
        self.update_quote()
        self.update_todos()
        self.update_meetings()
        self.update_events()

    def update_time_and_greeting(self):
        
        current_time = time.strftime("%I:%M:%S %p")
        current_date = time.strftime(r"%A, %B %d, %Y")

        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        
        self.after(self.DATETIME_UPDATE_TIMER, self.update_time_and_greeting)
    
    def update_weather(self):
        try:
            data = self._redis.get_weather_data()
            if data is None:
                data = self._utils.call_weather_api()
            
            temp = f"{data['temp']}°C"
            location = f"{data['city_name']}, {data['country']}"

            self.temp_label.config(text=temp)
            self.temp_loc_label.config(text=location)
        
        except Exception as e:
            print("Error update_weather(greetingsPage)", e)
            self.temp_label.config(text="XX")
            self.temp_loc_label.config(text="XXXXXXX")
        
        finally:
            self.after(self.WEATHER_UPDATE_TIMER, self.update_weather)
    
    def update_todos(self):
        try:
            data = self._redis.get_todo_data(default_msg=False)
            if data is not None:
                todos_count = 0
                todos_show = ""
                for todo in data.split("•"):
                    if len(todo) != 0:
                        if todos_count < 3:
                            todo = todo.replace("\n", "").strip()
                            todos_show += "• " + todo + "\n"
                        todos_count += 1
                self.todo_items.config(text=todos_show)
                if (todos_count - 3) > 0:
                    self.todo_more.config(text=f"+{todos_count-3} more")
            else:
                self.todo_items.config(text="• No todos")
        except Exception as e:
            print("Error: update_todos(greetingsPage)", e)
            self.todo_items.config(text="• Error**")
        finally:
            self.after(self.TODO_UPDATE_TIMER, self.update_todos)

    def update_quote(self):
        try:
            data = self._redis.get_quote_data()
            if data is None:
                data = self._utils.fetch_quote_data()
                old_quote = ""
            else:
                old_quote = self.quote_text.cget("text")
                if old_quote is None:
                    old_quote = ""

            full_quote = data["quote"]

            diff = (len(full_quote) - len(old_quote))
            if diff == len(full_quote):
                new_index = 0
            else:
                new_index = diff + 1

            text = full_quote[new_index::]
            self.quote_text.config(text = text)
        except Exception as e:
            print("Error: update_quote(greetingsPage)", str(e))
            self.quote_text.config(text="Error while fetching")
        finally:
            self.after(ms=self.QUOTE_UPDATE_TIMER, func=self.update_quote)
    
    def update_meetings(self):
        try:
            data = self._redis.get_meetings_data()
            meetings = ""
            if data is not None:
                meetings_count = 0
                today_date = str(datetime.date.today())  
                for meeting in data.split("•"):
                    if len(meeting) != 0:
                        if today_date in meeting and meetings_count < 3:
                            meetings += f"• {meeting.replace(today_date, '')} \n"
                            meetings_count += 1
                self.meetings_items.config(text=meetings)
                if (meetings_count - 3) > 0:
                    self.meetings_more.config(text=f"+{meetings_count-3} more")

            if len(meetings) == 0:
                self.meetings_items.config(text="• No Meetings")
        except Exception as e:
            print("Error: update_meetings(greetingsPage)", str(e))
            self.meetings_items.config(text="• Error**")
        finally:
            self.after(self.MEETING_UPDATE_TIMER, self.update_meetings)
    
    def update_events(self):
        try:
            user_event_data = self._redis.get_calendar_user_data()  
            year = datetime.date.today().year
            month = datetime.date.today().month
            today_day = datetime.date.today().day      
            all_holidays = holidays.country_holidays("IN", years=year)
            fields = [self.events_item_1, self.events_item_2, self.events_item_3, self.events_item_4]        
            show_more = False
            month_events = {}
            
            yyyy_mm = f"{year}-0{month}-" if month < 10 else f"{year}-{month}-"

            for date in user_event_data:
                day = int(date[-2:])
                if yyyy_mm in date and day >= today_day:
                    month_events[day] = user_event_data[date]

            for date in all_holidays:
                if date.year == year and date.month == month and date.day >= today_day:
                    day = date.day
                    if day in month_events:
                        month_events[day].append(all_holidays[date])
                    else:
                        month_events[day] = [all_holidays[date]]

            if len(month_events) != 0:
                max_item_show = 0
                for day, events in sorted(month_events.items(), key=lambda x: x[0]):
                    if max_item_show < 4:
                        if len(events) > 2:
                            show_more = True
                        
                        event = "; ".join(events[0:2])
                        if len(event) > 17:
                            event = event[:14] + "..."
                            show_more = True
                        
                        if day < 10:
                            day = "0"+str(day)
                        fields[max_item_show].config(text=f"• {day}: {event}")
                        max_item_show += 1
                if show_more:
                    self.events_more.config(text="More on Calendar")
            else:
                self.events_item_1.config(text="• No Events")
        except Exception as e:
            print("Error: update_events(greetingsPage)", str(e))
            self.events_item_1.config(text="• Error**") 
        finally:
            self.after(self.EVENTS_UPDATE_TIMER, self.update_events)

