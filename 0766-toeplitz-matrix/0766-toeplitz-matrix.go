func isDiagonal(matrix[][]int, r,c int) bool {
    val:=matrix[r][c]
    for i,j:=r+1,c+1;i<len(matrix)&&j<len(matrix[0]);i,j=i+1,j+1 {
        if matrix[i][j]!=val {
            return false
        }
    }
    return true
}
func isToeplitzMatrix(matrix [][]int) bool {
    for j:=0;j<len(matrix[0]);j++ {
        if !isDiagonal(matrix, 0, j) {
            return false
        }
    }
    for i:=0;i<len(matrix);i++ {
        if !isDiagonal(matrix, i, 0) {
            return false
        }
    }
    return true
}