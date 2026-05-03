class QuotePageStyle:
    RETRO_GREEN = "#18E310"
    RETRO_BG = "#050505"

    FramePack: dict = {
        "fill": "both", 
        "expand": True,
        "anchor": "center"
    }
    QuoteLabel: dict = {
        "font": ("Courier", 12, "bold", "italic"),
        "fg": RETRO_GREEN,
        "bg": RETRO_BG,
        "wraplength": 250,
        "anchor": "center",
        "text": "Loading quote..."
    }
    QuoteLabelStateColor: dict = {
        "error_color": "#FF0000",                  
        "success_color": "#18E310"                
    }
    QuoteLabelPack: dict = {
        "side": "top", 
        "pady": (0,0), 
        "padx": 10,
        "fill": "both",
        "expand": True
    }
    LastUpdatedLabel: dict = {
        "font": ("Courier", 10),                    
        "fg": RETRO_GREEN,                          
        "bg": RETRO_BG,                            
        "text": "Last updated: Never"
    }
    LastUpdatedLabelPack: dict = {
        "side": "bottom", 
        "pady": 3
    }

class GreetingsPageStyle:
    FRAME_BG_ONE = "#001100"
    FRAME_BG_TWO = "#000000"
    HIGHLIGHT_COLOR = "#003300"
    LABEL_FG = "#00CC33"

    BoldFont11 = {"family":"Helvetica", "size":11, "weight":"bold"}
    NormalFont9 = {"family":"Helvetica", "size":9, "weight":"normal"}
    BoldFont9 = {"family":"Helvetica", "size":9, "weight":"bold"}
    UnderlineBold9 = {"family":"Helvetica", "size":9, "weight":"bold", "underline":True}

    FrameOne = {
        "bg": FRAME_BG_ONE, 
        "relief":"solid",
        "highlightcolor":HIGHLIGHT_COLOR, 
        "highlightthickness":1, 
        "highlightbackground": HIGHLIGHT_COLOR
    }

    FrameTwo = {
        "bg": FRAME_BG_TWO, 
        "relief":"solid",
        "highlightcolor":HIGHLIGHT_COLOR, 
        "highlightthickness":1, 
        "highlightbackground": HIGHLIGHT_COLOR
    }

    LabelWithoutText = {
        "background":FRAME_BG_ONE,
        "foreground":LABEL_FG,
    }

    TopFrame1Place = {
        "x":0, 
        "y":0,
        "height": 50,
        "width": 145
    }
    TopFrame2Place = {
        "x":145, 
        "y":0,
        "height": 50,
        "width": 175
    }
    MidFrame1Place = {
        "x":0, 
        "y":50,
        "height": 105,
        "width": 145
    }
    MidFrame2Place = {
        "x":145, 
        "y":50,
        "height": 105,
        "width": 175
    }
    SecondLastFramePlace = {
        "x":0, 
        "y":148,
        "height": 62,
        "width": 320
    }
    LastFrame1Place = {
        "x":0, 
        "y":209,
        "height": 31,
        "width": 60
    }
    LastFrame2Place = {
        "x":60, 
        "y":209,
        "height": 31,
        "width": 260
    }

    TimeLablePlace = {
        "x":5, 
        "y":8,
        "height": 18,
        "width": 135
    }
    DateLabelPlace = {
        "x":5, 
        "y":27,
        "height": 18,
        "width": 135
    }
    TempLabelPlace = {
        "x":10, 
        "y":8
    }
    TempLocLabelPlace = {
        "x":10, 
        "y":27,
        "height": 18,
        "width": 167
    }

    TodoLabelPlace = {
        "x":1, 
        "y":1,
        "height": 18,
        "width": 50
    }
    TodoItemsPlace = {
        "x":5, 
        "y":22
    }
    TodoMorePlace = {
        "x":90, 
        "y":75
    }

    MeetingsLabelPlace = {
        "x":1, 
        "y":1
    }
    MeetingsItemsPlace = {
        "x":5, 
        "y":22
    }
    MeetingsMorePlace = {
        "x":120, 
        "y":75
    }

    EventLabelPlace ={
        "x":1, 
        "y":1
    }
    EventsItem1Place = {
        "x":1, 
        "y":20
    }
    EventsItem2Place = {
        "x":1, 
        "y":40
    }
    EventsItem3Place = {
        "x":165, 
        "y":5
    }
    EventsItem4Place = {
        "x":165, 
        "y":20
    }
    EventsMorePlace = {
        "x":210, 
        "y":40
    }

    QuoteLabelPlace = {
        "x":5, 
        "y":5
    }
    QuoteTextPlace = {
        "x":5, 
        "y":5
    }


class TodoPageStyle:
    RETRO_GREEN = "#18E310"
    RETRO_BG = "#050505"

    TodoLabel = {
        "text": "Loading todos...", 
        "font": ("Courier", 12),              
        "fg": RETRO_GREEN,                     
        "bg": RETRO_BG,                        
        "justify": "left",
        "wraplength": 250,
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
    RETRO_GREEN = "#18E310"
    RETRO_BG = "#050505"

    WeatherLabel = {
        "text": "Loading weather...", 
        "font": ("Courier", 13),           
        "fg": RETRO_GREEN,                    
        "bg": RETRO_BG,                        
        "justify": "left"
    }
    WeatherLabelPack = {
        "side": "top", 
        "pady": 10,
        "expand": True,
        "fill": "both"
    }
    WeatherLabelStateColor: dict = {
        "error_color": "#FF0000",           
        "success_color": "#18E310"            
    }
    LastUpdatedLabel = {
        "text": "Last updated: Never",
        "font": ("Courier", 10),            
        "fg": RETRO_GREEN,                    
        "bg": RETRO_BG                        
    }
    LastUpdatedLabelPack = {
        "side": "bottom", 
        "pady": 3
    }

class CalendarPageStyle:
    RETRO_GREEN = "#18E310"
    RETRO_BG = "#050505"

    MonthLabel = {
        "text": "Loading...", 
        "font": ("Courier", 10, "bold"),     
        "fg": RETRO_GREEN,                      
        "bg": RETRO_BG                         
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
        "text": "SELECT DATE FOR INFO",        
        "font": ("Courier", 10),                
        "fg": RETRO_GREEN,                      
        "bg": RETRO_BG                          
    }
    InfoLabelSmallFont = {
        "font": ("Courier", 8),                
        "fg": RETRO_GREEN,
        "bg": RETRO_BG
    }
    InfoLabelPack = {
        "pady": 0
    }
    WeekDayHeaderLabel = {
        "font": ("Courier", 10, "bold"),
        "fg": RETRO_GREEN,                     
        "bg": RETRO_BG                          
    }
    WeekDayHeaderLabelPack = {
        "sticky": "nsew", 
        "padx": 5
    }

class MeetingPageStyle:
    RETRO_GREEN = "#18E310"
    RETRO_BG = "#050505"

    MeetingLabel = {
        "text": "Loading meetings...", 
        "font": ("Courier", 12),              
        "fg": RETRO_GREEN,                    
        "bg": RETRO_BG,                        
        "justify": "left",
        "wraplength": 250,
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
    RETRO_BG = "#050505"
    RETRO_GREEN = "#18E310"
    
    Title = "Dashboard"
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
        "font": ("Courier", 11, "bold"), 
        "anchor": "center",
        "fg": "#18E310",
        "bg": "#050505"
    }

    ScreenInfoLabelPack = {
        "side": "left",
        "fill": "x",
        "expand": True,
        "padx": 2,
        "pady": 2,
        "ipady": 3
    }

    ButtonStyle = {
        "font": ("Courier", 9, "bold"),
        "bg": "#050505",
        "fg": "#18E310",
        "activebackground": "#18E310",
        "activeforeground": "#050505",
        "relief": "flat",
        "highlightthickness": 1,
        "highlightbackground": "#18E310",
        "bd": 0
    }

    ButtonPack = {
        "side": "left",
        "fill": "x",
        "expand": True,
        "padx": 1,
        "pady": 2,
        "ipady": 1
    }

class SysteminfoStyle:
    RETRO_BG = "#050505"
    RETRO_GREEN = "#18E310"

    TopFramePack = {
        "side": "top", 
        "expand": True, 
        "fill": "both"
    }

    BottomFramePack = {
        "side": "top", 
        "expand": True, 
        "fill": "both"
    }

    CPULabel = {
        "font": ("Courier", 12, "bold"), 
        "text": "CPU Status:\nXX%", 
        "bg": RETRO_BG,
        "fg": RETRO_GREEN
    }

    CPULabelPack = {
        "side": "left", 
        "expand": True, 
        "fill": "both"
    }

    MemoryLabel = {
        "font": ("Courier", 12, "bold"), 
        "text": "Memory Status:\nXX%", 
        "bg": RETRO_BG,
        "fg": RETRO_GREEN
    }

    MemoryLabelPack = {
        "side": "left", 
        "expand": True, 
        "fill": "both"
    }

    VoltageLabel = {
        "font": ("Courier", 12, "bold"), 
        "text": "Voltage Status:\nActive/Issue", 
        "bg": RETRO_BG,
        "fg": RETRO_GREEN
    }

    VoltageLabelPack = {
        "side": "left", 
        "expand": True, 
        "fill": "both"
    }

    TempLabel = {
        "font": ("Courier", 12, "bold"), 
        "text": "Temp Status:\nXX.XC", 
        "bg": RETRO_BG,
        "fg": RETRO_GREEN
    }

    TempLabelPack = {
        "side": "left", 
        "expand": True, 
        "fill": "both"
    }

class NotificationStyle:
    RETRO_BG = "#050505"
    RETRO_GREEN = "#18E310"

    TAG_COLORS = {
        "NOTIF":   {"bg": "#58a6ff", "fg": "#050505"},
        "INCALL":  {"bg": "#f85149", "fg": "#ffffff"},
        "OUTCALL": {"bg": "#f85149", "fg": "#ffffff"},
        "BATT":    {"bg": "#f5a623", "fg": "#050505"},
        "DEFAULT": {"bg": "#18E310", "fg": "#050505"},
    }
    FramePlace = {
        "x": 0, "y": 0,
        "relwidth": 1, "relheight": 1
    }
    CardBorder = {
        "bg": "#0a0a0a",
        "highlightthickness": 1,
        "highlightbackground": "#18E310",
        "relief": "flat",
        "bd": 0
    }
    TagLabel = {
        "font": ("Courier", 8, "bold"),
        "padx": 5, "pady": 1,
        "relief": "flat"
    }
    TitleLabel = {
        "font": ("Courier", 13, "bold"),
        "fg": "#18E310",
        "bg": "#0a0a0a",
        "anchor": "w"
    }
    BodyLabel = {
        "font": ("Courier", 11),
        "fg": "#18E310",
        "bg": "#0a0a0a",
        "justify": "left",
        "wraplength": 280,
        "anchor": "w"
    }
    TimeLabel = {
        "font": ("Courier", 9),
        "fg": "#18E310",
        "bg": "#0a0a0a",
        "anchor": "e"
    }