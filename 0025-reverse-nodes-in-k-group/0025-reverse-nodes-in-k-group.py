# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next
        prev=ListNode(0)
        prev.next=head
        dummyHead=prev
        curr=None
        next=None
        if head==None or head.next==None:
            return head
        while count>=k:
            curr=prev.next
            next=curr.next
            for i in range(1, k):
                curr.next=next.next
                next.next=prev.next
                prev.next=next
                next=curr.next
            prev=curr
            count-=k
        return dummyHead.next
            
        