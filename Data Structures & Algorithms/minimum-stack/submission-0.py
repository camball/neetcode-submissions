class MinStack:
    def __init__(self):
        self.stack: list[int] = []

        # We can't just store a single running min, because if we push a new min
        # onto the top of the stack, overwrite the running min, then immediately
        # pop that value, we'll have no way of knowing the old min.
        #
        # To solve this, we'll store the min for every stack depth. Whenever we
        # push a new value on, we'll write (or overwrite) that min to a hash
        # entry. The `mins` dictionary will be able to tell us the min value for
        # any stack depth.
        self.mins: dict[int, int] = dict()

    @property
    def depth(self) -> int:
        return len(self.stack)

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mins[self.depth] = min(val, self.mins.get(self.depth - 1, float("inf")))

    def pop(self) -> None:
        del self.mins[self.depth]
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[self.depth]
