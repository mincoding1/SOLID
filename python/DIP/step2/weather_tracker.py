from phone import Phone
from emailer import Emailer

class WeatherTracker:
    def __init__(self) -> None:
        super().__init__()
        self.__current_conditions = ""
        self.__phone = Phone()
        self.__emailer = Emailer()

    def set_current_conditinos(self, weather_description: str) -> None:
        self.__current_conditions = weather_description
        if weather_description == 'rainy':
            alert = self.__phone.generate_weather_alert(weather_description)
            print(alert)
        if weather_description == 'sunny':
            alert = self.__emailer.generate_weather_alert(weather_description)
            print(alert)
