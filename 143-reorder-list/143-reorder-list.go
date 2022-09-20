/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reorderList(head *ListNode)  {
    slow:=head
    fast:=head
    for fast!=nil && fast.Next!=nil {
        slow=slow.Next
        fast=fast.Next.Next
    }
    curr:=slow.Next
    slow.Next=nil
    var prev *ListNode
    for curr!=nil {
        next:=curr.Next
        curr.Next=prev
        prev=curr
        curr=next
    }
    first:=head
    second:=prev
    for second!=nil {
        secondNext:=second.Next
        firstNext:=first.Next
        first.Next=second
        second.Next=firstNext
        first=firstNext
        second=secondNext
    }
    
}