# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -5 * 104 <= nums[i] <= 5 * 104


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Helper function to merge two sorted halves
        # Base case: single element or empty list is 
        # already sorted
        if len(nums) <= 1:
            return nums
        
        # Split the array into two halves
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        # Merge the sorted halves
        return self.merge(left_half, right_half)
    
    def merge(self, left, right):
        sorted_list = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
        
        # Append any remaining elements from 
        # the left or right list
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        
        return sorted_list
        

solution = Solution()
print(solution.sortArray([5, 2, 3, 1]))  # Output: [1, 2, 3, 5]
print(solution.sortArray([5, 1, 1, 2, 0, 0]))  # Output: [0, 0, 1, 1, 2, 5]