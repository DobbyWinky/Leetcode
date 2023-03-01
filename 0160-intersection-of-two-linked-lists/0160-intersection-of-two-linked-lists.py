# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA=headA
        tempB=headB
        while tempA!=tempB:
            tempA=headB if tempA==None else tempA.next
            tempB=headA if tempB==None else tempB.next
        return tempA
            
        