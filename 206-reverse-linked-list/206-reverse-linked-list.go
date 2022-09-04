/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
/*
Time - O(n)
Space - O(1)
*/
func reverseList(head *ListNode) *ListNode {
    curr:=head
    var prev *ListNode
    for curr!=nil {
        next:=curr.Next
        curr.Next=prev
        prev=curr
        curr=next
    }
    return prev
}