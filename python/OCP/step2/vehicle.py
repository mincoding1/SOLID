from enum import Enum

class DrivingMode(Enum):
    SPORT = 0
    COMFORT = 1

class Vehicle:
    def __init__(self) -> None:
        super().__init__()
        self.__power = 0
        self.__suspension_height = 0

    def get_power(self):
        return self.__power

    def get_suspension_height(self):
        return self.__suspension_height

    def set_power(self, power):
        self.__power = power

    def set_suspension_height(self, suspension_height):
        self.__suspension_height = suspension_height
