from enum import Enum

class Gear(Enum):
    P = 0 #Parking
    R = 1 #Reverse
    N = 2 #Neutral
    D = 3 #Drive

class Vehicle:
    def __init__(self) -> None:
        super().__init__()
        self.__gear = Gear.P

    def get_gear(self):
        return self.__gear

    def change_gear(self, gear: Gear):
        self.__gear = gear

    def get_gear_name(self, gear: Gear) -> str:
        if gear == Gear.P : return "Parking"
        if gear == Gear.R : return "Reverse"
        if gear == Gear.N : return "Neutral"
        if gear == Gear.D : return "Drive"
