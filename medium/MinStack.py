class MinStack:
    """
    method: use tuple to store the elements and keep track of the minimum
    time: O(1) for each function called
    space: O(n), the cost of stack
    """
    def __init__(self):
        self.stack =[]

    def push(self, val: int) -> None:
        t = (val, val)
        if self.stack:
            smaller = min(val, self.stack[-1][1])
            self.stack.append((val, smaller))
        else:
            self.stack.append(t)
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0] 
        
    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()