/*
Time - O(m*n)
Space - O(m+n)
*/
func setZeroes(matrix [][]int)  {
    rowMap:=make([]int, 0)
    colMap:=make([]int, 0)
    for i:=0;i<len(matrix);i++ {
        for j:=0;j<len(matrix[0]);j++ {
            if matrix[i][j]==0 {
                rowMap=append(rowMap, i)
                colMap=append(colMap, j)
            }
        }
    }
    for i:=0;i<len(rowMap);i++ {
        for j:=0;j<len(matrix[0]);j++ {
            matrix[rowMap[i]][j]=0
        }
    }
    for j:=0;j<len(colMap);j++ {
        for i:=0;i<len(matrix);i++ {
            matrix[i][colMap[j]]=0
        }
    }
}