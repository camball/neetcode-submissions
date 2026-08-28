from math import floor, ceil

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                match token:
                    case "+":
                        operand_1 = stack.pop()
                        operand_2 = stack.pop()
                        stack.append(operand_1 + operand_2)
                    case "-":
                        operand_1 = stack.pop()
                        operand_2 = stack.pop()
                        stack.append(operand_2 - operand_1)
                    case "*":
                        operand_1 = stack.pop()
                        operand_2 = stack.pop()
                        stack.append(operand_1 * operand_2)
                    case "/":
                        operand_1 = stack.pop()
                        operand_2 = stack.pop()
                        raw = operand_2 / operand_1

                        # Always round in the direction closest to zero
                        toward_zero = ceil(raw) if raw < 0 else floor(raw)

                        stack.append(toward_zero)
            else:
                stack.append(int(token))

        return stack.pop()
