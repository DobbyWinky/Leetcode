/*   Below is the interface for ImmutableListNode, which is already defined for you.
 *
 *   type ImmutableListNode struct {
 *       
 *   }
 *
 *   func (this *ImmutableListNode) getNext() ImmutableListNode {
 *		// return the next node.
 *   }
 *
 *   func (this *ImmutableListNode) printValue() {
 *		// print the value of this node.
 *   }
 */

// Time - O(n)
// Space - 1
func printLinkedListInReverse(head ImmutableListNode) {
    for head != nil {
        defer head.printValue()
        head = head.getNext()
    }
}