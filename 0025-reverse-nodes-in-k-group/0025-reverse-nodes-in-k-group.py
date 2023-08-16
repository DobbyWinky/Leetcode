# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        prev=dummy
        while count>=k:
            curr=prev.next
            next=curr.next
            for i in range(k-1):
                curr.next=next.next
                next.next=prev.next
                prev.next=next
                next=curr.next
                temp=dummy.next
            prev=curr
            count-=k
        return dummy.next
            
            
            
                
                
        