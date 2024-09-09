# You are given two integers m and n, which represent the 
# dimensions of a matrix.

# You are also given the head of a linked list of integers.

# Generate an m x n matrix that contains the integers in the 
# linked list presented in spiral order (clockwise), starting from 
# the top-left of the matrix. If there are remaining empty spaces, 
# fill them with -1.

# Return the generated matrix.

# Example 1:
# Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
# Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
# Explanation: The diagram above shows how the values are printed 
# in the matrix.
# Note that the remaining spaces in the matrix are filled with -1.
# Example 2:

# Input: m = 1, n = 4, head = [0,1,2]
# Output: [[0,1,2,-1]]
# Explanation: The diagram above shows how the values are printed 
# from left to right in the matrix.
# The last space in the matrix is set to -1.

# Constraints:
# 1 <= m, n <= 105
# 1 <= m * n <= 105
# The number of nodes in the list is in the range [1, m * n].
# 0 <= Node.val <= 1000

class ListNode:
    def __init__(self, val=0, next=next):
        self.val = val 
        self.next = next


def spiral_matrix(m, n, head):
    # Initialize matrix with -1
    matrix = [[-1] * n for _ in range(m)]

    # initialize boundaries
    top, bottom, left, right = 0, m - 1, 0, n - 1

    # start from the head of the linked list
    current = head

    while top <= bottom and left <= right:
        # traverse from left to right along the top row
        for i in range(left, right + 1):
            if current:
                matrix[top][i] = current.val
                current = current.next

        top += 1

        # traverse from top to bottom along the right column
        for i in range(top, bottom + 1):
            if current:
                matrix[i][right] = current.val
                current = current.next
        
        right -= 1

        # traverse from right to left along the bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                if current:
                    matrix[bottom][i] = current.val
                    current = current.next
            bottom -= 1 

        # traverse from bottom to top along the left column 
        if left <= right:
            for i in range(bottom, top - 1, -1):
                if current:
                    matrix[i][left] = current.val
                    current = current.next
            left += 1

    return matrix   


# helper function to create a linked list from a list of values 
def create_linked_list(vals):
    dummy = ListNode()
    current = dummy
    for val in vals:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


m, n = 3, 5
head_vals = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
head = create_linked_list(head_vals)
result = spiral_matrix(m, n, head)

for row in result:
    print(row)