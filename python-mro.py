# MRO is a concept used in inheritance. It is the order in which 
# a method is searched for in a classes hierarchy and is especially 
# useful in Python because Python supports multiple inheritance.

# In Python, the MRO is from bottom to top and left to right. This 
# means that, first, the method is searched in the class of the object. 
# If it’s not found, it is searched in the immediate super class. 
# In the case of multiple super classes, it is searched left to right, 
# in the order by which was declared by the developer.


# Method Resolution Order :
# Method Resolution Order(MRO) it denotes the way a programming language 
# resolves a method or attribute. Python supports classes inheriting 
# from other classes. The class being inherited is called the Parent or 
# Superclass, while the class that inherits is called the Child or 
# Subclass. In python, method resolution order defines the order in 
# which the base classes are searched when executing a method. First, 
# the method or attribute is searched within a class and then it 
# follows the order we specified while inheriting. This order is also 
# called Linearization of a class and set of rules are called MRO(Method 
# Resolution Order). While inheriting from another class, the 
# interpreter needs a way to resolve the methods that are being called 
# via an instance. Thus we need the method resolution order. For 
# Example

class A:
  def method(self):
    print("A.method() called")

class B:
  def method(self):
    print("B.method() called")

class C(A, B):
  pass

class D(C, B):
  pass

d = D()
d.method()


# Methods for Method Resolution Order(MRO) of a class:
# To get the method resolution order of a class we can use
# either __mro__ attribute or mro() method. By using these 
# methods we can display the order in which methods are resolved. 
# For Example


# Python program to show the order
# in which methods are resolved
  
class A:
    def rk(self):
        print(" In class A")
class B:
    def rk(self):
        print(" In class B")
  
# classes ordering
class C(A, B):
    def __init__(self):
        print("Constructor C")
  
r = C()
  
# it prints the lookup order 
print(C.__mro__)
print(C.mro())


# We can use multiple inheritance to add this new class as a parent of our existing
# Friend class. The tricky part is that we now have two parent __init__() methods,
# both of which need to be called. And they need to be called with different arguments.
# How do we do this? Well, we could start with a naïve approach for the Friend class,
# also:
class Friend(Contact, AddressHolder):
    def __init__(
    self,
    name: str,
    email: str,
    phone: str,
    street: str,
    city: str,
    state: str,
    code: str,
    ) -> None:
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone

# In this example, we directly call the __init__() function on each of the superclasses
# and explicitly pass the self argument. This example technically works; we can access
# the different variables directly on the class. But there are a few problems.

# First, it is possible for a superclass to remain uninitialized if we neglect to explicitly
# call the initializer. That wouldn't break this example, but it could cause hard-todebug program crashes in common scenarios. We would get a lot of strange-looking
# AttributeError exceptions in classes where there's clearly an __init__() method. It's
# rarely obvious the __init__() method wasn't actually used.
# A more insidious possibility is a superclass being called multiple times because of
# the organization of the class hierarchy. Look at this inheritance diagram:

# The __init__() method from the Friend class first calls __init__() on the Contact
# class, which implicitly initializes the object superclass (remember, all classes derive
# from object). The Friend class then calls __init__() on AddressHolder, which
# implicitly initializes the object superclass again. This means the parent class has
# been set up twice. With the object class, that's relatively harmless, but in some
# situations, it could spell disaster. Imagine trying to connect to a database twice for
# every request!

# The base class should only be called once. Once, yes, but when? Do we call Friend,
# then Contact, then Object, and then AddressHolder? Or Friend, then Contact,
# then AddressHolder, and then Object?

# Let's contrive an example to illustrate this problem more clearly. Here, we have
# a base class, BaseClass, that has a method named call_me(). Two subclasses,
# LeftSubclass and RightSubclass, extend the BaseClass class, and each overrides the
# call_me() method with different implementations.

# Then, another subclass extends both of these using multiple inheritance with a
# fourth, distinct implementation of the call_me() method. This is called diamond
# inheritance because of the diamond shape of the class diagram:

# Let's convert this diagram into code. This example shows when the methods are
# called:
class BaseClass:
    num_base_calls = 0

    def call_me(self) -> None:
        print("Calling method on BaseClass")
        self.num_base_calls += 1


class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self) -> None:
        BaseClass.call_me(self)
        print("Calling method on LeftSubclass")

        self.num_left_calls += 1


class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self) -> None:
        BaseClass.call_me(self)
        print("Calling method on RightSubclass")

        self.num_right_calls += 1


class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0

    def call_me(self) -> None:
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        print("Calling method on Subclass")

        self.num_sub_calls += 1

# driver code
s = Subclass()
s.call_me()
 print(
    s.num_sub_calls,
    s.num_left_calls,
    s.num_right_calls,
    s.num_base_calls)

# Thus, we can see the base class's call_me() method being called twice. This could
# lead to some pernicious bugs if that method is doing actual work, such as depositing
# into a bank account, twice. 


# Python's Method Resolution Order (MRO) algorithm transforms the diamond
# into a flat, linear tuple. We can see the results of this in the __mro__ attribute of a
# class. The linear version of this diamond is the sequence Subclass, LeftSubclass,
# RightSubClass, BaseClass, object. What's important here is that Subclass lists
# LeftSubclass before RightSubClass, imposing an ordering on the classes in the
# diamond. 

# The thing to keep in mind with multiple inheritance is that we often want to call
# the next method in the MRO sequence, not necessarily a method of the parent class.
# The super() function locates the name in the MRO sequence. Indeed, super() was
# originally developed to make complicated forms of multiple inheritance possible. 

# Here is the same code written using super(). We've renamed some of the classes,
# adding an _S to make it clear this is the version using super():

class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print("Calling method on Base Class")

        self.num_base_calls += 1


class LeftSubclass_S(BaseClass):
    num_left_calls = 0

    def call_me(self) -> None:
        super().call_me()
        print("Calling method on LeftSubclass_S")

        self.num_left_calls += 1


class RightSubclass_S(BaseClass):
    num_right_calls = 0
    def call_me(self) -> None:
        super().call_me()
        print("Calling method on RightSubclass_S")

        self.num_right_calls += 1


class Subclass_S(LeftSubclass_S, RightSubclass_S):
    num_sub_calls = 0

    def call_me(self) -> None:
        super().call_me()
        print("Calling method on Subclass_S")

        self.num_sub_calls += 1


# The change is pretty minor; we only replaced the naive direct calls with calls to
# super(). The Subclass_S class, at the bottom of the diamond, only calls super()
# once rather than having to make the calls for both the left and right. The change
# is easy enough, but look at the difference when we execute it:

# driver code 
ss = Subclass_S()
ss.call_me()

print(ss.num_sub_calls, ss.num_left_calls, ss.num_right_calls, ss.num_base_calls)
pprint(Subclass_S.__mro__)
