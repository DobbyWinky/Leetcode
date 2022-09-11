/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicatesUnsorted(head *ListNode) *ListNode {
    temp:=head
    duplicate:=make(map[int]int)
    for head!=nil {
        duplicate[head.Val]++
        head=head.Next
    }
    temp2:=new(ListNode)
    temp2.Next=temp
    temp=temp2
    if duplicate[temp2.Next.Val]>1 {
        temp2.Next=temp2.Next.Next
    }
    for temp2!=nil && temp2.Next!=nil{
        if duplicate[temp2.Next.Val]>1 {
            temp2.Next=temp2.Next.Next
        }else {
            temp2=temp2.Next
        }
    }
    return temp.Next
}