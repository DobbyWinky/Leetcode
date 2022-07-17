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
// Space - O(n)
func printLinkedListInReverse(head ImmutableListNode) {
    var helper func(head ImmutableListNode)
    helper = func (head ImmutableListNode) {
        if head==nil {
            return
        }
        helper(head.getNext())
        head.printValue()
    }
    helper(head)
}