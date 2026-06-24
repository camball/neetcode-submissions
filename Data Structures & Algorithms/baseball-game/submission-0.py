class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Conceptually, `scores` is a stack here
        scores: list[int] = []

        for op in operations:
            match op:
                case "C":
                    scores.pop()
                case "D":
                    try:
                        scores.append(scores[-1] * 2)
                    except IndexError:
                        pass  # `scores` is empty
                case "+":
                    try:
                        scores.append(scores[-1] + scores[-2])
                    except IndexError:
                        pass  # `scores` is empty or only has one element
                case _:  # Number
                    scores.append(int(op))

        return sum(scores)