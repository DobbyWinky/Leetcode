func sortByBits(arr []int) []int {
    sort.Slice(arr, func(i,j int) bool {
        if count(arr[i])<count(arr[j]) {
            return true
        } 
        if count(arr[i]) == count(arr[j]) {
            return arr[i]<arr[j]
        }
        return false
    })
    return arr
}
            
func count(num int) int {
    c:=0
    for num!=0 {
        if num%2==1 {
            c++
        }
        num/=2
    }
    return c
}
