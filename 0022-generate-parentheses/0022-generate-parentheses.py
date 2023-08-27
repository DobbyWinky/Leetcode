class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def dfs(openN, closeN, curr):
            if openN==closeN==n:
                ans.append(curr)
                return
            if openN<n:
                dfs(openN+1, closeN, curr+"(")
            if closeN<openN:
                dfs(openN, closeN+1, curr+")")
        dfs(0,0,"")
        return ans
            
        