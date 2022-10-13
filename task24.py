
import abc
class Vechicle(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_direction(self):
        pass

class Car(Vechicle):
    def get_direction(self):
        return "Drive Forward"

class Plane(Vechicle):
    def get_direction(self):
        return "Drive Upward"


cdirect = Car()
pdirect = Plane()

print(cdirect.get_direction())
print(pdirect.get_direction())