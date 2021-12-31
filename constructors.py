# python code for default constructor


class SkycrewFamily:

    # defualt constructor
    def __init__(self):
        self.sky = 'Skycrew'

    # method for printing the data members
    def print_sky(self):
        print(self.sky)


# creating object of the class 
obj = SkycrewFamily()

# calling the instance method using the object
# obj.print_sky()


# parameterized constructor
class Addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print(f'Firts number = {self.first}') 
        print(f'Second number = {self.first}') 
        print(f'Addition of two number = {self.answer}') 

    def calculate(self):
        self.answer = self.first + self.second

    
# creating object of the class 
# this will invoke parameterized constructor
obj = Addition(1000, 2000)

# perform Addition
obj.calculate()

# display result
obj.display()