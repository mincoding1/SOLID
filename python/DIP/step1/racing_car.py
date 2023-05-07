class RacingCar:
    def __init__(self, max_fuel) -> None:
        super().__init__()
        self.__max_fuel = max_fuel
        self.__remaining_fuel = max_fuel
        self.__power = 0

    def accelerate(self):
        self.__power += 1
        self.__remaining_fuel -= 1
