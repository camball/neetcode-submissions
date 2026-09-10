class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Monotonic stack: every element stays consistently increasing or
        decreasing according to some value.

        Is top of stack the biggest or smallest local temp for this problem?

        Since warmer means "higher number", if we ever see a higher number
        than the top of the stack as we iterate, we'll need to deal with the
        items in the stack immediately then. This implies the top of the stack
        should be the smallest element in the stack, and increase toward the
        bottom of the stack.

        We iterate through temperatures, and if we see a higher number than
        the top of the stack, we pop the stack and write to the result array
        for that popped value's index.

        So what are we storing in the stack, values or indices? Via pointer
        arithmetic, it seems like we should store indices that way we don't
        have to do weird backwards calculation logic to figure out how far
        down in the stack we are. We can just look up the value from
        `temperatures` via index when needed.
        """

        # Default `result[i]` is zero, so initialise to that and overwrite
        result = [0] * len(temperatures)

        stack: list[int] = []

        for i in range(len(temperatures)):
            if not stack or temperatures[i] < temperatures[stack[-1]]:
                # We encountered a day as cool as or cooler than the last
                stack.append(i)
            else:
                # We encountered a warmer day than the last
                while stack and temperatures[stack[-1]] < temperatures[i]:
                    distance = stack.pop()
                    result[distance] = i - distance

                stack.append(i)

        return result