# Range Sum of Sorted Subarray Sums
# You are given the array nums consisting of n positive integers. 
# You computed the sum of all non-empty continuous subarrays from 
# the array and then sorted them in non-decreasing order, creating 
# a new array of n * (n + 1) / 2 numbers.
# Return the sum of the numbers from index left to index right 
# (indexed from 1), inclusive, in the new array. Since the answer 
# can be a huge number return it modulo 109 + 7.

# Constraints:
# n == nums.length
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 100
# 1 <= left <= right <= n * (n + 1) / 2


class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        MOD = 10**9 + 7
        subarray_sums = []
        
        # Generate all subarray sums
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)
        
        # Sort the subarray sums
        # subarray_sums.sort()
        self.merge_sort(subarray_sums)
        
        # Compute the sum from left to right (1-based index)
        result_sum = 0
        for k in range(left-1, right):
            result_sum = (result_sum + subarray_sums[k]) % MOD
        
        return result_sum
    
    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        

solution = Solution()
nums = [1, 2, 3, 4]
n = 4
left = 1
right = 5
print(solution.rangeSum(nums, n, left, right)) 