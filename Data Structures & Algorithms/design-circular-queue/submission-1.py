class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None]*k
        self.head = 0
        self.tail = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.count == len(self.queue):
            return False
        idx = self.tail % len(self.queue)
        self.queue[idx] = value
        self.tail += 1
        self.count += 1
        print(self.queue, self.head, self.tail)
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.head += 1
        self.count -= 1
        print(self.queue, self.head, self.tail)
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        idx = self.head % len(self.queue)
        print(self.queue, self.head, self.tail)
        return self.queue[idx]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        idx = (self.tail-1) % len(self.queue)
        print(self.queue, self.head, self.tail)
        return self.queue[idx]

    def isEmpty(self) -> bool:
        print(self.queue, self.head, self.tail)
        return self.count == 0

    def isFull(self) -> bool:
        print(self.queue, self.head, self.tail)
        return self.count == len(self.queue)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()