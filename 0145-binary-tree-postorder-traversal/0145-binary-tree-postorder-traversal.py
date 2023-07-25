# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        curr=root
        while curr:
            if not curr.right:
                ans.append(curr.val)
                curr=curr.left
            else:
                prev=curr.right
                while prev.left and prev.left!=curr:
                    prev=prev.left
                if not prev.left:
                    prev.left=curr
                    ans.append(curr.val)
                    curr=curr.right
                else:
                    prev.left=None
                    curr=curr.left
        return ans[::-1]