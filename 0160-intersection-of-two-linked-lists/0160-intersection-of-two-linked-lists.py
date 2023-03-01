# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash=set()
        while headA!=None:
            hash.add(headA)
            headA=headA.next
        while headB!=None:
            if headB in hash:
                return headB
            headB=headB.next
        return None
        