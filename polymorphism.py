# python program to demonstrate in-built
# polymorpic function


# len() being used for a string 
# print(len('Skycrew Technologies'))

# len() being used for a list 
# print(len([10, 20, 30]))


# a simple python function to demonstrate
# polymorphism

def add(x, y, z = 0):
    return x + y + z 


# driver code 
# print(add(2, 3))
# print(add(2, 3, 4))


class Ghana():
    
    def capital(self):
        print('Accra is the capital of Ghana.')

    def language(self):
        print('Twi is the most widely spoken language in Ghana')

    def type(self):
        print('Ghana is a developing country.')


class USA():

    def capital(self):
        print('Washington, D.C. is the capital of USA.')  

    def language(self):
        print('English is the primary language of USA.')  

    def type(self):
        print('USA is a developed country.')


# driver code
# obj_gha = Ghana()
# obj_usa = USA()

# for country in (obj_gha, obj_usa):
#     country.capital()
#     country.language()
#     country.type()


# polymorphism with inheritance
class Bird:
    
    def intro(self):
        print('There are many types of birds.')

    def flight(self):
        print('Most of the birds can fly out some cannot.')


class sparrow(Bird):
    
    def flight(self):
        print('Sparrows can fly.')


class ostrich(Bird):
    
    def flight(self):
        print('Ostriches cannot fly.')


# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()


# polymorphism with a function and objects
def func(obj):
    obj.capital()
    obj.language()
    obj.type()


obj_gha = Ghana()
obj_usa = USA()

# func(obj_gha)
# func(obj_usa)


# implementing polymorphism with a function 
class Togo():

    def capital(self):
        print('Lome is the capital of Togo')

    def language(self):
        print('French is the most widely spoken language.')

    def type(self):
        print('Togo is a developing country.')


class Canada():
    
    def capital(self):
        print('Toronto is the capital of Canada.')

    def language(self):
        print('English is the primary language of Canada.')

    def type(self):
        print('Canada is a developed country.')


# Driver code
def func(obj):
    obj.capital()
    obj.language()
    obj.type()

obj_togo = Togo()
obj_canada = Canada()

func(obj_togo)
func(obj_canada)

