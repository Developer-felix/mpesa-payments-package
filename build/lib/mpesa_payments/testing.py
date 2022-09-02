"""
Auther : Onjomba Felix
Phone : +254717713943
license : MIT
"""

class Testing:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def testing(self):
        print("Testing: ")
    
    def myfunction(self, state):
        self.testing()
        print("My name is " + self.name +" and my state is " + state)

test = Testing(
    "Felix",
    "These is Felix"
)

print(test.myfunction(
    state = "Nairobi"
))


