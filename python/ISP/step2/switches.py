from abc import ABC, abstractmethod

class Switches(ABC):
    @abstractmethod
    def start_engine(self): pass

    @abstractmethod
    def shutdown_engine(self): pass

    @abstractmethod
    def turn_radio_on(self): pass

    @abstractmethod
    def turn_radio_off(self): pass

    @abstractmethod
    def turn_camera_on(self): pass

    @abstractmethod
    def turn_camera_off(self): pass
