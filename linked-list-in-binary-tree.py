# Given a binary tree root and a linked list with head as the first node. 
# Return True if all the elements in the linked list starting from the head 
# correspond to some downward path connected in the binary tree otherwise 
# return False.
# In this context downward path means a path that starts at some 
# node and goes downwards.

# Example 1:
# Input: head = [4,2,8], 
# root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true
# Explanation: Nodes in blue form a subpath in the binary Tree.

# Example 2:
# Input: head = [1,4,2,6], 
# root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: true

# Example 3:
# Input: head = [1,4,2,6,8], 
# root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
# Output: false
# Explanation: There is no path in the binary tree that contains 
# all the elements of the linked list from head.

# Constraints:
# The number of nodes in the tree will be in the range [1, 2500].
# The number of nodes in the list will be in the range [1, 100].
# 1 <= Node.val <= 100 for each node in the linked list and binary 
# tree.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        # helper function to check if we can match the linked list 
        # from the current tree node
        def dfs(tree_node: TreeNode, list_node: ListNode) -> bool:
                
            # if we've matched the entire linked list
            if not list_node:
                return True
            
            # if reached a null tree node without matching the list 
            if not tree_node:
                return False
            
            # if the values match, continue both left and right subtrees
            if tree_node.val == list_node.val:
                return dfs(tree_node.left, list_node.next) or dfs(tree_node.right, list_node.next)
            
            return False
        
        # check if the current tree node or any subtree of the tree contains 
        # the lined list
        def search(tree_node: TreeNode) -> bool:

            if not tree_node:
                return False
            
            # start checking from the current tree node or continue checking its children
            return dfs(tree_node, head) or search(tree_node.left) or search(tree_node.right)
        
        return search(root)