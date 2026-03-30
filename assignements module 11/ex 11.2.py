# Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar. Electric cars have the capacity of the battery in kilowatt-hours as their property. Gasoline cars have the volume of the tank in liters as their property. Write initializers for the subclasses. For example, the initializer of electric cars receives the registration number, maximum speed and battery capacity as its parameter. It calls the initializer of the base class to set the first two properties and then sets its capacity. Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds for both cars, make them drive for three hours and print out the values of their kilometer counters.

import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive (self, hours):
        distance_covered = self.current_speed * hours
        self.travelled_distance += distance_covered


class ElectricCar(Car):
    def __init__(self,registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity=battery_capacity


class GasolineCar(Car):
    def __init__(self,registration_number, maximum_speed,tank):
        super().__init__(registration_number,maximum_speed)
        self.tank=tank

electric_car= ElectricCar("ABC-15", 180, 52.5)
gasoline_car=GasolineCar("ACD-123", 165, 32.3)

electric_car.accelerate(100)
gasoline_car.accelerate(90)

electric_car.drive(3)
gasoline_car.drive(3)

print(f"Electric car {electric_car.registration_number} has been driving for {electric_car.travelled_distance} km,  while gasoline car {gasoline_car.registration_number} has been driving for {gasoline_car.travelled_distance} km")