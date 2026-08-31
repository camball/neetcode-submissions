# Note: This question was done on LeetCode, not NeetCode, as NeetCode
# doesn't have this question. As such, manually adding my solutions
# to this repo for posterity.

class Solution:
    def calculate(self, s: str) -> int:
        num = 0  # For building string parsing
        additive = []  # Stack of additive terms

        # This algo relies on applying the previous operator to the last-extracted
        # number(s). Initialising the first operator to '+' is the same as saying
        # to always add the first term to the stack. Conceptually, "2-3" is the same
        # as "+2-3" here.
        operator = "+"

        for idx, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)
            
            # If we encounter an operator, or we're on the very last operand,
            # flush + reset `num`, apply the previous operator, and save the
            # current operator.
            if char in "+-*/" or idx == len(s) - 1:
                if operator == "+":
                    additive.append(num)
                elif operator == "-":
                    additive.append(-num)
                elif operator == "*":
                    additive.append(additive.pop() * num)
                elif operator == "/":
                    additive.append(int(additive.pop() / num))

                operator = char
                num = 0
            
        return sum(additive)
