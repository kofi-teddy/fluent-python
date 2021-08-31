# Using classes and property


class Presenter():
    def __init__(self, name):
        # Constructor
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        # Validation
        self.__name = value

    def say_hello(self):
        print("Hello"+" "+self.name)


presenter = Presenter("Chris")
presenter.name = "Christopher"
presenter.say_hello() 