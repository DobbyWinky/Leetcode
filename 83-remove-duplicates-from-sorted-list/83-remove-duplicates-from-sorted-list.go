/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    temp:=head
    for temp!=nil && temp.Next!=nil {
        if temp.Val ==temp.Next.Val {
            temp.Next=temp.Next.Next
        }else {
            temp=temp.Next
        }
    }
    
    return head
}