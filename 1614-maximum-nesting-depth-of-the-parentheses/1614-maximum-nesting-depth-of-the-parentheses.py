class Solution:
    def maxDepth(self, s: str) -> int:
        open=0
        level=0
        for c in s:
            if c=='(':
                open+=1
            if c==')':
                level=max(level, open)
                open-=1
        return level
        