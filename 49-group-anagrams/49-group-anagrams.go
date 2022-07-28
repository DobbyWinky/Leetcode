/*
L - Length of each string
N - Number of strings
Time - O(N*L)
Space - O(N*L)
*/
func groupAnagrams(strs []string) [][]string {
    hash:=make(map[[26]int][]string)
    for _, str:=range strs {
        var count [26]int
        for i:=0;i<len(str);i++ {
            count[str[i]-'a']++
        }
        hash[count]=append(hash[count], str)
    }
    ans:=make([][]string, 0)
    for _,v:=range hash {
        ans=append(ans, v)
    }
    return ans
}