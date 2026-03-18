# Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled distance. Add a class initializer that sets the first two of the properties based on parameter values. The current speed and travelled distance of a new car must be automatically set to zero. Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h). Finally, print out all the properties of the new car.

class Car:
    def __init__ (self,registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

new_car = Car ("ABC-123", 142)

print(f"the new car registration number is {new_car.registration_number}, it's maximum speed is {new_car.maximum_speed}, but now is speeding at {new_car.current_speed} km/h and travelled {new_car.travelled_distance} km")