# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=[]
        queue.append([root,0,0])
        ans=OrderedDict()
        ansVal =[]
        while len(queue)>0:
            size=len(queue)
            while size>0:
                pop=queue.pop(0)
                val = pop[0].val
                col = pop[1]
                level=pop[2]
                if col not in ans:
                    ans[col]=OrderedDict()
                if level not in ans[col]:
                    ans[col][level]=[]
                ans[col][level].append(val)
                ans[col][level].sort()
                if pop[0].left!=None:
                    queue.append([pop[0].left, pop[1]-1, pop[2]+1])
                if pop[0].right!=None:
                    queue.append([pop[0].right, pop[1]+1, pop[2]+1])
                size-=1
        ansVal=[]
        for k, v in sorted(ans.items()):
            ans2=[]
            for k1,v1 in v.items():
                for x in v1:
                    ans2.append(x)
            ansVal.append(ans2)
        return ansVal
        
        