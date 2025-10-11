import calendar
from datetime import date
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, StringProperty
from CustomScreen.customScreen import CustomScreen
import holidays
from datetime import date
from Logger.Logger import log
from Static.Messages.messages import (
    CALENDAR_DATE_TAPPED, CALENDAR_ON_PRE_ENTER_EVENT,
    CALENDAR_DATA_UDPATE, CALENDAR_HOLIDAY_DATA)
from Storage.Cache import Cache

class DateLabel(Button):
    is_today = BooleanProperty(False)
    is_holiday = BooleanProperty(False)
    is_user_event = BooleanProperty(False)
    holiday_text = StringProperty('')
    user_event_text = StringProperty('')

class CalendarScreen(CustomScreen):
    cache = Cache()

    def on_pre_enter(self):
        log.debug(CALENDAR_ON_PRE_ENTER_EVENT)
        self.populate_calendar()
    
    def date_tapped(self, instance):
        log.debug(CALENDAR_DATE_TAPPED.format(instance.text, instance.holiday_text, instance.user_event_text))
        text = ""
        if instance.is_holiday:
            text += instance.holiday_text
        if instance.is_user_event:
            if len(text) > 0:
                text += "; "
            text += instance.user_event_text
        self.ids.holiday_info_label.text = text

    def populate_calendar(self):
        log.debug(CALENDAR_DATA_UDPATE)
        today = date.today()
        year, month = today.year, today.month
        holidays_dict = holidays.country_holidays('IN', years=year)
        log.debug(CALENDAR_HOLIDAY_DATA.format(str(holidays_dict)))

        cal = calendar.monthcalendar(year, month)
        
        month_label = self.ids.month_label
        date_grid = self.ids.date_grid
        
        date_grid.clear_widgets()
        month_label.text = today.strftime("%B %Y")

        user_monthly_events = self.cache.get_user_monthly_events(month_label.text)

        # Populate the grid with date labels
        for week in cal:
            for day in week:
                if day == 0:
                    date_grid.add_widget(Label(text=''))
                else:
                    is_user_event = False
                    user_event_text = ""
                    if user_monthly_events is not None and str(day) in user_monthly_events[0]:
                        is_user_event = True
                        user_event_text = user_monthly_events[0][str(day)]

                    calc_date = date(year, month, day)
                    
                    is_today_bool = (day == today.day and month == date.today().month and year == date.today().year)
                    
                    is_holiday_bool = calc_date in holidays_dict
                    holiday_name = holidays_dict.get(calc_date, '')

                    color = (0.184, 0.208, 0.259, 1)
                    if is_holiday_bool and is_today_bool and is_user_event:
                        color = (1,0,0,1)
                    elif is_holiday_bool or is_user_event:
                        color = (1,0, 0, 1)
                    elif is_today_bool:
                        color = (1, 1, 1, 1)
                    
                    day_widget = DateLabel(
                        text=str(day), 
                        is_today=is_today_bool,
                        is_holiday=is_holiday_bool,
                        is_user_event=is_user_event,
                        user_event_text=user_event_text,
                        holiday_text=holiday_name,
                        font_name='Roboto-Regular',
                        color=color
                    )
                    day_widget.bind(on_release=self.date_tapped)
                    date_grid.add_widget(day_widget)