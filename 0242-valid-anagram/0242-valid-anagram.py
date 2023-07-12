class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash=collections.defaultdict(int)
        for s1 in s:
            hash[s1]+=1
        for t1 in t:
            if t1 not in hash:
                return False
            hash[t1]-=1
        for k in hash:
            if hash[k]!=0:
                return False
        return True
        