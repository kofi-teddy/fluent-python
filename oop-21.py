# creating an abstract base class 
from collections.abc import Container

# class MediaLoader(abc.ABC):
#     @abc.abstractmethod
#     def play(self) -> None:
#         ...


# @property
# @abc.abstractmethod
# def ext(self) -> str:
#     ...


# class Wav(MediaLoader):
#     pass


# class Ogg(MediaLoader):
#     ext = '.ogg'

#     def play(self):
#         pass


class OddIntegers:
    def __contains__(self, x: int) -> bool:
        return x % 2 != 0


# driver code 
# MediaLoader.__abstractmethod__
# x = Wav()

odd = OddIntegers()
print(isinstance(odd, Container))
print(issubclass(OddIntegers, Container))

'''
One cool thing about the Container ABC is that any class that implements it
gets to use the in keyword for free. In fact, in is just syntax sugar that delegates
to the __contains__() method. Any class that has a __contains__() method is
a Container and can therefore be queried by the in keyword
'''
print(1 in odd)
print(2 in odd)
print(3 in odd)



