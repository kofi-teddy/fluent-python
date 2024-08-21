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


class StrangePrinter:
    def __init__(self, s: str):
        # Store the input string and its length
        self.s = s
        self.n = len(s)
        # Initialize a 2D DP array
        self.dp = [[0] * self.n for _ in range(self.n)]

    def calculate_min_turns(self):
        # Base case: A single character can be printed in one turn
        for i in range(self.n):
            self.dp[i][i] = 1
        
        # Consider substrings of increasing lengths starting from 2 to n
        for length in range(2, self.n + 1):
            for i in range(self.n - length + 1):
                # j is the end index of the current substring
                j = i + length - 1  
                
                # Assume we print the entire substring from i to j in one 
                # turn and then one more turn for the last character
                self.dp[i][j] = self.dp[i][j-1] + 1
                
                # Check all possible split points to see if we can reduce 
                # the number of turns by splitting the problem
                for k in range(i, j):
                    self.dp[i][j] = min(
                        self.dp[i][j], self.dp[i][k] + self.dp[k + 1][j]
                    )
                
                # If the first and last characters of the substring are the same,
                # we can print the substring from i to j in the same number of 
                # turns as dp[i][j-1].
                if self.s[i] == self.s[j]:
                    self.dp[i][j] = min(self.dp[i][j], self.dp[i][j-1])
        
        # The answer for the entire string is stored in dp[0][n-1]
        return self.dp[0][self.n - 1]


# Example usage:
s = "aba"
printer = StrangePrinter(s)
print(printer.calculate_min_turns())  
# Output: 2