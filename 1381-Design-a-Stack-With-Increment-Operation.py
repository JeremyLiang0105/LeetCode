class CustomStack:

    def __init__(self, maxSize: int):
        self.cap = maxSize
        self.stack = []
        self.increments = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.cap:
            self.stack.append(x)
            self.increments.append(0)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        lastIncrement = self.increments.pop()
        if self.increments:
            self.increments[-1] += lastIncrement
        return self.stack.pop() + lastIncrement
    
    def increment(self, k: int, val: int) -> None:
        if 0 < len(self.stack) < k:
            self.increments[-1] += val
        elif len(self.stack) >= k:
            self.increments[k - 1] += val
     
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
