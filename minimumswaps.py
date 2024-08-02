# A swap is defined as taking two distinct positions in an array 
# and swapping the values in them.

# A circular array is defined as an array where we consider the 
# first element and the last element to be adjacent.

# Given a binary circular array nums, return the minimum number 
# of swaps required to group all 1's present in the array together 
# at any location.

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

# Example 1:

# Input: nums = [0,1,0,1,1,0,0]
# Output: 1
# Explanation: Here are a few of the ways to group all the 
# 1's together:
# [0,0,1,1,1,0,0] using 1 swap.
# [0,1,1,1,0,0,0] using 1 swap.
# [1,1,0,0,0,0,1] using 2 swaps (using the circular property 
# of the array).
# There is no way to group all 1's together with 0 swaps.
# Thus, the minimum number of swaps required is 1.

class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalOnes = sum(nums)
        if totalOnes == 0:
            return 0
        
        n = len(nums)
        maxOnesInWindow = 0
        currentOnesInWindow = 0
        
        # Initial window
        for i in range(totalOnes):
            if nums[i] == 1:
                currentOnesInWindow += 1
        
        maxOnesInWindow = currentOnesInWindow
        
        # Slide the window across the array
        for i in range(1, n):
            if nums[i - 1] == 1:
                currentOnesInWindow -= 1
            if nums[(i + totalOnes - 1) % n] == 1:
                currentOnesInWindow += 1
            
            maxOnesInWindow = max(maxOnesInWindow, currentOnesInWindow)
        
        return totalOnes - maxOnesInWindow


nums = [0, 1, 0, 1, 1, 0, 0]
solution = Solution()
print(solution.minSwaps(nums))