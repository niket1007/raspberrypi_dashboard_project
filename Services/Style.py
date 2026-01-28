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
        "font": ("Courier", 30, "bold"),
        "fg": RETRO_GREEN,              
        "bg": RETRO_BG                  
    }
    TimeLabelPack: dict = {
        "side": "top", 
        "expand": True, 
        "anchor": "center"
    }
    DateAndGreeting: dict = {
        "font": ("Courier", 12, "bold"),
        "fg": RETRO_GREEN,               
        "bg": RETRO_BG                   
    }
    DateAndGreetingPack: dict = {
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