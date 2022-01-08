# python class that represents an individual node
# in a binary tree
# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key


# # create root
# root = Node(1)
# ''' 
# following is the tree after above statement
#          1
#         / \
#      None None
# '''

# root.left = Node(2)
# root.right = Node(3)

# ''' 
# 2 and 3 become left and right children of 1
#          1
#         / \
#       2     3
#      / \   / \
# None None None None
# '''

# root.left.left = Node(4)
# '''
# 4 becomes left child of 2
#         1
#     /     \
#   2         3
# / \        / \
# 4 None None None
# / \
# None None
# '''


# python program to demonstrate tree traversal

# a class that represents an individual node in a tree
# binary tree
# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key


# # a function to do inorder tree traversal
# def printInorder(root):

#     if root:

#         # first recur on left child
#         printInorder(root.left)

#         # then print the data of node
#         print(root.val),

#         # now recur on right child
#         printInorder(root.right)


# # a function to do postorder tree traversal
# def printPostorder(root):

#     if root:

#         # first recur on left child
#         printPostorder(root.left)

#         # first recur on right child
#         printPostorder(root.right)

#         # now print the data of nodes 
#         print(root.val)


# #  a fucntion to do preorder tree traversal
# def printPreorder(root):
    
#     if root:

#         # first print the data of node
#         print(root.val)

#         # finally recur on right child
#         printPreorder(root.left)

#         # finally recur on right child
#         printPreorder(root.right)



# # Driver code 
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# print('Preorder traversal of binary tree is ')
# printPreorder(root)

# print('\nInorder traversal of binary tree is ')
# printInorder(root)

# print('\nPostorder traversal of binary tree is')
# printPostorder(root)


# python program to print level 
# order traversal using queue 

# a node structures
class Node:

    # a utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None 
        self.right = None 


# iterate method to print the 
# height of a binary tree 
def printLevelOrder(root):

    # base case 
    if root is None:
        return

    # create an empty queue
    # for level order traversal
    queue = []

    # enqueue root and initialize height
    queue.append(root)

    while(len(queue) > 0):

        # print front of queue and
        # remove it from queue
        print(queue[0].data)
        node = queue.pop(0)

        # enqueue left child 
        if node.left is not None:
            queue.append(node.left)

        # enqueue right child
        if node.right is not None:
            queue.append(node.right)


# Driver program to test above function 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('level order traversal of binary tree is -')
printLevelOrder(root)