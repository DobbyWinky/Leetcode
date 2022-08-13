func countOdds(lo int, hi int) int {
    if lo%2==0 && hi%2==0 {
        return (hi-lo)/2
    }
    return (hi-lo)/2+1
}