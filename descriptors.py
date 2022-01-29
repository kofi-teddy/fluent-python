# Descriptors
# if at least one of the three methods i.e __get__
# __set__, __delete__ a descriptor has been created.
# __get__(self, obj, type=None), returns value
# __set__(self, obj, value), returns None 
# __delete(self, obj), returns None

from weakref import WeakKeyDictionary


# class MyDescriptor():
#     '''
#     A simple demo descriptor
#     '''
#     def __init__(self, initial_value=None, name='my_var'):
#         self.var_name = name
#         self.value = initial_value

#     def __get__(self, obj, objtype):
#         print('Getting', self.var_name)
#         return self.value
    
#     def __set__(self, obj, value):
#         msg = 'Setting {name} to {value}'
#         print(msg.format(name=self.var_name, value=value))
#         self.value = value


# class MyClass():
#     desc = MyDescriptor(initial_value='Mike', name='desc')
#     normal = 10


# if __name__ == '__main__':
#     c = MyClass()
#     print(c.desc)
#     print(c.normal)
#     c.desc = 100
#     print(c.desc)


class Drinker:
    def __init__(self):
        self.req_age = 21
        self.age = WeakKeyDictionary()

    def __get__(self, instance_obj, objtype):
        return self.age.get(instance_obj, self.req_age)

    def __set__(self, instance, new_age):
        if new_age < 21:
            msg = '{name} is too young to legally imbibe'
            raise Exception(msg.format(name=instance.name))
        self.age[instance] = new_age
        print('{name} can legally drink in the USA'.format(name=instance.name))

    def __delete__(self, instance):
        del self.age[instance]


class Person:
    drinker_age = Drinker()

    def __init__(self, name, age):
        self.name = name
        self.drinker_age = age

p = Person('Miguel', 30)
p = Person('Niki', 13)