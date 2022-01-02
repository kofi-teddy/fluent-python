# python program to show that the variables with a value 
# assigned in class declarations are class variables

# class for computer science student
class CSStudent:
    
    stream = 'cse'
    def __init__(self, name, roll):
        self.name = name # instance variable
        self.roll = roll # instance variable

# objects of CSStudent class 
a = CSStudent('Teddy', 1)
b = CSStudent('Benkaf', 2)

print(a.stream) # prints 'cse'
print(b.stream) # print 'cse'
print(a.name) # print 'Kofi'
print(b.name) # print 'benkaf'
print(a.roll) # print '1'
print(b.roll) # print '2'

# class variables can be accessed using class 
# name also
print(CSStudent.stream) # print 'cse'

# Now if we change the stream for just a it wont be changed for b 
a.stream = 'ece'
print(a.stream) # print 'ece'
print(b.stream) # print 'cse'

# to change the stream for all instances of the class we can change it 
# directly from the class
CSStudent.stream = 'mech'

print(a.stream) # print 'ece'
print(b.stream) # prints 'mech'
