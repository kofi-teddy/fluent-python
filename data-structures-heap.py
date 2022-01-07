# importing 'heapq' to implement heap queue
import heapq

# initializing list 
mylist = [5, 7, 9, 1, 3]

# using heapify to convert list into heap
heapq.heapify(mylist)

# printing created heap 
print('The created heap is: ', end='')
print(list(mylist))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(mylist, 4)

# printing modified heap 
print('the modified heap after push is: ',end='')
print(list(mylist))

# using heappop() to pop smallest element
print('the popped and smallest element is: ',end='')
print(heapq.heappop(mylist))