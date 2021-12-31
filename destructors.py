# python program to illustrate destructors
class Employee:

    # initializing
    def __init__(self):
        print('Employee created.')

    # deleting (calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted')


# obj = Employee()
# del obj


# python program to illustrate destructors
class Employee:

    # initializing
    def __init__(self):
        print('Employee created')

    # calling destructor
    def __del__(self):
        print('Destructor called')


def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj


# print('Calling Created_obj() function...')
# obj = Create_obj()
# print('Program End...')


# python program to illustrate destructor
class A:
    def __init__(self, bb):
        self.b = bb

class B:
    def __init__(self):
        self.a = A(self)

    def __del__(self):
        print('die')

def fun():
    b = B()

fun()