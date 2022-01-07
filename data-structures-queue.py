# advance data structures
# Queue
# queue = []

# # adding elements to the Queue
# queue.append('g')
# queue.append('f')
# queue.append('g')

# print('initial queue')
# print(queue)

# # removing elements from the queue
# print('\nqueue after removing elements')
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))

# print('\nqueue after removing elements')
# print(queue)

# uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty

# implementing using deque
from collections import deque
# queue = deque()

# # adding elements to the Queue
# queue.append('g')
# queue.append('f')
# queue.append('g')

# print('initial queue')
# print(queue)

# # removing elements from the queue
# print('\nqueue after removing elements')
# print(queue.popleft())
# print(queue.popleft())
# print(queue.popleft())

# print('\nqueue after removing elements')
# print(queue)


# implementing using the queue.queue
# from queue import Queue


# queue = Queue(maxsize=3)

# # qsize() give the maxsize
# # of the Queue
# print(queue.qsize())

# # adding elements to the Queue
# queue.put('g')
# queue.put('f')
# queue.put('g')

# # return boolean for full 
# # queue
# print('\nFull: ', queue.full())

# print('initial queue')
# print(queue)

# # removing elements from the queue
# print('\nqueue after removing elements')
# print(queue.get())
# print(queue.get())
# print(queue.get())

# # return boolean for empty 
# # queue
# print('\nEmpty: ', queue.empty())

# queue.put(1)
# print('\nEmpty: ', queue.empty())
# print('Full: ', queue.full())

# this would result into infinite 
# loop as the queue is Empty
# print(g.get())



# a simple implementation of priority Queue
# using Queue
class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self): 
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self): 
        return len(self.queue) == 0

    # for inserting an element into the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7)
    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.delete())