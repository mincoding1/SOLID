from vehicle import Vehicle

class Drone(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        self.__camera_on = False

    def is_camera_on(self) -> bool:
        return self.__camera_on

    def turn_camera_on(self):
        self.__camera_on = True

    def turn_camera_off(self):
        self.__camera_on = False

    def turn_radio_on(self):
        # nothing to do here
        pass

    def turn_radio_off(self):
        # nothing to do here
        pass

