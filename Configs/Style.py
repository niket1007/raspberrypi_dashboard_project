class Style:
    font = "Helvetica"
    size18 = "18"

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
        "anchor": "center"
    }
    QuoteLabelStateColor: dict = {
        "error_color": "red",
        "success_color": "black"
    }
    QuoteLabelPack: dict = {
        "side": "top", 
        "pady": (0, 0), 
        "padx": 20
    }
    LastUpdatedLabel: dict = {
        "font": ("Helvetica", 8)
    }
    LastUpdatedLabelPack: dict = {
        "side": "bottom", 
        "pady": 5
    }
    CharacterLabel: dict = {
        "font": ("Helvetica", 12),
        "anchor": "center"
    }
    CharacterLabelPack: dict = {
        "side": "top", 
        "pady": (0, 20), 
        "padx": 20
    }

class GreetingsPageStyle:
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

