class ListNode:
    
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.next=None
        self.prev= None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.head=ListNode(-1,-1)
        self.tail=ListNode(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.hash=collections.defaultdict(ListNode)
        self.capacity=capacity
        

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        else:
            node=self.hash[key]
            self.remove(node)
            self.add(node)
            return node.val       
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            old_node=self.hash[key]
            self.remove(old_node)
        
        node = ListNode(key, value)
        self.hash[key]=node
        self.add(node)
        
        if len(self.hash)>self.capacity:
            node_delete = self.head.next
            self.remove(node_delete)
            del self.hash[node_delete.key]
        
    def remove(self, node):
        node.next.prev=node.prev
        node.prev.next=node.next
        
    def add(self, node):
        prev_end=self.tail.prev
        prev_end.next=node
        node.prev=prev_end
        node.next=self.tail
        self.tail.prev=node
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)