# Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators to the bottom floor. Continue the main program by causing a fire alarm in your building.

class Elevator:
    def __init__(self, bottom_floor , top_floor ):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print (f"elevator is now at {self.current_floor}")


    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"elevator is now at {self.current_floor}")


    def go_to_floor (self, selected_floor) :
        while self.current_floor< selected_floor:
            self.floor_up()

        while self.current_floor > selected_floor:
            self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(num_elevators):
            new_elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(new_elevator)

    def run_elevator(self, elevator_number, destination_floor):

        selected_elevator = self.elevators[elevator_number - 1]
        selected_elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        print("Emergency")
        for i in range(len(self.elevators)):
            print(f"evaquating elevator {i+1}")
            elevator = self.elevators[i]
            elevator.go_to_floor(self.bottom_floor)

#Main
my_building=Building(1,10,3)

my_building.run_elevator(1,5)

my_building.fire_alarm()

