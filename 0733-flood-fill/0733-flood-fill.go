func floodFill(image [][]int, sr int, sc int, color int) [][]int {
    var helper func(sr, sc, colorx int) 
    helper = func(sr, sc int, colorx int){
        if sr<0 || sr>=len(image)|| sc<0 || sc>=len(image[0]) {
            return 
        }
        if image[sr][sc]==colorx {
            image[sr][sc]=color
            helper(sr+1, sc, colorx)
            helper(sr-1, sc, colorx)
            helper(sr, sc+1, colorx)
            helper(sr, sc-1, colorx)
        }
    }
    if image[sr][sc]==color {
        return image
    }
    helper(sr, sc, image[sr][sc])
    return image
}