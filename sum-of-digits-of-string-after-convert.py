# Sum of Digits of String After Convert

# You are given a string s consisting of lowercase English letters, 
# and an integer k.

# First, convert s into an integer by replacing each letter with its 
# position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' 
# with 26). Then, transform the integer by replacing it with the sum of 
# its digits. Repeat the transform operation k times in total.

# For example, if s = "zbax" and k = 2, then the resulting integer would 
# be 8 by the following operations:

# Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
# Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
# Transform #2: 17 ➝ 1 + 7 ➝ 8
# Return the resulting integer after performing the operations described 
# above.


# Example 1:

# Input: s = "iiii", k = 1
# Output: 36
# Explanation: The operations are as follows:
# - Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
# - Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
# Thus the resulting integer is 36.

def get_lucky(s: str, k: int) -> int:
    # convert the string to a numeric string
    numeric_string = ''.join(str(ord(char) - ord("a") + 1) for char in s)

    # perform the transformation k times
    current_value = sum(int(digit) for digit in numeric_string)

    for _ in range(k - 1):
        current_value = sum(int(digit) for digit in str(current_value))

    return current_value


s = "iiii"
k = 1
result = get_lucky(s, k)
print(result)