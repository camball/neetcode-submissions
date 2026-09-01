class Solution:
    def calculate(self, s: str) -> int:
        """
        ## General algorithm framing:

        We parse tokens and evaluate (at the same time) from left to right in one
        pass. Multiplication and division are evaluated immediately, whereas
        subtraction (converted to adding a negative) and addition are stored and
        summed at the end.

        ## Helpful tricks

        Even though we are iterating over tokens from left to right, it is easier
        to evaluate the previous three operations all at once instead of looking
        forward and reading the current number (lhs) and evaluating the next token
        (operator) and next number (rhs). By saving the operation that needs to happen
        and dealing with it in retrospect, we don't need to do any weird tricks for
        modifying the input character array we are iterating over (i.e., rewriting
        a range of characters to be the result of a multiplication or division
        evaluation).

        In short, this looks like:

        - Encounter an operator? Save it.
        - Encounter a number? We now have enough info to evaluate the prev operator

        ## Important notes

        - We leverage how subtraction is the same as adding a negative number.
        - All the input numbers are non-negative integers, so although we may need to
          produce a negative result, we don't need to worry about parsing negatives.
        - We don't worry about parenthesis or grouping at all. Multiplication and
          division can be evaluated instantly from left to right.
        """

        lhs: int | None = None
        add: list[int] = list()
        number_buffer = []
        pending_operator: str | None = None

        for char in s:
            if char.isdigit():  # Simply build the current number
                number_buffer.append(char)
            elif char != " " and pending_operator:
                rhs = int("".join(number_buffer))
                number_buffer = []

                if pending_operator == "*":
                    lhs = lhs * rhs
                elif pending_operator == "/":
                    lhs = int(lhs / rhs)
                elif pending_operator == "-":
                    add.append(lhs)  # "All ints in the expr. are non-negative"
                    lhs = -rhs
                elif pending_operator == "+":
                    add.append(lhs)
                    lhs = rhs

                pending_operator = char
            elif char != " ":
                if number_buffer:  # Flush + reset
                    lhs = int("".join(number_buffer))
                    number_buffer = []

                pending_operator = char

        rhs = int("".join(number_buffer))

        if not pending_operator:  # Handle case of no operators in expression
            return rhs

        # Deal with final term
        if pending_operator == "*":
            add.append(lhs * rhs)
        elif pending_operator == "/":
            add.append(int(lhs / rhs))
        elif pending_operator == "-":
            add.append(lhs - rhs)
        elif pending_operator == "+":
            add.append(lhs + rhs)

        return sum(add)
