import calendar
from datetime import date
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.screenmanager import Screen
import holidays
from datetime import date

class DateLabel(Button):
    is_today = BooleanProperty(False)
    is_holiday = BooleanProperty(False)
    holiday_text = StringProperty('')


class CalendarScreen(Screen):
    def on_pre_enter(self):
        self.populate_calendar()
    
    def date_tapped(self, instance):
        print(f"Tapped on Day: {instance.text}, Holiday: '{instance.holiday_text}'")
        self.ids.holiday_info_label.text = instance.holiday_text

    def populate_calendar(self):
        today = date.today()
        holidays_dict = holidays.country_holidays('IN', years=today.year)
        cal = calendar.monthcalendar(today.year, today.month)
        
        month_label = self.ids.month_label
        date_grid = self.ids.date_grid
        
        date_grid.clear_widgets()
        month_label.text = today.strftime("%B %Y")

        # Populate the grid with date labels
        for week in cal:
            for day in week:
                if day == 0:
                    date_grid.add_widget(Label(text=''))
                else:
                    calc_date = date(today.year, today.month, int(day))
                    
                    is_today_bool = (day == today.day and today.month == date.today().month and today.year == date.today().year)
                    
                    is_holiday_bool = calc_date in holidays_dict
                    holiday_name = holidays_dict.get(calc_date, '')
 
                    color = (0.184, 0.208, 0.259, 1)
                    if is_holiday_bool and is_today_bool:
                        color = (1,0,0,1)
                    elif is_holiday_bool:
                        color = (1,0, 0, 1)
                    elif is_today_bool:
                        color = (1, 1, 1, 1)
                    day_widget = DateLabel(
                        text=str(day), 
                        is_today=is_today_bool,
                        is_holiday=is_holiday_bool,
                        holiday_text=holiday_name,
                        font_name='Roboto-Regular',
                        color=color
                    )
                    day_widget.bind(on_release=self.date_tapped)
                    date_grid.add_widget(day_widget)