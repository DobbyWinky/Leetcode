/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getDecimalValue(head *ListNode) int {
    result:=head.Val
    node:=head
    for node.Next != nil {
        node = node.Next
        result = result * 2 + node.Val
    }
    return result
}