# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next==None:
            return True
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        curr=slow.next
        prev=None
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        slow.next=prev
        first=head
        second=prev
        while second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True
        