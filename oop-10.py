# oop
# Multiple inheritance  

# the diamon problem 
from pprint import pprint

# class Base:
#     num_base_calls = 0

#     def call_me(self) -> None:
#         print('Calling method on Base')
#         self.num_base_calls += 1


# class LeftSubClass(Base):
#     num_left_calls = 0

#     def call_me(self) -> None:
#         Base.call_me(self)
#         print('Calling method on LeftSubClass')
#         self.num_left_calls += 1


# class RightSubClass(Base):
#     num_right_calls = 0

#     def call_me(self) -> None:
#         Base.call_me(self)
#         print('Calling method on RightSubClass')
#         self.num_right_calls += 1


# class Subclass(LeftSubClass, RightSubClass):
#     num_sub_calls = 0

#     def call_me(self) -> None:
#         LeftSubClass.call_me(self)
#         RightSubClass.call_me(self)
#         print('Calling method on Subclass')
#         self.num_sub_calls += 1


# Using super() to solve issues with diamond problems
class Base:
    num_base_calls = 0

    def call_me(self):
        print('Calling method on Base')
        self.num_base_calls += 1


class LeftSubclass_S(Base):
    num_left_calls = 0

    def call_me(self) -> None:
        super().call_me()
        print('Calling method on LeftSubclass')
        self.num_left_calls += 1


class RightSubclass_S(Base):
    num_right_calls = 0

    def call_me(self) -> None:
        super().call_me()
        print('Calling method on RightSubclass_S')
        self.num_right_calls += 1


class Subclass_S(LeftSubclass_S, RightSubclass_S):
    num_sub_calls = 0

    def call_me(self) -> None:
        super().call_me()
        print('Calling method on Subclass_S')
        self.num_sub_calls += 1

# Driver code
ss = Subclass_S()
ss.call_me()
print(
    ss.num_sub_calls,
    ss.num_left_calls, 
    ss.num_right_calls, 
    ss.num_base_calls
    )

# driver code for mro 
pprint(Subclass_S.__mro__)


# Driver code
# s = Subclass()
# s.call_me()
# print(
#     s.num_sub_calls,
#     s.num_left_calls, 
#     s.num_right_calls, 
#     s.num_base_calls
#     )

