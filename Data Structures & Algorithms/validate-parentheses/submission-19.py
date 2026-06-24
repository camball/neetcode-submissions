class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []

        corresponding_braces = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        for brace in s:
            if brace in '([{':
                stack.append(brace)
                continue

            if brace in ')]}':
                if not stack:
                    return False

                if brace != corresponding_braces[stack.pop()]:
                    return False

        return not stack