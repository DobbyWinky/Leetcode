/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sortedArrayToBST(nums []int) *TreeNode {
    if len(nums)==0 {
        return nil
    }
    newNode:=new(TreeNode)
    mid:=len(nums)/2
    newNode.Val=nums[mid]
    newNode.Left=sortedArrayToBST(nums[:mid])
    newNode.Right=sortedArrayToBST(nums[mid+1:])
    return newNode
}