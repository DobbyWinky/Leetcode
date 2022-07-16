func arraysIntersection(arr1 []int, arr2 []int, arr3 []int) []int {
    hash:=make(map[int]int)
    for i:=0;i<len(arr1);i++ {
        hash[arr1[i]]++
    }
    for i:=0;i<len(arr2);i++ {
        hash[arr2[i]]++
    }
    for i:=0;i<len(arr3);i++ {
        hash[arr3[i]]++
    }
    ans:=make([]int, 0)
    for k,v:=range hash {
        if v==3 {
            ans=append(ans, k)
        }
    }
    sort.Ints(ans)
    return ans
}