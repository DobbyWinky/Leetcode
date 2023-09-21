"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
        left=child
        right=next
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(head):
            curr=head
            tail=head
            while curr:
                next=curr.next
                child=curr.child
                if child:
                    tail2=dfs(child)
                    tail2.next=next
                    if next:
                        next.prev=tail2
                    curr.next=child
                    child.prev=curr
                    curr.child=None
                    curr=tail2
                else:
                    curr=next
                if curr:
                    tail=curr
            return tail
        if head:
            dfs(head)
        return head
                    
        