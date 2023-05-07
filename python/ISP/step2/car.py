from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        self.__radio_on = False

    def is_radio_on(self) -> bool:
        return self.__radio_on

    def turn_radio_on(self):
        self.__radio_on = True

    def turn_radio_off(self):
        self.__radio_on = False

    def turn_camera_on(self):
        # nothing to do here
        pass

    def turn_camera_off(self):
        # nothing to do here
        pass
