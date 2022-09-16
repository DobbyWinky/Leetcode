/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
/*
Time - O(n)
Space - O(n)
*/
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    prev:=new(ListNode)
    newList:=prev
    for l1!=nil && l2!=nil {
        if l1.Val<l2.Val {
            prev.Next=l1
            l1=l1.Next
        }else {
            prev.Next=l2
            l2=l2.Next
        }
        prev=prev.Next
    }
    if l1!=nil {
        prev.Next=l1
    }else {
        prev.Next=l2
    }
    return newList.Next
}