/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func findMode(root *TreeNode) []int {
    freq:=make(map[int]int)
    var helper func(root *TreeNode)
    helper=func(root *TreeNode) {
        if root==nil {
            return
        }
        helper(root.Left)
        freq[root.Val]++
        helper(root.Right)
    }
    helper(root)
    maxFreq:=0
    for _,v:=range freq {
        if v>maxFreq {
            maxFreq=v
        }
    }
    
    ans:=make([]int, 0)
    for k,v:=range freq {
        if v==maxFreq {
            ans=append(ans, k)
        }
    }
    return ans
}