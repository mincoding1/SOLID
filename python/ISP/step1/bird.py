from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self): pass

    @abstractmethod
    def molt(self): pass
