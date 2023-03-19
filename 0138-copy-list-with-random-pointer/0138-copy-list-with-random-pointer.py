"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return None
        hash=collections.defaultdict(Node)
        temp=head
        while temp!=None:
            newNode=Node(temp.val, None, None)
            hash[temp]=newNode
            temp=temp.next
        temp=head
        while temp!=None:
            if temp.next!=None:
                hash[temp].next=hash[temp.next]
            if temp.random!=None:
                hash[temp].random=hash[temp.random]
            temp=temp.next
        return hash[head]
                
        