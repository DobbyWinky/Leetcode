/*
Time - O(1)
Space - O(1)
*/
func isValidSudoku(board [][]byte) bool {
    r:=make(map[[2]int]bool)
    c:=make(map[[2]int]bool)
    b:=make(map[[2]int]bool)
    for i:=0;i<9;i++ {
        for j:=0;j<9;j++ {
            val:=board[i][j]
            if val!='.' {
                if r[[2]int{i,int(val-'0')}] {
                    fmt.Println("Hello1", i,j)
                    return false
                }
                r[[2]int{i,int(val-'0')}]=true
                if c[[2]int{j,int(val-'0')}] {
                    fmt.Println("Hello2", i,j)
                    return false
                }
                c[[2]int{j,int(val-'0')}]=true
                if b[[2]int{3*(i/3)+j/3, int(val-'0')}] {
                    fmt.Println("Hello3", i,j)
                    return false
                }
                b[[2]int{3*(i/3)+j/3, int(val-'0')}]=true
            }
        }
    }
    return true
}