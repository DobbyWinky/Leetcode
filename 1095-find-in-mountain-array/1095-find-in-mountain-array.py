# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Find Peak
        n=mountain_arr.length()
        lo=0
        hi=n-1
        while lo<hi:
            mid=(lo+hi)//2
            if mountain_arr.get(mid)<mountain_arr.get(mid+1):
                lo=mid+1
                peak=mid+1
            else:
                hi=mid
        
        #Search for first half
        lo=0
        hi=peak
        while lo<=hi:
            mid=(lo+hi)//2
            if mountain_arr.get(mid)==target:
                return mid
            if mountain_arr.get(mid)>target:
                hi=mid-1
            else:
                lo=mid+1
        
        # Search second half
        lo=peak+1
        hi=n-1
        while lo<=hi:
            mid=(lo+hi)//2
            if mountain_arr.get(mid)==target:
                return mid
            if mountain_arr.get(mid)>target:
                lo=mid+1
            else:
                hi=mid-1

        return -1
        