func uniqueOccurrences(arr []int) bool {
    hash:=make(map[int]int)
    for _, a:=range arr {
        hash[a]++
    }
    uniq:=make(map[int]bool)
    for _, v:=range hash {
        if uniq[v] {
            return false
        }
        uniq[v]=true
    }
    return true
}