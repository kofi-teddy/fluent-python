# advance data structures
# linked list in python
# node code
class Node:

    # function to initialize the node object
    def __init__(self, data):
        self.data = data # assign data 
        self.next = None # initialize next as null

# lint list class
class LinkedList:

    # function to initialize the linked 
    # list object 
    def __init__(self):
        self.head = None

    # this function prints contents of linked list object
    # starting from head
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


# code execution starts here 
if __name__=='__main__':

    # start with the empty list 
    mylist = LinkedList()

    mylist.head = Node(1)
    second = Node(2)
    third = Node(3)

    '''
    three nodes have been created
    we have reference to there 3 blocks as head, second and third

     llist.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1 | None |     | 2 | None |     | 3 | None |
    +----+------+     +----+------+     +----+------+
    '''

    mylist.head.next = second # Link second node with the third node

    '''
    Now next of second Node refers to third. So all three
    nodes are linked.
 
    llist.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1 | o-------->| 2 | o-------->| 3 | null |
    +----+------+     +----+------+     +----+------+
    '''
    second.next = third

    mylist.printList()