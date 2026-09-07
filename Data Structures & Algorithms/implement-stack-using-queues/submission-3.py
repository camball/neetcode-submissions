from collections import deque

class MyStack:
    """
    We'll use one queue and rotate its values, which simplifies the
    implementation significantly.
    """

    def __init__(self):
        self.queue = deque()
        

    def push(self, x: int) -> None:
        """
        push(3), push(6), push(14)

        appends from the right:
        => [3, 6, 14]
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        rotate len(queue) - 1 times
        len(queue) == 3, so rotate twice:
        1. [6, 14, 3]
        2. [14, 3, 6]
        then return popleft()
        => 14

        [3, 6]
        """
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return not len(self.queue)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()