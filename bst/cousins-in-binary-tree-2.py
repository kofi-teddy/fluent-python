# Given the root of a binary tree, replace the value of each node in 
# the tree with the sum of all its cousins' values.
# Two nodes of a binary tree are cousins if they have the same depth 
# with different parents.
# Return the root of the modified tree.`
# Note that the depth of a node is the number of edges in the path 
# from the root node to it.

# Example 1:
# Input: root = [5,4,9,1,10,null,7]
# Output: [0,0,0,7,7,null,11]
# Explanation: The diagram above shows the initial binary tree and 
# the binary tree after changing the value of each node.
# - Node with value 5 does not have any cousins so its sum is 0.
# - Node with value 4 does not have any cousins so its sum is 0.
# - Node with value 9 does not have any cousins so its sum is 0.
# - Node with value 1 has a cousin with value 7 so its sum is 7.
# - Node with value 10 has a cousin with value 7 so its sum is 7.
# - Node with value 7 has cousins with values 1 and 10 so its sum is 11.

# Example 2:
# Input: root = [3,1,2]
# Output: [0,0,0]
# Explanation: The diagram above shows the initial binary tree and the 
# binary tree after changing the value of each node.
# - Node with value 3 does not have any cousins so its sum is 0.
# - Node with value 1 does not have any cousins so its sum is 0.
# - Node with value 2 does not have any cousins so its sum is 0.
 
# Constraints:
# The number of nodes in the tree is in the range [1, 105].
# 1 <= Node.val <= 104

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def replace_with_cousines_sum(root: TreeNode)   -> TreeNode:
    if not root:
        return root

    # Queue for BFS (Breadth-First Search)
    queue = [(root, None)]
    
    while queue:
        next_level = []
        # dictionay to store node's parent.
        parent_map = {} 
        level_sum = 0

        # Process all nodes at the current level
        for node, parent in queue:
            # Store the parent information
            parent_map[node] = parent
            # Add nodes value to the total level sum
            level_sum += node.val

            # Add children to the next level queue
            if node.left:
                next_level.append((node.left, node))
            if node.right:
                next_level.append((node.right, node))

        # Update each nodes value based on its cousins sum
        for node, parent in queue:
            sibling_sum = 0

            # Calculate siblings sum by checking nodes with the same parent
            for other_node, other_parent in queue:
                if other_parent == parent:
                    sibling_sum += other_node.val

            # Cousins sum is total level sum minus siblings sum
            node.val = level_sum - sibling_sum

        # Move to the next level
        queue =  next_level

    return root


# Helper function to print the tree in level order
def print_tree(root: TreeNode):
    if not root:
        return
    queue = [root]
    result = []
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Prune trailing None values for clearer output
    while result and result[-1] is None:
        result.pop()
    print(result)


# Create the binary tree: [5, 4, 9, 1, 10, None, 7]
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(9)
root.left.left = TreeNode(1)
root.left.right = TreeNode(10)
root.right.right = TreeNode(7)


# Original tree
print("Original tree:")
print_tree(root)


# Modify the tree by replacing values with cousin sums
replace_with_cousines_sum(root)

# Modified tree
print("Modified tree:")
print_tree(root)