/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/*
Time - O(n)
Space - O(n)
*/
func max(i,j int) int {
    if i>j {
        return i
    }
    return j
}
func maxDepth(root *TreeNode) int {
    if root==nil {
        return 0
    }
    return max(maxDepth(root.Left), maxDepth(root.Right))+1
}