# python program to demonstrate 
# insert operation in binary search tree
# A new key is always inserted at the leaf. 
# Start searching a key from the root till 
# a leaf node is found then add the new node 
# as a child of the leaf node.

# Time Complexity: O(h) where h is height of BST

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A utility function to insert 
# a new node with the given key
def insert(root, key):
    if root is None:
        return Node(key)
    
    if root.val == key:
        return root
    
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)

    return root


# A utility function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


# create the following BST
#       50
#      /  \
#     30   70
#    / \   / \
#   20 40 60 80

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

inorder(r)