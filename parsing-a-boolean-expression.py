# Parsing A Boolean Expression

# A boolean expression is an expression that evaluates to either true or false. 
# It can be in one of the following shapes:

# 't' that evaluates to true.
# 'f' that evaluates to false.
# '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
# '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the 
# inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
# '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the 
# inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
# Given a string expression that represents a boolean expression, return the evaluation 
# of that expression.

# It is guaranteed that the given expression is valid and follows the given rules.

# Constraints:

# 1 <= expression.length <= 2 * 104
# expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.


def parse_bool_expr(expression) -> bool:
    stack = []

    for char in expression:
        if char == ")":
            # when we encounter a closing parenthesis we need to evaluate the sub expression
            operands = []
            
            # collect the operands inside the current expression (between "(" and ")" ) 
            while stack[-1] != "(":
                operands.append(stack.pop())

            # remove the "(" from the stack
            stack.pop()

            # the operator for this expression is just before "("
            operator = stack.pop()
                        
            # Perform the evaluation based on the operator 
            if operator == "!":
                # not operator requires all operands to be "t" to return "t"
                result = "f" if operands[0] == "t" else "t"
            elif operator == "&":
                # OR operator requires at least one operand to be "t" to return "t"
                result = "t" if any(op == "t" for op in operands) else "f"
            elif operator == "|":
                result = "t" if any(op == "t" for op in operands) else "f"

            # push the result of the evaluation back onto the stack
            stack.append(result)

        elif char != ",":
            # ignore commas and push everything onto the stack
            stack.append(char)
    
    return stack[0] == "t"


print(parse_bool_expr("&(|(f))"))