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
    for i:=1;i<=n+1;i++ {
        first=first.Next
    }
    for first!=nil {
        first=first.Next
        second=second.Next
    }
    if second.Next!=nil {
        second.Next=second.Next.Next
    }else {
        second.Next=nil
    }
    return dummy.Next
}