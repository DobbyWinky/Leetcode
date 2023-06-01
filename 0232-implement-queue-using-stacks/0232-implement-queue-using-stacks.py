from collections import deque
class MyQueue:

    def __init__(self):
        self.stack_in=deque()
        self.stack_out=deque()
        

    def push(self, x: int) -> None:
        self.stack_in.append(x)
        

    def pop(self) -> int:
        if len(self.stack_out)!=0:
            return self.stack_out.pop()
        else:
            while len(self.stack_in)!=0:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        

    def peek(self) -> int:
        if len(self.stack_out)!=0:
            return self.stack_out[-1]
        else:
            while len(self.stack_in)!=0:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out[-1]
        

    def empty(self) -> bool:
        if len(self.stack_out)==0 and len(self.stack_in)==0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()