# This exercise continues the previous car race exercise from the last exercise set. Write a Race class that has the following properties: name, distance in kilometers and a list of cars participating in the race. The class has an initializer that receives the name, kilometers, and car list as parameters and sets their values to the corresponding properties in the class. The class has the following methods:
#
# hour_passes, which performs the operations done once per hour in the original exercise: generates a random change of speed for each car and calls their drive method.
# print_status, which prints out the current information of each car as a clear, formatted table.
# race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven the entire distance of the race.
# Write a main program that creates an 8000-kilometer race called Grand Demolition Derby. The new race is given a list of ten cars similarly to the earlier exercise. The main program simulates the progressing of the race by calling the hour_passes in a loop, after which it uses the race_finished method to check if the race has finished. The current status is printed out using the print_status method every ten hours and then once more at the end of the race.

import random
from operator import truediv


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



class Race:
    def __init__(self, name, distance, cars ):
        self.name=name
        self.distance=distance
        self.cars = cars

    def hour_passes (self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)
    def print_status(self):
        for car in self.cars:
            print(f"{car.registration_number} | {car.maximum_speed} km/h | "
                  f"{car.current_speed} km/h | {car.travelled_distance} km")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

#Main

car_list = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    new_car = Car(f"ABC-{i}", max_speed)
    car_list.append(new_car)

grand_derby = Race("Grand Demolition Derby", 8000, car_list)

hours_elapsed = 0
while True:
    grand_derby.hour_passes()
    hours_elapsed += 1


    if grand_derby.race_finished():
        break

    if hours_elapsed % 10 == 0:
        grand_derby.print_status()

print(f"\nFINAL RESULTS at {hours_elapsed} hours:")
grand_derby.print_status()




