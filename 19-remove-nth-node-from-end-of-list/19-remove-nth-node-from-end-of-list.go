/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    dummy:=new(ListNode)
    dummy.Next=head
    first:=dummy
    second:=dummy
    for n>=0 {
        first=first.Next
        n--
    }
    for first!=nil {
        first=first.Next
        second=second.Next
    }
    second.Next=second.Next.Next
    return dummy.Next
}