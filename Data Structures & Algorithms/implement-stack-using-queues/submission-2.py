from collections import deque

class MyStack:
    """
    We will use two queues to implement a stack.
    Invariant: one queue will be completely empty at the start and
               end of all operations.
    
    ---

    push 4, then 23, then 9

                    top of stack
                     |
    queue 1: [4, 23, 9]
    queue 2: []

    pop => push everything in the non-empty queue to the other queue,
           except the last element, which is returned instead.

    queue 1: []
    queue 2: [23, 9]
    return 4

    top => while we could implement very similarly to `pop`, we'll
           alternatively keep track of a "last pushed" value and update 
           it on every push/pop for O(1) lookup.

    queue 1: [23, 9]
    queue 2: []
    return 23

    empty => `not queue1 and not queue2`

    False
    """

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self.running_top: int | None = None

    def push(self, x: int) -> None:
        # Keep appending to the non-empty queue; default to queue1
        if not self.queue2:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

        self.running_top = x

    def pop(self) -> int:
        if not self.queue2:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.popleft())

            self.running_top = None if not self.queue2 else self.queue2[-1]

            return self.queue1.popleft()
        else:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.popleft())

            self.running_top = None if not self.queue1 else self.queue1[-1]

            return self.queue2.popleft()

    def top(self) -> int:
        return self.running_top

    def empty(self) -> bool:
        return not self.queue1 and not self.queue2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()