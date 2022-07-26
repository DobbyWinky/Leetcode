/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func evaluateTree(root *TreeNode) bool {
    var helper func(root *TreeNode) bool
    helper = func(root *TreeNode) bool{
        switch root.Val {
            case 0: return false
            case 1: return true
            case 2: return helper(root.Left) || helper(root.Right)
            case 3: return helper(root.Left) && helper(root.Right)
            default: return false
        }
    }
    return helper(root)
}