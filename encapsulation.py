# python program to 
# demonstrate protected members 


# Creating a base class 
class Base:

    def __init__(self):

        # protected member 
        self._a = 2 


# creating a derived class 
class Derived(Base):

    def __init__(self):

        # calling constructor of
        # base class 
        Base.__init__(self)
        print('calling protected member of base class: ')
        print(self._a)


obj1 = Derived()
obj2 = Base()


# calling protected member 
# outside class will result in 
# AttributeError
# print(obj2.a)


# python program to 
# demonstrate private members 

# creating a base class 
class Base:
    def __init__(self):
        self.a = 'Skycrew Technologies'
        self.__c = 'Software Development'


# creating derived class
class Derived(Base):

    def __init__(self):

        # calling constructor of 
        # base class 
        Base.__init__(self)
        print('calling private member of base class: ')
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)
print(obj1.c)
