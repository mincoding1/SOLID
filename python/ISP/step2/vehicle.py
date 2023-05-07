from switches import Switches

class Vehicle(Switches):
    def __init__(self) -> None:
        super().__init__()
        self.__engin_running = False

    def is_engin_running(self) -> bool:
        return self.__engin_running

    def start_engine(self):
        self.__engin_running = True

    def shutdown_engine(self):
        self.__engin_running = False

