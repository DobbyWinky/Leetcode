class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min=99999
        ans=[]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]<min:
                min=arr[i+1]-arr[i]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==min:
                ans.append([arr[i],arr[i+1]])
        return ans
        