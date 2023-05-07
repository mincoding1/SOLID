from vehicle import Vehicle, DrivingMode

class EventHandler:
    def __init__(self, vehicle:Vehicle) -> None:
        super().__init__()
        self.__vehicle = vehicle

    def change_driving_mode(self, driving_mode:DrivingMode):
        if driving_mode == DrivingMode.SPORT:
            self.__vehicle.set_power(500)
            self.__vehicle.set_suspension_height(10)
        elif driving_mode == DrivingMode.COMFORT:
            self.__vehicle.set_power(400)
            self.__vehicle.set_suspension_height(20)
        else:
            self.__vehicle.set_power(400)
            self.__vehicle.set_suspension_height(20)

        # when we need to add another mode (e.g. ECONOMY) 2 classes will change DrivingMode and EventHandler.
