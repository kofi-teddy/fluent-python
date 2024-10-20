# Traversal(Inorder traversal of BST)
# Inorder traversal gives nodes in non-decreasing 
# order visit the left child first then root and 
# then the right child
# Time Complexity: O(N), where N is the number of 
# nodes of the BST


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None


# Utility function to do inorder traversal
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Driver code
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(12)
    root.right.right = Node(18)
    inorder(root)

    print()