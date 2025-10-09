class Cache:
    weather_data = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Cache, cls).__new__(cls)
        return cls.instance
    
    def set_weather_data(self, data: dict|None) -> None:
        self.weather_data = data

    def get_weather_data(self) -> dict|None:
        return self.weather_data
    
    
    