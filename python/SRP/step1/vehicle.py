class Vehicle:
    def __init__(self, max_fuel: int) -> None:
        super().__init__()
        self.max_fuel = max_fuel
        self.remaining_fuel = max_fuel

    # this is not a car's responsibility.
    def re_fuel(self):
        self.remaining_fuel = self.max_fuel

    def get_max_fuel(self):
        return self.max_fuel

    def get_remaining_fuel(self):
        return self.remaining_fuel

    def set_remaining_fuel(self, remaining_fuel: int):
        self.remaining_fuel = remaining_fuel

    def accelerate(self):
        self.remaining_fuel -= 1
