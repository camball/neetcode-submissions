class MyQueue:

    def __init__(self):
        self.enqueue_stack: list[int] = []
        self.dequeue_stack: list[int] = []

    def push(self, x: int) -> None:
        self.enqueue_stack.append(x)

    def pop(self) -> int:
        if self.dequeue_stack:
            return self.dequeue_stack.pop()
        else:
            for _ in range(len(self.enqueue_stack) - 1):
                self.dequeue_stack.append(self.enqueue_stack.pop())

            return self.enqueue_stack.pop()

    def peek(self) -> int:
        if self.dequeue_stack:
            return self.dequeue_stack[-1]
        else:
            for _ in range(len(self.enqueue_stack)):
                self.dequeue_stack.append(self.enqueue_stack.pop())

            return self.dequeue_stack[-1]
        

    def empty(self) -> bool:
        return not self.enqueue_stack and not self.dequeue_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()