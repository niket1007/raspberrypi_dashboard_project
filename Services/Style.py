class NavigationBarStyle:
    Button: dict = {}
    ScreenInfo: dict = {
        "borderwidth":1, 
        "relief": "sunken", 
        "font": ("Helvetica", 8, "bold"), 
        "anchor": "center"
    }

class QuotePageStyle:
    FramePack: dict = {
        "fill": "both", 
        "expand": True,
        "anchor": "center"
    }
    QuoteLabel: dict = {
        "font": ("Helvetica", 10, "bold", "italic"), 
        "wraplength": 300,
        "anchor": "center",
        "text": "Loading quote..."
    }
    QuoteLabelStateColor: dict = {
        "error_color": "red",
        "success_color": "black"
    }
    QuoteLabelPack: dict = {
        "side": "top", 
        "pady": (0,0), 
        "padx": 10,
        "fill": "both",
        "expand": True
    }
    LastUpdatedLabel: dict = {
        "font": ("Helvetica", 8),
        "text": "Last updated: Never"
    }
    LastUpdatedLabelPack: dict = {
        "side": "bottom", 
        "pady": 3
    }

class GreetingsPageStyle:
    MainFrame: dict = {
        "side": "top", 
        "fill": "both", 
        "expand": True, 
        "padx": 10, 
        "pady": 10
    }
    TimeLabel: dict = {
        "font": ("Helvetica", 30, "bold")
    }
    TimeLabelPack: dict = {
        "side": "top", 
        "expand": True, 
        "anchor": "center"
    }
    DateAndGreeting: dict = {
        "font": ("Helvetica", 15, "bold")
    }
    DateAndGreetingPack: dict = {
        "side": "top", 
        "expand": True, 
        "anchor": "center"
    }

class TodoPageStyle:
    TodoLabel = {
        "text": "Loading todos...", 
        "font": ("Helvetica", 9),
        "justify": "left",
        "wraplength": 300,
        "anchor": "center"
    }
    TodoLabelPack = {
        "side": "top",
        "expand": True, 
        "fill": "both", 
        "padx": 10, 
        "pady": 10
    }

class WeatherPageStyle:
    WeatherLabel = {
        "text": "Loading weather...", 
        "font": ("Helvetica", 15),
        "justify": "left"
    }
    WeatherLabelPack = {
        "side": "top", 
        "pady": 10,
        "expand": True,
        "fill": "both"
    }
    WeatherLabelStateColor: dict = {
        "error_color": "red",
        "success_color": "black"
    }
    LastUpdatedLabel = {
        "text": "Last updated: Never",
        "font": ("Helvetica", 8)
    }
    LastUpdatedLabelPack = {
        "side": "bottom", 
        "pady": 3
    }

class CalendarPageStyle:
    MonthLabel = {
        "text": "Loading...", 
        "font": ("Helvetica", 8, "bold")
    }
    MonthLabelPack = {
        "pady": (3, 5)
    }
    CalendarFramePack = {
        "expand": True,
        "fill": "both",
        "padx": 5
    }
    InfoLabel = {
        "text": "Tap a date for info", 
        "font": ("Helvetica", 8),
        "foreground": "gray"
    }
    InfoLabelSmallFont = {
        "font": ("Helvetica", 8)
    }
    InfoLabelPack = {
        "pady": 0
    }
    WeekDayHeaderLabel = {
        "font": ("Helvetica", 10, "bold")
    }
    WeekDayHeaderLabelPack = {
        "sticky": "nsew", 
        "padx": 5
    }

class MeetingPageStyle:
    MeetingLabel = {
        "text": "Loading meetings...", 
        "font": ("Helvetica", 9),
        "justify": "left",
        "wraplength": 300,
        "anchor": "center"
    }
    MeetingLabelPack = {
        "side": "top",
        "expand": True, 
        "fill": "both", 
        "padx": 10, 
        "pady": 10
    }

class MainPageStyle:
    Title = "Raspberry Pi Dashboard"
    Geometry = "320x240"
    NavFramePack = {
        "side": "bottom", 
        "fill": "x"
    }
    MainContainerPack = {
        "side": "top",
        "fill": "both",
        "expand": True
    }
    EachPageFrameGrid = {
        "row": 0,
        "column": 0,
        "sticky": "nsew"
    }
    ScreenInfoLabel = {
        "borderwidth":1, 
        "relief": "sunken", 
        "font": ("Helvetica", 10, "bold"), 
        "anchor": "center"
    }
    ScreenInfoLabelPack = {
        "side": "left",
        "fill": "x",
        "expand": True,
        "padx": 0,
        "pady": 1,
        "ipady": 3
    }
    ButtonPack = {
        "side": "left",
        "fill": "x",
        "expand": True,
        "padx": 0,
        "pady": 0,
        "ipady": 1
    }