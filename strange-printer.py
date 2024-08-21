# There is a strange printer with the following two special 
# properties:

# The printer can only print a sequence of the same character 
# each time.
# At each turn, the printer can print new characters starting 
# from and ending at any place and will cover the original 
# existing characters.
# Given a string s, return the minimum number of turns the 
# printer needed to print it.

# Example 1:

# Input: s = "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
# Example 2:

# Input: s = "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the 
# second place of the string, which will cover the existing 
# character 'a'.

# Constraints:

# 1 <= s.length <= 100
# s consists of lowercase English letters.


class Solution:
    def strange_printer(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
    
        for i in range(n):
            dp[i][i] = 1
    
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i][j-1] + 1
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
                if s[i] == s[j]:
                    dp[i][j] = min(dp[i][j], dp[i][j-1])
        
        return dp[0][n-1]
    

sample_string = "aaabbb"
strange_printer = Solution.strange_printer()
print(strange_printer(sample_string))