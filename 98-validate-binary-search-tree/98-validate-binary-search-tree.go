/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
    var helper func(root *TreeNode, min, max int) bool
    helper=func(root *TreeNode, min, max int) bool{
        if root==nil {
            return true
        }
        if root.Val<=min || root.Val>=max {
            return false
        }
        return helper(root.Left, min, root.Val)&&helper(root.Right, root.Val, max)
        
    }
    return helper(root, -2147483649, 2147483648)
}