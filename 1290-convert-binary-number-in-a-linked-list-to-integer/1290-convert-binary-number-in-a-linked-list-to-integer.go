/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getDecimalValue(head *ListNode) int {
    temp:=head
    count:=0.0
    for temp!=nil {
        count++
        temp=temp.Next
    }
    ans:=0
    for head!=nil {
        count--
        ans+=head.Val*int(math.Pow(2, count))
        head=head.Next
    }
    return ans
}