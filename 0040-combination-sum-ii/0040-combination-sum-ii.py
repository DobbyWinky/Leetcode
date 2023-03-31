class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        def helper(idx, curr, currArr):
            if curr==target:
                temp=currArr[:]
                ans.append(temp)
                return
            if curr>target:
                return
            prev=-1
            for i in range(idx, len(candidates)):
                if candidates[i]==prev:
                    continue
                currArr.append(candidates[i])
                helper(i+1, curr+candidates[i], currArr)
                currArr.pop()
                prev=candidates[i]
        helper(0,0,[])
        return ans