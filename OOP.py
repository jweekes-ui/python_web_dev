
class Flight():
    def __init__ (self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def print_passengers(self):
        print(f"The current Passengers are {self.passengers}")
    
    
    def add_passenger(self, name):
        # Check length of passengers
        if (len(self.passengers) >= self.capacity):
            print(f"Flight capacity filled. No More Passengers can be added.")
            
        else:
            self.passengers.append(name)
            self.print_passengers()

    def remove_passenger(self, name):
        # Check that passenger is in the list
        passenger_present = name in self.passengers  # This returns a Boolean value
        if (passenger_present):
            self.passengers.remove(name)
            print(f"{name} has been removed from the passenger list")
            self.print_passengers()
        else:
            print(f"{name} is not in the passenger list")



flight09 = Flight(4)
# Testing the Flight class
flight09.add_passenger("John")
flight09.add_passenger("Jake")
flight09.remove_passenger("Carla")
flight09.remove_passenger("Jake")
flight09.add_passenger("Carla")

