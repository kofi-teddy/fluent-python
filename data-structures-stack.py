# advance data structures 
# stack
# implementing using list

# stack = []

# append() function to push 
# element in the stack 
# stack.append('g')
# stack.append('f')
# stack.append('g')

# print('initial stack')
# print(stack)

# pop() funtion to pop 
# element from stack in 
# LIFO
# print('\nelements popped from stack: ')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print('\nstack after elements are popped')
# print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty


# implementing using collectio.deque 
from collections import deque 

# stack = deque()

# append() function to push 
# element in the stack 
# stack.append('g')
# stack.append('f')
# stack.append('g')

# print('initial stack')
# print(stack)

# pop() funtion to pop 
# element from stack in 
# LIFO
# print('\nelements popped from stack: ')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print('\nstack after elements are popped')
# print(stack)


# implementing using queue
from queue import LifoQueue


# initializing a stack 
# stack = LifoQueue(maxsize=3)

# qsize() show the number of elements in the stack
# print(stack.qsize())

# put() function to push 
# element in the stack
# stack.put('g')
# stack.put('f')
# stack.put('g')

# print('full:L ', stack.full())
# print('size: ', stack.qsize())

# get() function to pop element from stack in
# LIFI order
# print('\nelements popped from the stack')
# print(stack.get())
# print(stack.get())
# print(stack.get())

# print('\nEmpty: ', stack.empty())