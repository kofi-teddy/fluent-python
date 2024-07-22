# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

# For each index i, names[i] and heights[i] denote the name and height of the ith person.

# Return names sorted in descending order by the people's heights.

 

# Example 1:

# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.
# Example 2:

# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
 

# Constraints:

# n == names.length == heights.length
# 1 <= n <= 103
# 1 <= names[i].length <= 20
# 1 <= heights[i] <= 105
# names[i] consists of lower and upper case English letters.
# All the values of heights are distinct.


class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        # Combine the names and heights into a list of tuples
        combined = list(zip(names, heights))
        
        # Sort the combined list based on heights in descending order
        combined.sort(key=lambda x: x[1], reverse=True)
        
        # Extract the sorted names
        sorted_names = [name for name, height in combined]
        
        return sorted_names


# Example usage:
sol = Solution()
names1 = ["Mary", "John", "Emma"]
heights1 = [180, 165, 170]
print(sol.sortPeople(names1, heights1))  # Output: ["Mary", "Emma", "John"]

names2 = ["Alice", "Bob", "Bob"]
heights2 = [155, 185, 150]
print(sol.sortPeople(names2, heights2))  # Output: ["Bob", "Alice", "Bob"]
