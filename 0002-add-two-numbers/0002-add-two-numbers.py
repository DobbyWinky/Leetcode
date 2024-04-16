# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        node=ListNode(0)
        dummy=node
        while l1!=None and l2!=None:
            val=l1.val+l2.val+carry
            newNode=ListNode(val%10, None)
            carry=val//10
            l1=l1.next
            l2=l2.next
            node.next=newNode
            node=newNode
        while l1!=None:
            val=l1.val+carry
            newNode=ListNode(val%10, None)
            carry=val//10
            l1=l1.next
            node.next=newNode
            node=newNode
        while l2!=None:
            val=l2.val+carry
            newNode=ListNode(val%10, None)
            carry=val//10
            l2=l2.next
            node.next=newNode
            node=newNode
        if carry!=0:
            newNode=ListNode(carry, None)
            node.next=newNode
            node=newNode
        return dummy.next
        
        