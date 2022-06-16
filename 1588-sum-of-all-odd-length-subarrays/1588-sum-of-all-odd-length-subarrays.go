func sumOddLengthSubarrays(arr []int) int {
    sum:=0
    for i:=0;i<len(arr);i++ {
        for j:=i+1;j<=len(arr);j++ {
            n:=len(arr[i:j])
            if n%2!=0 {
                for k:=0;k<n;k++ {
                    sum+=arr[i:j][k]
                }
            }
        }
    }
    return sum
}