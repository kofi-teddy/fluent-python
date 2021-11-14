# Method Resolution Order
# Python program to show the order
# in which methods are resolved


'''
In Python, the MRO is from bottom to top and left to right.
'''
  
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