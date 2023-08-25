class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        ans=[]
        hash={"2":"abc", "3":"def", "4":"ghi","5":"jkl","6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def dfs(i, curr):
            if len(curr)==len(digits):
                ans.append(curr)
                return
            for dig in hash[digits[i]]:
                dfs(i+1, curr+dig)
        dfs(0, "")
        return ans
            