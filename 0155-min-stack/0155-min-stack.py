class MinStack:

    def __init__(self):
        self.stack=[]
        self.min=float('inf')
        

    def push(self, val: int) -> None:
        if len(self.stack)==0:
            self.stack.append(val)
            self.min=val
            return
        if val<self.min:
            self.stack.append(2*val-self.min)
            self.min=val
        else:
            self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack[-1]<=self.min:
            self.min=2*self.min-self.stack[-1]
            self.stack.pop()
        else:
            self.stack.pop()
        if len(self.stack)==0:
            self.min=float(-inf)

    def top(self) -> int:
        if self.stack[-1]<self.min:
            return self.min
        else:
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()