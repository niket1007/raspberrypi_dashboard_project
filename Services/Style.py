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
    RETRO_GREEN = "#18E310"
    RETRO_BG = "#050505"

    MainFrame: dict = {
        "side": "top", 
        "fill": "both", 
        "expand": True, 
        "padx": 10, 
        "pady": 10
    }
    TimeLabel: dict = {
        "font": ("Courier", 20, "bold"),
        "fg": RETRO_GREEN,              
        "bg": RETRO_BG                  
    }
    TimeLabelPack: dict = {
        "side": "top", 
        "expand": True, 
        "anchor": "center"
    }
    CountLabel: dict = {
        "font": ("Courier", 12, "bold"),
        "fg": RETRO_GREEN,               
        "bg": RETRO_BG  
    }
    DateLabel: dict = {    
        "font": ("Courier", 12, "bold"),
        "fg": RETRO_GREEN,               
        "bg": RETRO_BG               
    }
    DateAndCountPack: dict = {
        "side": "top", 
        "expand": True, 
        "anchor": "center"
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