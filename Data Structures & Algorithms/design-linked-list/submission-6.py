class ListNode:
    def __init__(self, val: int | None, prev: ListNode | None = None, next: ListNode | None = None):
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        prev_val = None if not self.prev else self.prev.val
        next_val = None if not self.next else self.next.val
        return f"val = {self.val}, prev = {prev_val}, next = {next_val}"


class MyLinkedList:
    def __init__(self):
        self.length: int = 0
        self.head = None
        self.tail = None

    def __len__(self) -> int:
        return self.length

    def __str__(self) -> str:
        current = self.head
        output = []

        while current:
            output.append(current.val)
            current = current.next

        return str(output)

    def get(self, index: int) -> int:
        if index == 0:
            return self.head.val

        if index == len(self) - 1:
            return self.tail.val

        if index >= len(self) or index < 0:
            return -1

        # Start traversing at whichever side is closest to the
        # destination node, to slightly optimise runtime
        if index > (len(self) - 1) // 2:  # Traverse from tail, backwards
            current = self.tail
            for _ in range(len(self) - index - 1):
                current = current.prev
            return current.val
        else:  # Traverse from head, forwards
            current = self.head
            for _ in range(index):
                current = current.next
            return current.val

    def addAtHead(self, val: int) -> None:
        self.length += 1

        if not self.head:  # List has not been initialised yet
            self.head = ListNode(val)
            self.tail = self.head
        else:
            self.head.prev = ListNode(val, prev=None, next=self.head)
            self.head = self.head.prev

    def addAtTail(self, val: int) -> None:
        self.length += 1

        if not self.head:  # List has not been initialised yet
            self.head = ListNode(val)
            self.tail = self.head
        else:
            self.tail.next = ListNode(val, prev=self.tail, next=None)
            self.tail = self.tail.next

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        if index == len(self):
            self.addAtTail(val)
            return

        # Start traversing at whichever side is closest to the
        # destination node, to slightly optimise runtime
        if index > (len(self) - 1) // 2:  # Traverse from tail, backwards
            current = self.tail
            for _ in range(len(self) - index - 1):
                current = current.prev

            new_node = ListNode(val=val, prev=current.prev, next=current)
            current.prev.next = new_node
            current.prev = new_node

        else:  # Traverse from head, forwards
            current = self.head
            for _ in range(index):
                current = current.next

            new_node = ListNode(val=val, prev=current.prev, next=current)
            current.prev.next = new_node
            current.prev = new_node

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= len(self) or index < 0:
            return

        # Start traversing at whichever side is closest to the
        # destination node, to slightly optimise runtime
        if index > (len(self) - 1) // 2:  # Traverse from tail, backwards
            current = self.tail
            for _ in range(len(self) - index - 1):
                current = current.prev

            if current.prev and current.next:
                current.prev.next = current.next
                current.next.prev = current.prev
            elif current.prev:
                current.prev.next = None
                self.tail = current.prev
            else:  # current.next is not None and current.prev is None
                current.next.prev = None
                self.head = current.next

        else:  # Traverse from head, forwards
            current = self.head
            for _ in range(index):
                current = current.next

            if current.prev and current.next:
                current.prev.next = current.next
                current.next.prev = current.prev
            elif current.prev:
                current.prev.next = None
                self.tail = current.prev
            else:  # current.next is not None and current.prev is None
                current.next.prev = None
                self.head = current.next

        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
