# Abstraction is hiding internal details and showing only necessary features

from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def final(self):
        pass

class plane(vehicle):
    def final(self):
        print("wELCOME TO INDIGO")

class car(vehicle):
    def final(self):
        print("I will buy defender one day")
p = plane()
c = car()
p.final()
c.final()