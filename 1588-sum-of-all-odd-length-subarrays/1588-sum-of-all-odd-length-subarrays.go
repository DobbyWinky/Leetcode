func sumOddLengthSubarrays(arr []int) int {
    result:=0
    n:=len(arr)
    for i:=0;i<n;i++ {
        start:=n-i
        end:=i+1
        total:=start*end
        odd:=total/2
        if total%2!=0 {
            odd++
        }
        result+=odd*arr[i]
    }
    return result
}