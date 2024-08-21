class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def inorder_traversal(self):
        # Base case if the root is none
        if root is None:
            return 
        
        # Recursive case: traverse left subtree, visit root, traverse right subtree
        if self.left:
            self.left.inorder_traversal()

        print(self.value, end=" -> ")

        if self.right:
            self.right.inorder_traversal()


# Usage 
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(4)

print(root.inorder_traversal())

