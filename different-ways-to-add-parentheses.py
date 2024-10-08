# Given a string expression of numbers and operators, return all 
# possible results from computing all the different possible ways 
# to group numbers and operators. You may return the answer in any 
# order.

# The test cases are generated such that the output values fit in 
# a 32-bit integer and the number of different results does not 
# exceed 104.

 
# Example 1:
# Input: expression = "2-1-1"
# Output: [0,2]
# Explanation:
# ((2-1)-1) = 0 
# (2-(1-1)) = 2

# Example 2:
# Input: expression = "2*3-4*5"
# Output: [-34,-14,-10,-10,10]
# Explanation:
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
 

# Constraints:
# 1 <= expression.length <= 20
# expression consists of digits and the operator '+', '-', and '*'.
# All the integer values in the input expression are in the range 
# [0, 99].
# The integer values in the input expression do not have a leading 
# '-' or '+' denoting the sign.


def diff_ways_to_compute(expression):
    memo = {}

    def compute(left, right, op):
        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
    
    def ways(expression):
        if expression.isdigit():
            return [int(expression)]
        
        if expression in memo:
            return memo[expression]
        
        results = []
        for i, char in enumerate(expression):
            if char in "+-*":
                left_results = ways(expression[:i])
                right_results = ways(expression[i+1:])

                for left in left_results:
                    for right in right_results:
                        results.append(compute(left, right, char))

        memo[expression] = results
        return results 

    return ways(expression)       


expression1 = "2*3-4*5"
print(diff_ways_to_compute(expression1))