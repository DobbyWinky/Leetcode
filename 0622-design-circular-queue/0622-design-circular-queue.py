class MyCircularQueue:

    def __init__(self, k: int):
        self.queue=[-1]*k
        self.front=-1
        self.rear=-1
        self.len=k
        self.count=0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.rear==-1 and self.front==-1:
            self.front+=1
            self.rear+=1
        else:
            self.rear+=1
        self.queue[self.rear%self.len]=value
        self.count+=1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.front%self.len]=-1
        self.front+=1
        self.count-=1
        return True
        
        

    def Front(self) -> int:
        return self.queue[self.front%self.len]
        

    def Rear(self) -> int:
        return self.queue[self.rear%self.len]
        

    def isEmpty(self) -> bool:
        if self.count==0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.count==self.len:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()