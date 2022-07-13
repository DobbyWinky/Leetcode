/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
    if root==nil {
        return nil
    }
    queue:=make([]*TreeNode, 0)
    queue=append(queue, root)
    ans:=make([][]int, 0)
    for len(queue)>0 {
        size:=len(queue)
        res:=make([]int, 0)
        for size>0 {
            pop:=queue[0]
            queue=queue[1:]
            res=append(res, pop.Val)
            if pop.Left!=nil {
                queue=append(queue, pop.Left)
            }
            if pop.Right!=nil {
                queue=append(queue, pop.Right)
            }
            size--
        }
        ans=append(ans, res)
    }
    return ans
}