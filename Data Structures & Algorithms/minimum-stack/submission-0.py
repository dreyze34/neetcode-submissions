class MinStack:

    def __init__(self):
        self.minS = []
        self.mainS = []

    def push(self, val: int) -> None:
        if not self.minS:
            self.mainS.append(val)
            self.minS.append(val)
        else:
            self.mainS.append(val)
            self.minS.append(min(val, self.minS[-1]))

    def pop(self) -> None:
        self.mainS.pop()
        self.minS.pop()

    def top(self) -> int:
        return self.mainS[-1]

    def getMin(self) -> int:
        return self.minS[-1]
        
