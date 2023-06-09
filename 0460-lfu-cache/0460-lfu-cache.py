class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.val=value
        self.next=next
        self.prev=prev

class LinkedList:
    def __init__(self):
        self.head=ListNode(-1)
        self.tail=ListNode(-1,self.head)
        self.head.next=self.tail
        self.map={}
        
    def length(self):
        return len(self.map)
    
    def pushRight(self, val):
        node=ListNode(val, self.tail.prev, self.tail)
        self.tail.prev=node
        node.prev.next=node
        self.map[val]=node
    
    def pop(self, val):
        if val in self.map:
            node=self.map[val]
            prev, next=node.prev, node.next
            prev.next=next
            next.prev=prev
            self.map.pop(val, None)
    
    def popLeft(self):
        res=self.head.next.val
        self.pop(self.head.next.val)
        return res
    
    def update(self, val):
        self.pop(val)
        self.pushRight(val)
            
class LFUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.lfuCnt = 0
        self.valMap={}
        self.countMap=collections.defaultdict(int)
        self.listMap=collections.defaultdict(LinkedList)
        
    def counter(self, key):
        cnt=self.countMap[key]
        self.countMap[key]+=1
        self.listMap[cnt].pop(key)
        self.listMap[cnt+1].pushRight(key)
        if cnt == self.lfuCnt and self.listMap[cnt].length()==0:
            self.lfuCnt+=1
        
        

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]
        
        

    def put(self, key: int, value: int) -> None:
        if self.cap==0:
            return
        if key not in self.valMap and len(self.valMap) == self.cap:
            res=self.listMap[self.lfuCnt].popLeft()
            self.valMap.pop(res)
            self.countMap.pop(res)
        self.valMap[key]=value
        self.counter(key)
        self.lfuCnt=min(self.lfuCnt, self.countMap[key])
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)