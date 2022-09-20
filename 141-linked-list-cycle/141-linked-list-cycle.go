/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
    if head==nil {
        return false
    }
    fast:=head.Next
    slow:=head
    for fast!=nil && fast.Next!=nil {
        if slow==fast {
            return true
        }
        slow=slow.Next
        fast=fast.Next.Next
    }
    return false
}