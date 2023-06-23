# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        def isCelebrity(celebrity):
            for j in range(n):
                if celebrity==j:
                    continue
                if knows(celebrity, j) or not knows(j, celebrity):
                    return False
            return True
        celebrity=-1
        for i in range(0, n):
            if knows(celebrity, i):
                celebrity=i
        if isCelebrity(celebrity):
            return celebrity
        return -1
        