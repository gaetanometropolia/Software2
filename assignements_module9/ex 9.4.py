# Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of the main program, create a list that consists of 10 car objects created using a loop. The maximum speed of each new car is a random value between 100 km/h and 200 km/h. The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins. One per every hour of the race, the following operations are performed:
#
# The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is done using the accerelate method.
# Each car is made to drive for one hour. This is done with the drive method.
# The race continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties of each car are printed out formatted into a clear table.


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

cars=[]

for i in range (1,11):
    new_car= f"ABC-{i}"
    max_v = random.randint(100,200)
    cars.append(Car(new_car, max_v))



