from collections import deque
class MyStack:

    def __init__(self):
        self.queue=deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        n=len(self.queue)
        for i in range(0, n-1):
            self.queue.append(self.queue.popleft())
        

    def pop(self) -> int:
        return self.queue.popleft()
        

    def top(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        if len(self.queue)==0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()