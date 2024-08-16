# You are given m arrays, where each array is sorted in ascending order.
# You can pick up two integers from two different arrays (each array picks one) 
# and calculate the distance. We define the distance between two integers 
# a and b to be their absolute difference |a - b|.
# Return the maximum distance.
 
# Example 1:
# Input: arrays = [[1,2,3],[4,5],[1,2,3]]
# Output: 4
# Explanation: One way to reach the maximum distance 4 is to pick 1 in the first 
# or third array and pick 5 in the second array.

# Example 2:
# Input: arrays = [[1],[1]]
# Output: 0
 
# Constraints:
# m == arrays.length
# 2 <= m <= 105
# 1 <= arrays[i].length <= 500
# -104 <= arrays[i][j] <= 104
# arrays[i] is sorted in ascending order.
# There will be at most 105 integers in all the arrays.

# The algorithm processes each array once, and for each array, it performs 
# constant-time operations (finding the first and last element, calculating 
# distances). Hence, the time complexity is O(m), where m is the number of 
# arrays.


def maxDistance(arrays: list[list[int]]) -> int:
    # Initialize min_val and max_val with the first array's first 
    # and last element
    min_val, max_val = arrays[0][0], arrays[0][-1]
    max_distance = 0
    
    # Loop through the remaining arrays
    for i in range(1, len(arrays)):
        # Get the current array's first and last element
        current_min = arrays[i][0]
        current_max = arrays[i][-1]
        
        # Calculate the two potential distances
        max_distance = max(
            max_distance, 
            abs(current_max - min_val), abs(max_val - current_min)
        )
        
        # Update global min_val and max_val
        min_val = min(min_val, current_min)
        max_val = max(max_val, current_max)
    
    return max_distance


print(maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]))
