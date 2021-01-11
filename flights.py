# A program for flight operations 
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add__passengers(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)
        
flight = Flight(2)

people = ["Nabeel", "Aqeel", "Israr", "Shahroz"]

for person in people:
    success = flight.add__passengers(person)
    if success:
        print(f"Added {person} to flight successfully")
    else:
        print(f"Sorry, There is no available seats for {person} right now")