####### Common #######
UPDATE_CACHE_DATA = "Updating cache data with api response payload"
####### Common #######

####### main.py #######
BUILD_FUNC_LOG_MESSAGE = "Loading main.kv file"
APP_ON_START_LOG_MESSAGE = "Adding screens to screen manager"
APP_ON_TOUCH_DOWN_EVENT = "on_touch_down event triggered"
APP_ON_TOUCH_UP_EVENT = "on_touch_up event triggered"
####### main.py ####### 

####### ScreenSaverScreen.py #######
SCREENSAVER_ON_TOUCH_UP_EVENT = "on_touch_up_event triggered, moving to {0} screen"
####### ScreenSaverScreen.py #######

####### WeatherScreen.py #######
WEATHER_ON_ENTER_EVENT = "on_enter event triggered"
WEATHER_SET_API_JOB = "Setting job for making weather api call in every {} seconds"
WEATHER_ON_LEAVE_EVENT = "on_leave event triggered"
WEATHER_UNSET_API_JOB = "Removing the weather api call job"
WEATHER_DEFAULT_DATA = "Due to some error, setting the default weather data"
WEATHER_UPDATE_SCREEN_DATA = "Updating screen data"
WEATHER_API_CALL_INITIATE = "Cahce data is not available, making weather api call"
WEATHER_API_CALL_DATA = "Calling weather api for fetching weather of lattitude {} and longitude {}"
WEATHER_API_URL = "Weather API URL is {}"
WEATHER_API_CALL_STATUS = "Weather api call made, status code is {}"
WEATHER_API_RESPONSE_DATA = "Weather API response payload is {}"
####### WeatherScreen.py #######

####### Cache.py #######
CACHE_NEW_MAGIC_METHOD = "Cache.__new__ called"
CACHE_CREATE_INSTANCE = "Create Cache instance"
CACHE_REDIS_INITIATION = "Initiating Redis connection"
CACHE_SET_KEY_VALUE = "Setting weather api data in redis key {} with ttl is {} and data is {}"
CACHE_GET_KEY_VALUE = "Fetching cache data from {} and data is {}"
CACHE_DEFAULT_DATA = "Using config:screens default data"
####### Cache.py #######

####### GreetingsScreen.py #######
GREETINGS_ON_ENTER_EVENT = "on_enter event triggered"
GREETINGS_TEXT_UDPATE = "Hour is {} and greeting text will be {}"
####### GreetingsScreen.py #######

####### CalendarScreen.py #######
CALENDAR_ON_PRE_ENTER_EVENT = "on_pre_enter event triggered"
CALENDAR_DATE_TAPPED = "Tapped on Day: {}, Holiday: '{}' or User Event: '{}'"
CALENDAR_DATA_UDPATE = "creating calendar data"
CALENDAR_HOLIDAY_DATA = "Holidays dictionary is {}"
####### CalendarScreen.py #######

####### CustomScreen.py #######
CUSTOM_SCREEN_ON_ENTER_EVENT = "on_enter event triggered, setting reset screen event for screen {} having inactive timeout as {}"
CUSTOM_SCREEN_ON_LEAVE_EVENT = "Canceling the reset event for screen {} as screen is changed"
CUSTOM_SCREEN_ON_TOUCH_UP_EVENT = "Reset the inactive timeout as screen {} is now active"
CUSTOM_SCREEN_RESET_FUNCTION = "Reset Screen to ScreenSaver and Current Screen is {}"
####### CustomScreen.py #######

####### QuoteScreen.py #######
QUOTE_ON_ENTER_EVENT = "on_enter event triggered"
QUOTE_SET_API_JOB = "Setting job for making quote api call in every {} seconds"
QUOTE_ON_LEAVE_EVENT = "on_leave event triggered"
QUOTE_UNSET_API_JOB = "Removing the quote api call job"
QUOTE_DEFAULT_DATA = "Due to some error, setting the default quote data"
QUOTE_API_URL = "Quote API URL is {}"
QUOTE_API_CALL_STATUS = "Quote api call made, status code is {}"
QUOTE_UPDATE_SCREEN_DATA = "Updating screen data"
QUOTE_API_CALL_INITIATE = "Cahce data is not available, making quote api call"
QUOTE_API_RESPONSE_DATA = "Quote API response payload is {}"
####### QuoteScreen.py #######

####### InternetSpeedTestScreen.py #######
IST_ON_ENTER_EVENT = "on_enter event triggered"
IST_WIFI_NAME_INITIATE = "starting get wifi name process"
IST_WINDOWS_PLATFORM = "Windows Platform"
IST_LINUX_PLATFORM = "Linux Platform"
IST_INITIATE_SPEED_TEST = "Starting the speed test"
IST_COMMAND_OUTPUT = "speedtest-cli command output is {}"
IST_UPDATE_VALUES_ON_SCREEN = "setting values on screen"
####### InternetSpeedTestScreen.py #######
