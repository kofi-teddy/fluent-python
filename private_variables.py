# python code to illustrate how mangling works 


class Map:

    def __init__(self, iterate):
        self.list = []
        self.__magud(iterate)
    def magud(self, iterate):
        for item in iterate:
            self.list.appent(item)

    # private copy of original magud() methods
    __magud = magud


class MapSubclass(Map):

    # provide new signature for magud() but
    # does not break __init__()
    def geek(self, key, value):
        for i in zip(keys, value):
            self.list.append(i)


# python code to illustrate 
# how single underscore works 
def _get_errors(self):
    if self._errors is None:
        self.full_clean()
    return self._errors


errors = property(_get_errors)


# python code to illustrate how double 
# underscore at the beginning works 
class Skycrew:
    
    def _single_method(self):
        pass
    
    def __double_method(self): # for mangling 
        pass


class Pyth(Skycrew):

    def __double_method(self): # for mangling 
        pass


# python code to illustrate double leading and 
# double trailing underscore works
class Magud:

    # '__init__' for initializing, this is 
    # special method
    def __init__(self, ab):
        self.ab = ab

    # custom special method. try not to use it 
    def __custom__(self): 
        pass
