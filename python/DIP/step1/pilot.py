from racing_car import RacingCar

class Pilot:
    def __init__(self) -> None:
        super().__init__()
        self.__vehicle = RacingCar(100)

    def increase_speed(self):
        self.__vehicle.accelerate()
