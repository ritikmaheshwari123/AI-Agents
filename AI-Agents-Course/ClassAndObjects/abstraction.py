from abc import ABC, abstractmethod

class Vehicle(ABC):
    def drive(self):
        print("Driving the vehicle")

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Starting the car engine")

    def stop_engine(self):
        print("Stopping the car engine")

def operate_vehicle(vehicle):
    vehicle.drive()
    vehicle.start_engine()
    vehicle

car = Car()
operate_vehicle(car)  # This will print "Starting the car engine" 