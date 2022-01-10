# Data classes in python 
# @dataclasses.dataclass
# (*, init=True, repr=True, eq=True, order=False, 
# unsafe_hash=False, frozen=False)

# By changing the values of these parameters, 
# we can modify the behavior and functioning 
# of the default constructor been made for 
# our DataClasses.

# This parameter specifies that there should 
# be a default constructor or not.

from dataclasses import dataclass


# @dataclass(init=False)
# class Article():

#     title: str
#     author: str
#     language: str
#     upvotes: int


# # dataclass object
# article = Article('Metaverse', 'kofi teddy', 'python')

# print(article)


# This parameter specifies how the 
# __repr__() function will behave. 
# False value corresponds to hash 
# value representation of the object 
# in memory. 
# @dataclass(repr=False)
# class Article():

#     title: str
#     author: str
#     language: str
#     upvotes: int


# # dataclass object
# article = Article('Metaverse', 'kofi teddy', 'python', '1')

# print(article)


# eq : This parameter is used to specify the 
# operation performed in comparison when two 
# DataClasses are compared for equality 
# using == or != operators.
# When eq=False, the two object are compared 
# using their hash based on its location in 
# memory like two normal objects. Since the 
# two objects have different hash representation, 
# their equality returns False.
# @dataclass(repr=False, eq=False)
# class Article():

#     title: str
#     author: str
#     language: str
#     upvotes: int


# # dataclass object
# article1 = Article('Metaverse', 'kofi teddy', 'python', '1')
# article2 = Article('Open Source', 'kofi teddy', 'python', '1')
# article3 = Article('Metaverse', 'kofi teddy', 'python', '1')

# equal = article1 == article2
# print('classes equal: ', equal)


# supports >, >=, < and <= operators when 
# order=True is set in argument parameter.
# The comparison between objects is based 
# on the comparison between their corresponding 
# attributes, which is done one by one starting 
# from the first one.
# @dataclass(order=True)
# class A():
#     var1: int
#     var2: str
#     var3: float

# obj1 = A(1, 'Skycrew Technologies', 7.0)
# obj2 = A(2, 'Skycrew Technologies', 7.0)
# obj3 = A(1, 'st', 7)
# obj4 = A(1, 'Skycrew Technologies', 8.0)


# print(obj1 > obj2)
# print(obj1 < obj3)
# print(obj1 >= obj4)



# the frozen sets all the variables in the DataClass 
# as one-time initializable that is once 
# initialized, it cannot be reassigned a new value. 
# @dataclass(frozen=True)
# class Article():

#     title: str
#     author: str
#     language: str 
#     upvotes: int


# article = Article('OpenAI', 'koif teddy', 'python', 0)
# print(article)

# article.upvotes = 100
# print(article)


# unhashable means their hash cannot be generated
# using the hash() function of Python.
# @dataclass()
# class Article():

#     title: str
#     author: str
#     language: str 
#     upvotes: int


# article = Article('OpenAI', 'koif teddy', 'python', 0)
# print(article)

# print(hash(article))


# frozen=True sets the variables one-time initializable
# and hence makes the object immutable. This safely 
# generates a hash for the DataClass object.
# @dataclass(frozen=True)
# class Article():

#     title: str
#     author: str
#     language: str 
#     upvotes: int


# article = Article('OpenAI', 'koif teddy', 'python', 0)
# print(article)

# print(hash(article))


# unsafe_hash forces a DataClass which is
# still mutable to generate a hash.
@dataclass(unsafe_hash = True)
class Article():

    title: str
    author: str
    language: str 
    upvotes: int


article = Article('OpenAI', 'koif teddy', 'python', 0)
print(article)

print(hash(article))