/*
Time - O(n)
Space - O(1)
*/
func hammingDistance(x int, y int) int {
    res:=x^y
    count:=0
    for res>0 {
        if res%2==1 {
            count++
        }
        res/=2
    }
    return count
}