# Delete a Node of BST
# used to delete a node with specific key from the 
# BST and return the new BST

# Scenarios for deleting the node:
# 1. Node to be deleled is the leaf node, its simple 
# just null it out

# 2. Node to be deleted has one child: replace the node 
# with the child node

# 3. Node to be deleted has two children: delete the node 
# in such a way that the resulting tree follows the 
# properties of a BST. The trick is to find the inorder 
# successor of the node. Copy contents of the inoder successor 
# to the node and delete the inorder successor.

# Take care of following thins while deleting a node of BST:
# 1. Need to figure out what will be the replacement of the 
# node to be deleted
# 2. What minimal distruption to the existing tree struture
# 3.Can take the replacement node from the deleted nodes left 
# or right subtree.
# 4. If taking if from the left subtree, we have to take the 
# largest value in the right subtree
# 5. If taking it from the right subtree, we have to take the 
# smallest value in the right subtree

# Time Complexity: O(h) where h is height of BST 


class Node:
    def __init__(self, key):
        self.key = key 
        self.left = None
        self.right = None


# Note that it is not a generic inorder successor
# function. It mainly works when the right child 
# is not empty, which is the case we need in BST
def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr


# this fucntion deletes a given key x from the 
# given BST and returns the modified root of the 
# BST (if it is modified)
def del_node(root, x):
    if root is None:
        return root

    # If key to be deleted is smaller than 
    # the root's key, then it lies in the 
    # left subtree.
    if root.key > x:
        root.left = del_node(root.left, x)
    
    # If key to be deleted is greater than 
    # the root's key, then it lies in the 
    # right subtree.
    elif root.key < x:
        root.right = del_node(root.right, x)
    
    # If the key is the same as the root's key,
    # this is the node to be deleted.
    else:
        # Case 1: Node with only one child or 
        # no child
        # if root matches with the given key
        # cases when root has 0 children or 
        # only right child 
        if root.left is None:
            return root.right

        # when root has only left child
        if root.right is None:
            return root.left

        # Case 2: Node with two children
        # Get the inorder successor 
        # (smallest in the right subtree)
        succ = get_successor(root)
        root.key = succ.key
        root.right = del_node(root.right, succ.key)

    return root


# Utility function to do inorder traversal of the BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Driver code to test the functions
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(12)
    root.right.right = Node(18)

    x = 15

    # Delete the node with key 15
    root = del_node(root, x)

    # Perform inorder traversal of the modified tree
    inorder(root)
    print()