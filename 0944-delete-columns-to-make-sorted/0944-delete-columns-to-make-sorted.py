class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        i=0
        n=len(strs[0])
        m=len(strs)
        count=0
        while i<n:
            j=0
            while j<m-1:
                if strs[j][i]>strs[j+1][i]:
                    count+=1
                    break
                j+=1
            i+=1
        return count
        