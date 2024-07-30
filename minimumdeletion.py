# You are given a string s consisting only of characters 'a' and 'b'​​​​.

# You can delete any number of characters in s to make s balanced. s is 
# balanced if there is no pair of indices (i,j) such that i < j 
# and s[i] = 'b' and s[j]= 'a'.

# Return the minimum number of deletions needed to make s balanced.

# Constraints:

# 1 <= s.length <= 105
# s[i] is 'a' or 'b'​​.


# class Solution(object):
#     def minimumDeletions(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         n = len(s)
        
#         # Count the total number of 'a's and 'b's
#         total_a = s.count('a')
#         total_b = s.count('b')
        
#         # Initialize prefix and suffix deletion counters
#         prefix_b = 0
#         suffix_a = total_a
        
#         # Initialize minimum deletions to a large number
#         min_deletions = float('inf')
        
#         # Iterate through the string
#         for i in range(n + 1):
#             # The total deletions to balance at position i is the sum of
#             # 'b's in the prefix and 'a's in the suffix
#             min_deletions = min(min_deletions, prefix_b + suffix_a)
            
#             # Update prefix_b and suffix_a for the next position
#             if i < n:
#                 if s[i] == 'a':
#                     suffix_a -= 1
#                 else:  # s[i] == 'b'
#                     prefix_b += 1
        
#         return min_deletions


class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        
        # Count the total number of 'a's and 'b's
        total_a = s.count('a')
        total_b = s.count('b')
        
        # Initialize prefix and suffix deletion counters
        prefix_b = 0
        suffix_a = total_a
        
        # Initialize minimum deletions to a large number
        min_deletions = float('inf')
        
        # Iterate through the string
        for i in range(n + 1):
            # Calculate deletions needed at this position
            current_deletions = prefix_b + suffix_a
            
            # Update min_deletions without using min()
            if current_deletions < min_deletions:
                min_deletions = current_deletions
            
            # Update prefix_b and suffix_a for the next position
            if i < n:
                if s[i] == 'a':
                    suffix_a -= 1
                else:  # s[i] == 'b'
                    prefix_b += 1
        
        return min_deletions