class NavigationBarStyle:
    Button: dict = {}
    ScreenInfo: dict = {
        "borderwidth":2, 
        "relief": "sunken", 
        "font": ("Helvetica", 10, "bold"), 
        "anchor": "center"
    }

class QuotePageStyle:
    FramePack: dict = {
        "fill": "both", 
        "expand": True,
        "anchor": "center"
    }
    QuoteLabel: dict = {
        "font": ("Helvetica", 16, "bold", "italic"), 
        "wraplength": 440,
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
        "padx": 20,
        "fill": "both",
        "expand": True
    }
    LastUpdatedLabel: dict = {
        "font": ("Helvetica", 8),
        "text": "Last updated: Never"
    }
    LastUpdatedLabelPack: dict = {
        "side": "bottom", 
        "pady": 5
    }

class GreetingsPageStyle:
    MainFrame: dict = {
        "side": "top", 
        "fill": "both", 
        "expand": True, 
        "padx": 20, 
        "pady": 20
    }
    TimeLabel: dict = {
        "font": ("Helvetica", 55, "bold")
    }
    TimeLabelPack: dict = {
        "side": "top", 
        "expand": True, 
        "anchor": "center"
    }
    DateAndGreeting: dict = {
        "font": ("Helvetica", 18, "bold")
    }
    DateAndGreetingPack: dict = {
        "side": "top", 
        "expand": True, 
        "anchor": "center"
    }

class TodoPageStyle:
    TodoLabel = {
        "text": "Loading todos...", 
        "font": ("Helvetica", 18),
        "justify": "left",
        "wraplength": 400,
        "anchor": "center"
    }
    TodoLabelPack = {
        "side": "top",
        "expand": True, 
        "fill": "both", 
        "padx": 20, 
        "pady": 20
    }

class WeatherPageStyle:
    WeatherLabel = {
        "text": "Loading weather...", 
        "font": ("Helvetica", 18),
        "justify": "left"
    }
    WeatherLabelPack = {
        "side": "top", 
        "pady": 20,
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
        "pady": 5
    }

class CalendarPageStyle:
    MonthLabel = {
        "text": "Loading...", 
        "font": ("Helvetica", 9, "bold")
    }
    MonthLabelPack = {
        "pady": (5, 10)
    }
    CalendarFramePack = {
        "expand": True,
        "fill": "both",
        "padx": 20
    }
    InfoLabel = {
        "text": "Tap a date for info", 
        "font": ("Helvetica", 10),
        "foreground": "gray"
    }
    InfoLabelSmallFont = {
        "font": ("Helvetica", 8)
    }
    InfoLabelPack = {
        "pady": 5
    }
    WeeekDayHeaderLabel = {
        "font": ("Helvetica", 8, "bold")
    }
    WeekDayHeaderLabelPack = {
        "sticky": "nsew", 
        "padx": 20
    }

class MeetingPageStyle:
    MeetingLabel = {
        "text": "Loading todos...", 
        "font": ("Helvetica", 18),
        "justify": "left",
        "wraplength": 400,
        "anchor": "center"
    }
    MeetingLabelPack = {
        "side": "top",
        "expand": True, 
        "fill": "both", 
        "padx": 20, 
        "pady": 20
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
        "borderwidth":2, 
        "relief": "sunken", 
        "font": ("Helvetica", 10, "bold"), 
        "anchor": "center"
    }
    ScreenInfoLabelPack = {
        "side": "left",
        "fill": "x",
        "expand": True,
        "padx": 0,
        "pady": 2,
        "ipady": 5
    }
    ButtonPack = {
        "side": "left",
        "fill": "x",
        "expand": True,
        "padx": 0,
        "pady": 0,
        "ipady": 5
    }