# implementation of binary search tree
# The steps of searching a node in BST:
# 1. Compare the elements to be searched with the 
# root element of the tree.
# - if the root is matched with the target element, 
# then return the node's location.
# - if it is not matched, then check whether the item
# is less than the root element, if it is smaller than 
# the root element, then move to the left subtree
# - If it is largest than the root element, then move to 
# the right subtree
# 2. Repeat the above procedure recursively until the 
# match is found.
# 3. If the element is not found or not present in the 
# tree then return NULL

# Time Complexity: O(h) where h is height of BST

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    

def search(root, key):

    # base case: root is null or key is 
    # present at root
    if root is None or root.key == key:
        return root

    # key is greater than roots key
    if root.key < key:
        return search(root.right, key)

    # key is smaller than roots key
    return search(root.left, key)


# creating a hard coded tree for keeping
# the length of the code small. We need 
# to make sure that BST properties are 
# maintained if we try some other cases
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

# search for keys in the BST
print("Found" if search(root, 80) else "Not Found")