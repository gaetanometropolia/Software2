# Extend the previous program by creating a Building class. The initializer parameters for the class are the numbers of the bottom and top floors and the number of elevators in the building. When a building is created, the building creates the required number of elevators. The list of elevators is stored as a property of the building. Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters. In the main program, write the statements for creating a new building and running the elevators of the building.

class Elevator:
    def __init__(self, bottom_floor , top_floor ):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print (f"elevator is now at {self.current_floor}")
        else:
            print("U are already at the top floor")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"elevator is now at {self.current_floor}")
        else:
            print("already at bottom floor")

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


#Main
my_building=Building(1,10,3)

my_building.run_elevator(1,5)

