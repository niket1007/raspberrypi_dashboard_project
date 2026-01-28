# ============================================
# CYBERPUNK COLOR PALETTE
# ============================================
CYBER_CYAN = "#00f2ff"          # Neon cyan (primary)
CYBER_MAGENTA = "#ff00ff"       # Neon magenta (accent)
CYBER_PURPLE = "#8b00ff"        # Neon purple
CYBER_PINK = "#ff0080"          # Hot pink
CYBER_DARK_BG = "#0a0a0a"       # Deep black background
CYBER_DARKER = "#050505"        # Darker black
CYBER_PURPLE_BG = "#1a0030"     # Dark purple background
CYBER_GRID = "#1a1a2e"          # Grid background
CYBER_TEXT_DIM = "#a0a0ff"      # Dimmed text
CYBER_WHITE = "#ffffff"         # Pure white
CYBER_ERROR = "#ff0040"         # Error red with neon
CYBER_SUCCESS = CYBER_CYAN      # Success color

# ============================================
# FONTS (Cyberpunk/Futuristic)
# ============================================
FONT_DISPLAY = "Orbitron"       # For time and headers
FONT_BODY = "Courier New"       # For body text (monospace)
FONT_ALT = "Consolas"           # Alternative monospace

# ============================================
# NAVIGATION BAR STYLE
# ============================================
class NavigationBarStyle:
    Button: dict = {
        "bg": CYBER_DARKER,
        "fg": CYBER_CYAN,
        "activebackground": CYBER_PURPLE_BG,
        "activeforeground": CYBER_MAGENTA,
        "font": (FONT_BODY, 9, "bold"),
        "relief": "flat",
        "borderwidth": 0,
        "cursor": "none"
    }
    
    ScreenInfo: dict = {
        "bg": CYBER_DARKER,
        "fg": CYBER_MAGENTA,
        "borderwidth": 0,
        "relief": "flat",
        "font": (FONT_DISPLAY, 10, "bold"),
        "anchor": "center"
    }

# ============================================
# QUOTE PAGE STYLE
# ============================================
class QuotePageStyle:
    FramePack: dict = {
        "fill": "both",
        "expand": True,
        "anchor": "center"
    }
    
    QuoteLabel: dict = {
        "bg": CYBER_DARK_BG,
        "fg": CYBER_CYAN,
        "font": (FONT_BODY, 11, "bold", "italic"),
        "wraplength": 250,
        "anchor": "center",
        "text": "⚡ Loading quote...",
        "justify": "center"
    }
    
    QuoteLabelStateColor: dict = {
        "error_color": CYBER_ERROR,
        "success_color": CYBER_CYAN
    }
    
    QuoteLabelPack: dict = {
        "side": "top",
        "pady": (10, 5),
        "padx": 10,
        "fill": "both",
        "expand": True
    }
    
    LastUpdatedLabel: dict = {
        "bg": CYBER_DARK_BG,
        "fg": CYBER_TEXT_DIM,
        "font": (FONT_BODY, 7),
        "text": "LAST UPDATE: NEVER"
    }
    
    LastUpdatedLabelPack: dict = {
        "side": "bottom",
        "pady": 3
    }

# ============================================
# GREETINGS PAGE STYLE
# ============================================
class GreetingsPageStyle:
    MainFrame: dict = {
        "background": CYBER_DARK_BG
    }

    MainFramePack: dict = {
        "side": "top",
        "fill": "both",
        "expand": True,
        "padx": 10,
        "pady": 10
    }
    
    TimeLabel: dict = {
        "bg": CYBER_DARK_BG,
        "fg": CYBER_CYAN,
        "font": (FONT_DISPLAY, 32, "bold"),
        "text": "00:00:00"
    }
    
    TimeLabelPack: dict = {
        "side": "top",
        "expand": True,
        "anchor": "center",
        "pady": (10, 5)
    }
    
    DateAndGreeting: dict = {
        "bg": CYBER_DARK_BG,
        "fg": CYBER_MAGENTA,
        "font": (FONT_BODY, 11, "bold")
    }
    
    DateAndGreetingPack: dict = {
        "side": "top",
        "expand": True,
        "anchor": "center",
        "pady": 2
    }

# ============================================
# TODO PAGE STYLE
# ============================================
class TodoPageStyle:
    TodoLabel = {
        "bg": CYBER_DARK_BG,
        "fg": CYBER_CYAN,
        "text": "⚡ LOADING TODOS...",
        "font": (FONT_BODY, 11),
        "justify": "left",
        "wraplength": 250,
        "anchor": "nw"
    }
    
    TodoLabelPack = {
        "side": "top",
        "expand": True,
        "fill": "both",
        "padx": 15,
        "pady": 15
    }

# ============================================
# WEATHER PAGE STYLE
# ============================================
class WeatherPageStyle:
    WeatherLabel = {
        "bg": CYBER_DARK_BG,
        "fg": CYBER_CYAN,
        "text": "🌐 LOADING WEATHER...",
        "font": (FONT_BODY, 13, "bold"),
        "justify": "left"
    }
    
    WeatherLabelPack = {
        "side": "top",
        "pady": 15,
        "padx": 10,
        "expand": True,
        "fill": "both"
    }
    
    WeatherLabelStateColor: dict = {
        "error_color": CYBER_ERROR,
        "success_color": CYBER_CYAN
    }
    
    LastUpdatedLabel = {
        "bg": CYBER_DARK_BG,
        "fg": CYBER_TEXT_DIM,
        "text": "LAST UPDATE: NEVER",
        "font": (FONT_BODY, 7)
    }
    
    LastUpdatedLabelPack = {
        "side": "bottom",
        "pady": 3
    }

# ============================================
# CALENDAR PAGE STYLE
# ============================================
class CalendarPageStyle:
    MonthLabel = {
        "bg": CYBER_DARK_BG,
        "fg": CYBER_MAGENTA,
        "text": "LOADING...",
        "font": (FONT_DISPLAY, 10, "bold")
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
        "bg": CYBER_DARK_BG,
        "fg": CYBER_TEXT_DIM,
        "text": "▶ TAP A DATE",
        "font": (FONT_BODY, 9, "bold"),
        "foreground": CYBER_TEXT_DIM
    }
    
    InfoLabelSmallFont = {
        "font": (FONT_BODY, 7, "bold")
    }
    
    InfoLabelPack = {
        "pady": 2
    }
    
    WeekDayHeaderLabel = {
        "bg": CYBER_DARKER,
        "fg": CYBER_MAGENTA,
        "font": (FONT_DISPLAY, 9, "bold")
    }
    
    WeekDayHeaderLabelPack = {
        "sticky": "nsew",
        "padx": 2,
        "pady": 2
    }

# ============================================
# MEETING PAGE STYLE
# ============================================
class MeetingPageStyle:
    MeetingLabel = {
        "bg": CYBER_DARK_BG,
        "fg": CYBER_CYAN,
        "text": "📡 LOADING MEETINGS...",
        "font": (FONT_BODY, 11),
        "justify": "left",
        "wraplength": 250,
        "anchor": "nw"
    }
    
    MeetingLabelPack = {
        "side": "top",
        "expand": True,
        "fill": "both",
        "padx": 15,
        "pady": 15
    }

# ============================================
# MAIN PAGE STYLE
# ============================================
class MainPageStyle:
    Title = "RASPBERRY PI DASHBOARD // CYBER"
    Geometry = "320x240"
    
    # Main window background color
    BackgroundColor = CYBER_DARK_BG
    
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
        "bg": CYBER_DARKER,
        "fg": CYBER_MAGENTA,
        "borderwidth": 0,
        "relief": "flat",
        "font": (FONT_DISPLAY, 10, "bold"),
        "anchor": "center"
    }
    
    ScreenInfoLabelPack = {
        "side": "left",
        "fill": "x",
        "expand": True,
        "padx": 0,
        "pady": 0,
        "ipady": 5
    }
    
    ButtonPack = {
        "side": "left",
        "fill": "x",
        "expand": True,
        "padx": 0,
        "pady": 0,
        "ipady": 3
    }