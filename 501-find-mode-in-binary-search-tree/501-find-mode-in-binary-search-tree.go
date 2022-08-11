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
Space - O(n - Stack space only - No extra mem)
*/
func findMode(root *TreeNode) []int {
    prev:=-100001
    ans:=make([]int, 0)
    count:=1
    maxCount:=0
    var helper func(root *TreeNode)
    helper=func(root *TreeNode) {
        if root==nil {
            return
        }
        helper(root.Left)
        if prev!=-100001 {
            if root.Val==prev {
                count++
            }else {
                count=1
            }
        }
        if count>maxCount {
            ans=ans[:0]
            maxCount=count
            ans=append(ans, root.Val)
        }else if count==maxCount {
            ans=append(ans, root.Val)
        }
        prev=root.Val
        helper(root.Right)
    }
    helper(root)
    return ans
}