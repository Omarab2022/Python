from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class car(vehicle):
    def drive(self):
        print("you drive a car")

class moto(vehicle):
    def drive(self):
        print("you drive a moto")



car=car()
moto=moto()


car.drive()
moto.drive()

