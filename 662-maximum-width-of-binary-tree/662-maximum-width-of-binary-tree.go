/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type BFSNode struct {
    node *TreeNode
    index int
}
func widthOfBinaryTree(root *TreeNode) int {
    max:=1
    queue:=make([]BFSNode, 0)
    queue=append(queue, BFSNode{root, 1})
    for len(queue)>0 {
        size:=len(queue)
        if queue[len(queue)-1].index-queue[0].index+1>max {
            max=queue[len(queue)-1].index-queue[0].index+1
        }
        for size>0 {
            pop:=queue[0]
            queue=queue[1:]
            if pop.node.Left!=nil {
                queue=append(queue, BFSNode{pop.node.Left, 2*pop.index})
            }
            if pop.node.Right!=nil {
                queue=append(queue, BFSNode{pop.node.Right, 2*pop.index+1})
            }
            size--
        }
    }
    return max
}